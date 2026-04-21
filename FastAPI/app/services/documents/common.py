"""Shared document service constants and data containers."""
from dataclasses import dataclass
from typing import Any, Dict, Optional

from app.models.document_chunk import ChunkType

MAX_PDF_SIZE = 50 * 1024 * 1024  # 50MB
DEFAULT_CHUNK_SIZE = 500
DEFAULT_CHUNK_OVERLAP = 50
WORDS_PER_PAGE = 500

MIN_CHUNK_WORDS = 80
MAX_CHUNK_WORDS = 800
IDEAL_CHUNK_WORDS = 400
KEYWORDS_PER_CHUNK = 7

_STOPWORDS = frozenset({
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "shall", "can", "need", "dare", "ought",
    "used", "to", "of", "in", "for", "on", "with", "at", "by", "from",
    "as", "into", "through", "during", "before", "after", "above", "below",
    "between", "out", "off", "over", "under", "again", "further", "then",
    "once", "here", "there", "when", "where", "why", "how", "all", "each",
    "every", "both", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very",
    "just", "because", "but", "and", "or", "if", "while", "about", "up",
    "that", "this", "these", "those", "it", "its", "he", "she", "they",
    "we", "you", "i", "me", "him", "her", "us", "them", "my", "your",
    "his", "our", "their", "what", "which", "who", "whom", "also", "et",
    "al", "etc", "fig", "figure", "table", "using", "based", "however",
    "therefore", "thus", "hence", "since", "although", "though", "yet",
    "still", "already", "even", "well", "back", "also", "much", "any",
    "dan", "atau", "yang", "di", "ke", "dari", "pada", "untuk", "dengan",
    "adalah", "ini", "itu", "akan", "oleh", "telah", "sudah", "belum",
    "tidak", "bukan", "dapat", "bisa", "harus", "juga", "serta", "dalam",
    "antara", "melalui", "karena", "jika", "bila", "agar", "supaya",
    "tetapi", "namun", "selain", "meskipun", "walaupun", "bahwa", "hal",
    "lebih", "sangat", "saat", "ketika", "setelah", "sebelum", "secara",
    "seperti", "sebagai", "tersebut", "mereka", "kami", "kita", "saya",
    "yaitu", "yakni", "maupun", "adapun", "sedangkan", "maka", "pun",
})


@dataclass
class ChunkData:
    """Data class for chunk information."""
    chunk_index: int
    content: str
    token_count: int
    chunk_type: ChunkType
    page_number: Optional[int] = None
    section_title: Optional[str] = None
    chunk_metadata: Optional[Dict[str, Any]] = None
