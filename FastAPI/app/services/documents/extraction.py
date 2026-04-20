"""PDF extraction and metadata validation helpers."""
import re
from typing import Any, Dict, List, Optional

from fastapi import HTTPException

def _import_pymupdf():
    """Import PyMuPDF module with fitz fallback."""
    try:
        import pymupdf as pymupdf_module
        return pymupdf_module
    except ImportError:
        try:
            import fitz as pymupdf_module
            return pymupdf_module
        except ImportError:
            return None


def extract_raw_pdf_text(file_content: bytes):
    """
    Extract raw text from PDF using PyMuPDF.
    Returns (raw_text: str, pages_data: list[dict]).
    Each page_data has: { page_number: int, text: str }
    """
    pymupdf = _import_pymupdf()
    if pymupdf is None:
        print("PyMuPDF not installed")
        return "", []
    
    try:
        doc = pymupdf.open(stream=file_content, filetype="pdf")
        pages_text = []
        pages_data = []
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text("text")
            if text and text.strip():
                pages_text.append(text.strip())
                pages_data.append({
                    "page_number": page_num + 1,
                    "text": text.strip()
                })
        
        doc.close()
        raw_text = "\n\n".join(pages_text)
        print(f"  PyMuPDF: Extracted {len(raw_text)} chars from {len(pages_text)} pages")
        return raw_text, pages_data
        
    except Exception as e:
        print(f"PyMuPDF extraction error: {e}")
        return "", []


def _normalize_table_rows(rows: Optional[List[List[Any]]]) -> List[List[str]]:
    """Normalize table rows to a rectangular list of strings."""
    if not rows:
        return []

    cleaned_rows: List[List[str]] = []
    max_columns = 0

    for row in rows:
        if row is None:
            continue
        cleaned_row = [str(cell).strip() if cell is not None else "" for cell in row]
        if any(cell for cell in cleaned_row):
            cleaned_rows.append(cleaned_row)
            max_columns = max(max_columns, len(cleaned_row))

    if not cleaned_rows or max_columns == 0:
        return []

    return [row + [""] * (max_columns - len(row)) for row in cleaned_rows]


_CAPTION_PATTERN = re.compile(
    r"^\s*(table|tabel|figure|gambar)\s*([0-9]+(?:[.\-][0-9]+)*)\s*[:.\-]?\s*(.+)?\s*$",
    re.IGNORECASE,
)


def _extract_caption_candidates_from_page(page) -> List[Dict[str, Any]]:
    """Extract caption-like lines and their vertical positions from page text."""
    candidates: List[Dict[str, Any]] = []

    try:
        text_dict = page.get_text("dict")
    except Exception:
        return candidates

    for block in text_dict.get("blocks", []):
        if block.get("type") != 0:
            continue

        for line in block.get("lines", []):
            spans = line.get("spans", [])
            line_text = " ".join(
                (span.get("text") or "").strip() for span in spans if (span.get("text") or "").strip()
            )
            cleaned_text = " ".join(line_text.split())
            if not cleaned_text:
                continue

            match = _CAPTION_PATTERN.match(cleaned_text)
            if not match:
                continue

            bbox = line.get("bbox") or block.get("bbox")
            if not bbox or len(bbox) < 4:
                continue

            y0 = float(bbox[1])
            y1 = float(bbox[3])
            candidates.append({
                "prefix": match.group(1).lower(),
                "number": match.group(2),
                "caption": cleaned_text,
                "y_center": (y0 + y1) / 2.0,
                "y0": y0,
                "y1": y1,
            })

    return candidates


