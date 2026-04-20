"""Query processing helpers for chat retrieval."""
import re
from typing import Any, Dict, List

from sqlalchemy import extract, or_

from app.models.document import Document, DocumentType


def process_query(query: str) -> Dict[str, Any]:
    """Clean query text and extract Dublin Core entities plus keywords."""
    cleaned = clean_query(query)
    entities = extract_entities(query)
    keywords = extract_keywords(cleaned, entities)

    result = {
        "original_query": query,
        "cleaned_query": cleaned,
        "entities": entities,
        "keywords": keywords,
    }

    print("========== QUERY PROCESSING ==========")
    print(f"  Original : {query}")
    print(f"  Cleaned  : {cleaned}")
    print(f"  Entities : {entities}")
    print(f"  Keywords : {keywords}")
    print("=======================================")

    return result


def clean_query(query: str) -> str:
    """Clean and normalize the query text."""
    cleaned = query.lower().strip()
    cleaned = re.sub(r'[?!.,;:]+$', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned


def extract_entities(query: str) -> Dict[str, Any]:
    """Extract Dublin Core-mapped entities from query using regex patterns."""
    query_lower = query.lower()
    entities: Dict[str, Any] = {}

    year_match = re.search(r'\b(19\d{2}|20\d{2})\b', query)
    if year_match:
        entities["year"] = int(year_match.group(1))

    author_patterns = [
        r'(?:oleh|penulis|author|ditulis oleh|karya)\s+([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*)',
        r'(?:oleh|penulis|author|ditulis oleh|karya)\s+([a-zA-Z]+(?:\s+[a-zA-Z]+){0,3})',
    ]
    for pattern in author_patterns:
        author_match = re.search(pattern, query, re.IGNORECASE)
        if author_match:
            author_name = author_match.group(1).strip()
            stopwords = {'dan', 'di', 'yang', 'untuk', 'dari', 'pada', 'tahun', 'tentang'}
            name_words = [w for w in author_name.split() if w.lower() not in stopwords]
            if name_words:
                entities["creator"] = " ".join(name_words)
            break

    lang_patterns = {
        r'(?:bahasa|berbahasa|dalam bahasa)\s+(indonesia|inggris|english|indonesian|melayu|arab|jepang|mandarin)': {
            'indonesia': 'id', 'indonesian': 'id',
            'inggris': 'en', 'english': 'en',
            'melayu': 'ms', 'arab': 'ar', 'jepang': 'ja', 'mandarin': 'zh',
        }
    }
    for pattern, lang_map in lang_patterns.items():
        lang_match = re.search(pattern, query_lower)
        if lang_match:
            lang_name = lang_match.group(1)
            entities["language"] = lang_map.get(lang_name, lang_name)
            break

    publisher_match = re.search(
        r'(?:diterbitkan(?:\s+oleh)?|penerbit|published\s+by)\s+([a-zA-Z]+(?:\s+[a-zA-Z]+){0,4})',
        query,
        re.IGNORECASE,
    )
    if publisher_match:
        entities["publisher"] = publisher_match.group(1).strip()

    location_match = re.search(
        r'\bdi\s+(Indonesia|Jawa|Sumatera|Kalimantan|Sulawesi|Bali|Papua|'
        r'Jakarta|Bandung|Surabaya|Medan|Yogyakarta|Semarang|Malang|'
        r'Asia|Eropa|Amerika|Afrika|Australia)\b',
        query,
        re.IGNORECASE,
    )
    if location_match:
        entities["location"] = location_match.group(1)

    journal_match = re.search(
        r'(?:jurnal|journal|majalah|di\s+jurnal|di\s+journal)\s+([a-zA-Z]+(?:\s+[a-zA-Z]+){0,4})',
        query,
        re.IGNORECASE,
    )
    if journal_match:
        entities["source"] = journal_match.group(1).strip()

    doi_match = re.search(r'(10\.\d{4,}/[^\s]+)', query)
    if doi_match:
        entities["doi"] = doi_match.group(1)

    type_map = {
        r'\b(thesis|tesis|skripsi|disertasi)\b': DocumentType.THESIS,
        r'\b(conference|konferensi|seminar|prosiding)\b': DocumentType.CONFERENCE,
        r'\b(buku|book)\b': DocumentType.BOOK,
        r'\b(laporan|report)\b': DocumentType.REPORT,
        r'\b(jurnal|journal|artikel)\b': DocumentType.JOURNAL,
    }
    for pattern, doc_type in type_map.items():
        if re.search(pattern, query_lower):
            entities["doc_type"] = doc_type
            break

    return entities


def extract_keywords(cleaned_query: str, entities: Dict[str, Any] = None) -> List[str]:
    """Extract meaningful keywords from query, excluding already-extracted entity values."""
    stopwords = {
        'di', 'dan', 'yang', 'untuk', 'dengan', 'dari', 'ke', 'ini', 'itu',
        'adalah', 'pada', 'dalam', 'oleh', 'akan', 'atau', 'juga', 'sudah',
        'ada', 'bisa', 'dapat', 'saya', 'apa', 'bagaimana', 'mengapa', 'kapan',
        'tentang', 'mengenai', 'terkait', 'seputar', 'informasi', 'jelaskan',
        'hasil', 'penelitian', 'penulis', 'author', 'bahasa', 'berbahasa',
        'tahun', 'diterbitkan', 'penerbit', 'jurnal', 'journal', 'oleh',
        'karya', 'ditulis', 'published',
    }

    words = cleaned_query.split()
    keywords = [w for w in words if w not in stopwords and len(w) > 2]

    if entities:
        entity_words = set()
        for val in entities.values():
            if isinstance(val, str):
                entity_words.update(val.lower().split())
            elif isinstance(val, int):
                entity_words.add(str(val))
        keywords = [k for k in keywords if k not in entity_words]

    return keywords


def build_metadata_filters(entities: Dict[str, Any]) -> List:
    """Build SQLAlchemy filter conditions from extracted entities."""
    filters = []

    if not entities:
        return filters

    if "year" in entities:
        filters.append(extract('year', Document.date) == entities["year"])

    if "creator" in entities:
        creator_val = f"%{entities['creator']}%"
        filters.append(or_(Document.creator.ilike(creator_val), Document.contributor.ilike(creator_val)))

    if "language" in entities:
        filters.append(Document.language.ilike(f"%{entities['language']}%"))

    if "publisher" in entities:
        filters.append(Document.publisher.ilike(f"%{entities['publisher']}%"))

    if "location" in entities:
        filters.append(Document.coverage.ilike(f"%{entities['location']}%"))

    if "source" in entities:
        filters.append(Document.source.ilike(f"%{entities['source']}%"))

    if "doi" in entities:
        filters.append(Document.doi == entities["doi"])

    if "doc_type" in entities:
        filters.append(Document.type == entities["doc_type"])

    print(f"  Metadata filters: {len(filters)} applied")
    return filters


def calculate_keyword_score(content: str, doc: Document, keywords: List[str]) -> float:
    """Calculate keyword matching score against content and Dublin Core metadata."""
    if not keywords:
        return 0.0

    content_lower = content.lower()
    date_str = str(doc.date) if doc.date else ""
    metadata_fields = {
        'title': (doc.title.lower() if doc.title else "", 3),
        'keywords': (doc.keywords.lower() if doc.keywords else "", 2.5),
        'abstract': (doc.abstract.lower() if doc.abstract else "", 2),
        'description': (doc.description.lower() if doc.description else "", 1.5),
        'creator': (doc.creator.lower() if doc.creator else "", 1.5),
        'contributor': (doc.contributor.lower() if doc.contributor else "", 1.5),
        'publisher': (doc.publisher.lower() if doc.publisher else "", 1),
        'source': (doc.source.lower() if doc.source else "", 1),
        'relation': (doc.relation.lower() if doc.relation else "", 1),
        'language': (doc.language.lower() if doc.language else "", 0.5),
        'date': (date_str, 0.5),
    }

    total_score = 0
    max_possible = 0
    for keyword in keywords:
        keyword_matched = False
        for _field_name, (field_value, weight) in metadata_fields.items():
            if keyword in field_value:
                total_score += weight
                keyword_matched = True
                break

        if not keyword_matched and keyword in content_lower:
            total_score += 0.5

        max_possible += 3

    return min(total_score / max_possible, 1.0) if max_possible > 0 else 0.0
