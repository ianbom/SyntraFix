"""Markdown exports for inspecting document chunks and RAGAS test contexts."""
from pathlib import Path
import re
from typing import Any, Dict, Iterable, List, Tuple

DEFAULT_CHUNK_EXPORT_DIR = Path(__file__).resolve().parents[1] / "document_chunk"


def sanitize_markdown_filename(title: str) -> str:
    """Return a Windows-safe markdown filename stem."""
    clean_title = (title or "untitled_document").strip()
    clean_title = re.sub(r'[\\/:*?"<>|]', "_", clean_title)
    clean_title = re.sub(r"\s+", " ", clean_title).strip()
    clean_title = clean_title.rstrip(". ")
    return clean_title or "untitled_document"


def build_chunk_content_markdown(chunks: Iterable[Dict[str, Any]]) -> str:
    """Build markdown containing only chunk content separated by dividers."""
    contents: List[str] = []
    for chunk in chunks:
        content = (chunk.get("content") or "").strip()
        if content:
            contents.append(content)

    if not contents:
        return ""
    return "\n\n---\n\n".join(contents) + "\n"


def build_ragas_markdown(chunks: Iterable[Dict[str, Any]]) -> str:
    """Build markdown with question/context pairs for manual RAGAS dataset creation."""
    items: List[str] = []
    item_number = 1

    for chunk in chunks:
        content = (chunk.get("content") or "").strip()
        questions = chunk.get("_possibly_questions") or chunk.get("possibly_questions") or []
        if not content or not questions:
            continue

        for question in questions:
            clean_question = str(question).strip()
            if not clean_question:
                continue
            items.append(
                "\n".join(
                    [
                        f"## RAGAS Item {item_number}",
                        "",
                        "question:",
                        clean_question,
                        "",
                        "contexts:",
                        content,
                        "",
                        "ground_truth:",
                        content,
                    ]
                )
            )
            item_number += 1

    if not items:
        return ""
    return "\n\n---\n\n".join(items) + "\n"


def export_document_chunk_markdown_files(
    document_title: str,
    chunks: Iterable[Dict[str, Any]],
    output_dir: Path | str = DEFAULT_CHUNK_EXPORT_DIR,
) -> Tuple[Path, Path]:
    """Write chunk-only and RAGAS markdown files for a processed document."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    safe_title = sanitize_markdown_filename(document_title)
    content_path = output_path / f"{safe_title}.md"
    ragas_path = output_path / f"{safe_title}_ragas.md"
    chunk_list = list(chunks)

    content_path.write_text(build_chunk_content_markdown(chunk_list), encoding="utf-8")
    ragas_path.write_text(build_ragas_markdown(chunk_list), encoding="utf-8")

    return content_path, ragas_path