def _match_caption_to_bbox(
    caption_candidates: List[Dict[str, Any]],
    bbox: Optional[List[float]],
    allowed_prefixes: set[str],
    used_caption_indexes: set[int],
    max_distance: float = 220.0,
    fallback_to_nearest: bool = True,
) -> Optional[Dict[str, Any]]:
    """Find nearest valid caption to an element bbox (supports above/below captions)."""
    target_y0 = target_y1 = None
    if bbox and len(bbox) >= 4:
        target_y0 = float(bbox[1])
        target_y1 = float(bbox[3])

    best_idx = None
    best_distance = None
    nearest_idx = None
    nearest_distance = None

    for idx, candidate in enumerate(caption_candidates):
        if idx in used_caption_indexes:
            continue
        if candidate.get("prefix") not in allowed_prefixes:
            continue

        if target_y0 is None or target_y1 is None:
            best_idx = idx
            break

        y_center = float(candidate["y_center"])
        distance = min(abs(y_center - target_y0), abs(y_center - target_y1))

        if nearest_distance is None or distance < nearest_distance:
            nearest_idx = idx
            nearest_distance = distance

        # Accept caption when reasonably close to the visual block.
        if distance <= max_distance and (best_distance is None or distance < best_distance):
            best_idx = idx
            best_distance = distance

    if best_idx is None and fallback_to_nearest and nearest_idx is not None:
        best_idx = nearest_idx

    if best_idx is None:
        return None

    used_caption_indexes.add(best_idx)
    return caption_candidates[best_idx]


def _split_text_row_to_cells(row_text: str) -> List[str]:
    """Split one textual row into potential table cells."""
    row_text = " ".join((row_text or "").split())
    if not row_text:
        return []

    # Common delimiters in extracted PDF rows.
    candidates = re.split(r"\s{2,}|\t+|\s+\|\s+|\s*;\s*", row_text)
    cleaned = [cell.strip() for cell in candidates if cell and cell.strip()]

    # Fallback: split by single '|' if still a single cell.
    if len(cleaned) <= 1 and "|" in row_text:
        cleaned = [cell.strip() for cell in row_text.split("|") if cell.strip()]

    return cleaned


def _extract_table_rows_near_caption(
    page,
    caption_info: Dict[str, Any],
    caption_candidates: List[Dict[str, Any]],
) -> List[List[str]]:
    """
    Fallback table extraction from text lines below a table caption.
    Useful when `find_tables()` cannot detect table structure.
    """
    try:
        text_dict = page.get_text("dict")
    except Exception:
        return []

    caption_bottom = float(caption_info.get("y1") or caption_info.get("y_center") or 0.0)
    next_caption_y = None
    for candidate in caption_candidates:
        cand_y0 = float(candidate.get("y0") or 0.0)
        if cand_y0 > caption_bottom and (next_caption_y is None or cand_y0 < next_caption_y):
            next_caption_y = cand_y0

    scan_limit = caption_bottom + 320.0
    if next_caption_y is not None:
        scan_limit = min(scan_limit, max(caption_bottom + 40.0, next_caption_y - 2.0))

    rows: List[List[str]] = []
    for block in text_dict.get("blocks", []):
        if block.get("type") != 0:
            continue

        for line in block.get("lines", []):
            bbox = line.get("bbox") or block.get("bbox")
            if not bbox or len(bbox) < 4:
                continue

            y0 = float(bbox[1])
            y1 = float(bbox[3])
            y_center = (y0 + y1) / 2.0
            if y_center <= caption_bottom or y_center > scan_limit:
                continue

            line_text = " ".join(
                (span.get("text") or "").strip()
                for span in line.get("spans", [])
                if (span.get("text") or "").strip()
            )
            cleaned_text = " ".join(line_text.split())
            if not cleaned_text:
                continue
            if _CAPTION_PATTERN.match(cleaned_text):
                continue

            cells = _split_text_row_to_cells(cleaned_text)
            if len(cells) >= 2:
                rows.append(cells)

    normalized_rows = _normalize_table_rows(rows)
    if not normalized_rows:
        return []

    # Keep rows that look tabular.
    max_cols = max(len(row) for row in normalized_rows)
    if max_cols < 2:
        return []

    return normalized_rows


