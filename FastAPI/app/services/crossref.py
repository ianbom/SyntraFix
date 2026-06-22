"""Crossref metadata lookup and Dublin Core mapping helpers."""
from __future__ import annotations

import re
from datetime import date
from difflib import SequenceMatcher
from html import unescape
from typing import Any, Dict, Optional

import requests

from app.config import get_settings

settings = get_settings()

DOI_PATTERN = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
TRAILING_DOI_CHARS = ".,;:)]}>"
TITLE_STOP_WORDS = {
    "abstract",
    "abstrak",
    "keywords",
    "kata kunci",
    "author",
    "authors",
    "penulis",
}


def normalize_doi(doi: Optional[str]) -> Optional[str]:
    """Normalize a DOI string extracted from text or metadata."""
    if not doi:
        return None

    cleaned = doi.strip()
    cleaned = re.sub(r"^(doi:\s*|https?://(dx\.)?doi\.org/)", "", cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.strip().strip(TRAILING_DOI_CHARS)
    return cleaned.lower() or None


def extract_doi_from_text(text: str) -> Optional[str]:
    """Return the first DOI found in text."""
    if not text:
        return None

    match = DOI_PATTERN.search(text)
    if not match:
        return None
    return normalize_doi(match.group(0))


def extract_preliminary_metadata(raw_text: str) -> Dict[str, Optional[str]]:
    """Extract DOI and likely title before GROBID processing."""
    sample = (raw_text or "")[:12000]
    preliminary = {
        "doi": extract_doi_from_text(sample),
        "title": _extract_title_candidate(sample),
    }
    return {key: value for key, value in preliminary.items() if value}


def lookup_crossref_metadata(preliminary_metadata: Dict[str, Any]) -> Dict[str, Any]:
    """Lookup Crossref metadata by DOI first, then by title similarity."""
    if not preliminary_metadata:
        return {}

    try:
        doi = normalize_doi(preliminary_metadata.get("doi"))
        if doi:
            item = _lookup_by_doi(doi)
            if item:
                print(f"Crossref: found metadata by DOI {doi}")
                print(format_crossref_for_database(item))
                return format_crossref_for_database(item)

        title = preliminary_metadata.get("title")
        if title:
            item = _lookup_by_title(title)
            if item:
                print(f"Crossref: found metadata by title '{title[:80]}'")
                print(format_crossref_for_database(item))
                return format_crossref_for_database(item)
    except Exception as exc:
        print(f"Crossref: lookup skipped after error: {type(exc).__name__}: {exc}")

    return {}


def format_crossref_for_database(item: Dict[str, Any]) -> Dict[str, Any]:
    """Map one Crossref work item to the app's Dublin Core metadata fields."""
    title = _first_text(item.get("title"))
    abstract = _strip_markup(item.get("abstract"))
    doi = normalize_doi(item.get("DOI"))
    authors = [_format_author(author) for author in item.get("author") or []]
    authors = [author for author in authors if author]


    license_items = item.get("license") or []
    rights = None
    if license_items:
        first_license = license_items[0] or {}
        rights = first_license.get("URL") or first_license.get("content-version")

    subjects = item.get("subject") or []
    citation_count = item.get("is-referenced-by-count")
    if citation_count is None:
        citation_count = item.get("reference-count")

    return {
        "title": title,
        "creator": authors[0] if authors else None,
        "keywords": ", ".join(subjects) if subjects else None,
        "description": abstract,
        "publisher": item.get("publisher"),
        "contributor": ", ".join(authors[1:]) if len(authors) > 1 else None,
        "date": _extract_crossref_date(item),
        "format": "application/pdf",
        "identifier": doi or item.get("URL"),
        "source": _first_text(item.get("container-title")),
        "language": item.get("language"),
        "relation": None,
        "coverage": None,
        "rights": rights,
        "doi": doi,
        "abstract": abstract,
        "citation_count": citation_count or 0,
    }


def _headers() -> Dict[str, str]:
    user_agent = "SyntraFastAPI/1.0"
    mailto = getattr(settings, "CROSSREF_MAILTO", None)
    if mailto:
        user_agent = f"{user_agent} (mailto:{mailto})"
    return {"User-Agent": user_agent}


def _lookup_by_doi(doi: str) -> Optional[Dict[str, Any]]:
    url = f"{settings.CROSSREF_BASE_URL.rstrip('/')}/works/{doi}"
    response = requests.get(
        url,
        headers=_headers(),
        timeout=settings.CROSSREF_TIMEOUT_SECONDS,
    )
    if response.status_code != 200:
        return None
    return (response.json().get("message") or {}) or None


def _lookup_by_title(title: str) -> Optional[Dict[str, Any]]:
    url = f"{settings.CROSSREF_BASE_URL.rstrip('/')}/works"
    response = requests.get(
        url,
        params={"query.title": title, "rows": 3},
        headers=_headers(),
        timeout=settings.CROSSREF_TIMEOUT_SECONDS,
    )
    if response.status_code != 200:
        return None

    items = (response.json().get("message") or {}).get("items") or []
    best_item = None
    best_score = 0.0
    normalized_title = _normalize_title(title)

    for item in items:
        candidate = _first_text(item.get("title"))
        score = SequenceMatcher(None, normalized_title, _normalize_title(candidate)).ratio()
        if score > best_score:
            best_item = item
            best_score = score

    if best_item and best_score >= 0.85:
        return best_item
    return None


def _extract_title_candidate(text: str) -> Optional[str]:
    if not text:
        return None

    lines = [" ".join(line.split()) for line in text.splitlines()]
    candidates = [line for line in lines if _is_title_candidate(line)]
    return candidates[0] if candidates else None


def _is_title_candidate(line: str) -> bool:
    if not line or len(line) < 10 or len(line) > 220:
        return False
    lowered = line.strip().lower().rstrip(":")
    if lowered in TITLE_STOP_WORDS:
        return False
    if any(lowered.startswith(f"{word}:") for word in TITLE_STOP_WORDS):
        return False
    if re.fullmatch(r"[\d\s.]+", line):
        return False
    return True


def _first_text(value: Any) -> Optional[str]:
    if isinstance(value, list):
        for item in value:
            if isinstance(item, str) and item.strip():
                return " ".join(item.split())
        return None
    if isinstance(value, str) and value.strip():
        return " ".join(value.split())
    return None


def _format_author(author: Dict[str, Any]) -> Optional[str]:
    given = (author.get("given") or "").strip()
    family = (author.get("family") or "").strip()
    literal = (author.get("name") or "").strip()
    full_name = " ".join(part for part in [given, family] if part)
    return full_name or literal or None


def _strip_markup(value: Any) -> Optional[str]:
    if not isinstance(value, str) or not value.strip():
        return None
    text = re.sub(r"<[^>]+>", " ", value)
    text = unescape(text)
    return " ".join(text.split()) or None


def _extract_crossref_date(item: Dict[str, Any]) -> Optional[date]:
    for key in ("published-print", "published-online", "issued", "created", "deposited"):
        date_value = _date_from_parts(item.get(key))
        if date_value:
            return date_value
    return None


def _date_from_parts(value: Any) -> Optional[date]:
    parts_list = (value or {}).get("date-parts") if isinstance(value, dict) else None
    if not parts_list or not parts_list[0]:
        return None

    parts = parts_list[0]
    try:
        year = int(parts[0])
        month = int(parts[1]) if len(parts) > 1 else 1
        day = int(parts[2]) if len(parts) > 2 else 1
        return date(year, month, day)
    except (TypeError, ValueError):
        return None


def _normalize_title(title: Optional[str]) -> str:
    if not title:
        return ""
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()