def extract_pdf_tables_and_images(file_content: bytes):
    """
    Extract tables and images from PDF using PyMuPDF.

    Returns:
        tables_data: list[dict] with page_number, table_index, caption, rows, row_count, column_count
        images_data: list[dict] with page_number, image_index, xref, extension, width, height, size_bytes, image_bytes
    """
    pymupdf = _import_pymupdf()
    if pymupdf is None:
        print("PyMuPDF not installed")
        return [], []

    tables_data: List[Dict[str, Any]] = []
    images_data: List[Dict[str, Any]] = []

    try:
        doc = pymupdf.open(stream=file_content, filetype="pdf")
    except Exception as e:
        print(f"PyMuPDF open error (tables/images): {e}")
        return [], []

    try:
        for page_num in range(len(doc)):
            page = doc[page_num]
            page_number = page_num + 1
            caption_candidates = _extract_caption_candidates_from_page(page)
            used_caption_indexes: set[int] = set()
            page_table_index = 0

            # --- Table extraction ---
            if hasattr(page, "find_tables"):
                try:
                    detected_tables = []
                    seen_table_keys = set()

                    # Try default strategy first, then text-based strategy fallback.
                    table_strategies = [
                        {},
                        {"vertical_strategy": "text", "horizontal_strategy": "text"},
                    ]
                    for strategy in table_strategies:
                        try:
                            table_finder = page.find_tables(**strategy)
                        except TypeError:
                            table_finder = page.find_tables()
                        except Exception:
                            continue

                        for table in table_finder.tables:
                            table_bbox = list(table.bbox) if getattr(table, "bbox", None) else None
                            table_key = tuple(round(v, 1) for v in table_bbox) if table_bbox else None
                            if table_key and table_key in seen_table_keys:
                                continue
                            if table_key:
                                seen_table_keys.add(table_key)
                            detected_tables.append(table)

                    for table in detected_tables:
                        rows = _normalize_table_rows(table.extract())
                        if not rows:
                            continue

                        table_bbox = list(table.bbox) if getattr(table, "bbox", None) else None
                        caption_info = _match_caption_to_bbox(
                            caption_candidates=caption_candidates,
                            bbox=table_bbox,
                            allowed_prefixes={"table", "tabel"},
                            used_caption_indexes=used_caption_indexes,
                            max_distance=420.0,
                            fallback_to_nearest=True,
                        )
                        if not caption_info:
                            continue

                        page_table_index += 1
                        tables_data.append({
                            "page_number": page_number,
                            "table_index": page_table_index,
                            "rows": rows,
                            "row_count": len(rows),
                            "column_count": len(rows[0]) if rows else 0,
                            "caption": caption_info.get("caption"),
                            "extraction_method": "find_tables",
                        })
                except Exception as table_error:
                    print(f"PyMuPDF table extraction warning on page {page_number}: {table_error}")

            # Caption-driven fallback for tables missed by find_tables().
            for idx, caption_info in enumerate(caption_candidates):
                if idx in used_caption_indexes:
                    continue
                if caption_info.get("prefix") not in {"table", "tabel"}:
                    continue

                fallback_rows = _extract_table_rows_near_caption(
                    page=page,
                    caption_info=caption_info,
                    caption_candidates=caption_candidates,
                )
                if not fallback_rows:
                    continue

                used_caption_indexes.add(idx)
                page_table_index += 1
                tables_data.append({
                    "page_number": page_number,
                    "table_index": page_table_index,
                    "rows": fallback_rows,
                    "row_count": len(fallback_rows),
                    "column_count": len(fallback_rows[0]) if fallback_rows else 0,
                    "caption": caption_info.get("caption"),
                    "extraction_method": "caption_fallback",
                })

            # --- Image extraction ---
            try:
                page_images = page.get_images(full=True)
            except Exception as image_list_error:
                print(f"PyMuPDF image listing warning on page {page_number}: {image_list_error}")
                page_images = []

            seen_xrefs = set()
            for image_index, image_info in enumerate(page_images, start=1):
                if not image_info:
                    continue

                xref = image_info[0]
                if xref in seen_xrefs:
                    continue
                seen_xrefs.add(xref)

                image_bbox = None
                try:
                    image_rects = page.get_image_rects(xref)
                    if image_rects:
                        rect = image_rects[0]
                        image_bbox = [float(rect.x0), float(rect.y0), float(rect.x1), float(rect.y1)]
                except Exception:
                    image_bbox = None

                caption_info = _match_caption_to_bbox(
                    caption_candidates=caption_candidates,
                    bbox=image_bbox,
                    allowed_prefixes={"figure", "gambar"},
                    used_caption_indexes=used_caption_indexes,
                    max_distance=220.0,
                    fallback_to_nearest=False,
                )
                if not caption_info:
                    continue

                try:
                    extracted = doc.extract_image(xref)
                except Exception as image_error:
                    print(f"PyMuPDF image extraction warning (xref={xref}): {image_error}")
                    continue

                image_bytes = extracted.get("image")
                if not image_bytes:
                    continue

                extension = str(extracted.get("ext") or "bin").lower()
                width = extracted.get("width") or (image_info[2] if len(image_info) > 2 else None)
                height = extracted.get("height") or (image_info[3] if len(image_info) > 3 else None)

                images_data.append({
                    "page_number": page_number,
                    "image_index": image_index,
                    "xref": xref,
                    "extension": extension,
                    "width": width,
                    "height": height,
                    "size_bytes": len(image_bytes),
                    "image_bytes": image_bytes,
                    "caption": caption_info.get("caption"),
                })

        print(
            f"  PyMuPDF assets: extracted {len(tables_data)} tables and {len(images_data)} images"
        )
        return tables_data, images_data
    finally:
        doc.close()


def build_context_injected_content(
    content: str,
    document_title: Optional[str],
    section_title: Optional[str],
    page_number: Optional[int] = None,
    sub_section_title: Optional[str] = None,
) -> str:
    """Inject structural context header into a chunk content."""
    normalized_content = (content or "").strip()
    if not normalized_content:
        return ""

    header_lines = [
        f"[Dokumen: {document_title or 'Untitled Document'}]",
        f"[Section: {section_title or 'General'}]",
    ]

    if sub_section_title:
        header_lines.append(f"[Sub-section: {sub_section_title}]")
    if page_number is not None:
        header_lines.append(f"[Halaman: {page_number}]")

    return "\n".join(header_lines) + "\n\n" + normalized_content


def validate_metadata(metadata: Dict[str, Any], fulltext: str) -> Dict[str, Any]:
    """
    Final validation: ensure no critical field is empty.
    Generates fallback values if GROBID + LLM both failed.
    """
    from datetime import datetime as dt
    
    # Title: MUST exist
    title = metadata.get("title")
    if not title or title.strip() == "" or title.strip().lower() in ["untitled", "untitled document"]:
        if fulltext:
            first_line = fulltext.strip().split('\n')[0][:150].strip()
            if first_line and len(first_line) > 10:
                metadata["title"] = first_line
                print(f"  Fallback title from first line: {first_line[:80]}")
            else:
                metadata["title"] = f"Document-{hash(fulltext[:500]) % 100000}"
                print(f"  Fallback title from hash: {metadata['title']}")
        else:
            metadata["title"] = "Document tanpa judul"
    
    # Keywords: should exist
    if not metadata.get("keywords"):
        title_words = metadata["title"].split()
        keywords = [w for w in title_words if len(w) > 3][:5]
        if keywords:
            metadata["keywords"] = ", ".join(keywords)
            print(f"  Fallback keywords from title: {metadata['keywords']}")
    
    # Language: default to Indonesian if empty
    if not metadata.get("language"):
        metadata["language"] = "id"
        print("  Fallback language: id")
    
    # Description: generate from abstract or content
    if not metadata.get("description") and metadata.get("abstract"):
        metadata["description"] = metadata["abstract"][:200]
        print("  Fallback description from abstract")
    
    # Parse date string from LLM if it's a string
    if isinstance(metadata.get("date"), str):
        date_str = metadata["date"]
        parsed = None
        for fmt in ["%Y-%m-%d", "%Y-%m", "%Y", "%d %B %Y", "%B %Y"]:
            try:
                parsed = dt.strptime(date_str, fmt).date()
                break
            except ValueError:
                continue
        metadata["date"] = parsed
    
    print(f"  Final metadata validation complete. Title: {str(metadata.get('title', ''))[:80]}")
    return metadata
