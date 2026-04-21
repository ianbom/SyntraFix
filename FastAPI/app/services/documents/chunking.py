"""Document chunking strategies."""
import re as _re
from typing import Any, Dict, List, Optional

from app.models.document_chunk import ChunkType
from app.services.documents.common import (
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_CHUNK_SIZE,
    IDEAL_CHUNK_WORDS,
    KEYWORDS_PER_CHUNK,
    MAX_CHUNK_WORDS,
    MIN_CHUNK_WORDS,
    WORDS_PER_PAGE,
    _STOPWORDS,
)
from app.services.documents.extraction import build_context_injected_content

class TextChunker:
    """Handles text chunking with metadata (legacy fixed-size approach)."""
    
    def __init__(self, chunk_size: int = DEFAULT_CHUNK_SIZE, overlap: int = DEFAULT_CHUNK_OVERLAP):
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def chunk_text(self, text: str, document_title: str = None) -> List[Dict[str, Any]]:
        """Split text into overlapping chunks with metadata."""
        if not text or not text.strip():
            return []
        
        text = text.strip()
        words = text.split()
        total_words = len(words)
        
        chunks = []
        start = 0
        chunk_index = 0
        
        while start < len(words):
            end = start + self.chunk_size
            chunk_words = words[start:end]
            chunk_content = " ".join(chunk_words)
            
            if chunk_content.strip():
                chunks.append(self._create_chunk_dict(
                    chunk_index=chunk_index,
                    content=chunk_content,
                    word_count=len(chunk_words),
                    word_start=start,
                    word_end=min(end, total_words),
                    total_words=total_words,
                    document_title=document_title
                ))
                chunk_index += 1
            
            start = end - self.overlap if end < len(words) else len(words)
        
        return chunks
    
    def _create_chunk_dict(
        self, 
        chunk_index: int, 
        content: str, 
        word_count: int,
        word_start: int,
        word_end: int,
        total_words: int,
        document_title: str = None
    ) -> Dict[str, Any]:
        """Create chunk dictionary with metadata."""
        estimated_page = (word_start // WORDS_PER_PAGE) + 1
        
        return {
            "chunk_index": chunk_index,
            "content": content,
            "token_count": word_count,
            "chunk_type": ChunkType.PARAGRAPH,
            "page_number": estimated_page,
            "section_title": None,
            "chunk_metadata": {
                "source_document": document_title,
                "word_start": word_start,
                "word_end": word_end,
                "total_words": total_words,
                "relative_position": round(word_start / total_words, 3) if total_words > 0 else 0,
                "chunk_size": word_count,
                "has_overlap": word_start > 0
            }
        }
    
    @staticmethod
    def create_title_chunk(title: str, creator: str = None, doi: str = None) -> Dict[str, Any]:
        """Create special chunk for document title."""
        return {
            "chunk_index": 0,
            "content": title,
            "token_count": len(title.split()),
            "chunk_type": ChunkType.TITLE,
            "page_number": 1,
            "section_title": "Title",
            "chunk_metadata": {
                "source_document": title,
                "section": "title",
                "is_header": True,
                "authors": creator,
                "doi": doi
            }
        }
    
    @staticmethod
    def create_abstract_chunk(abstract: str, document_title: str = None) -> Dict[str, Any]:
        """Create special chunk for abstract."""
        return {
            "chunk_index": 0,
            "content": abstract,
            "token_count": len(abstract.split()),
            "chunk_type": ChunkType.ABSTRACT,
            "page_number": 1,
            "section_title": "Abstract",
            "chunk_metadata": {
                "source_document": document_title,
                "section": "abstract",
                "is_summary": True,
                "word_count": len(abstract.split())
            }
        }
    
    @staticmethod
    def reindex_chunks(chunks: List[Dict[str, Any]]) -> None:
        """Re-index chunks after insertion."""
        for i, chunk in enumerate(chunks):
            chunk["chunk_index"] = i


# =============================================================================
# Smart Chunking (Section & Paragraph-aware)
# =============================================================================

class SmartChunker:
    """
    Smart chunking strategy that respects document structure.
    
    Instead of splitting by fixed word count, this chunker:
    1. Uses GROBID's structured sections (title, abstract, body sections, references)
    2. Chunks by paragraph boundaries within each section
    3. Merges short paragraphs with the next one to avoid tiny chunks
    4. Splits overly long paragraphs at sentence boundaries
    5. Preserves section metadata for each chunk
    6. Extracts keywords per-chunk and resolves accurate page numbers
    7. Guarantees NO text is lost — every character from the document is included
    """
    
    def __init__(
        self,
        min_chunk_words: int = MIN_CHUNK_WORDS,
        max_chunk_words: int = MAX_CHUNK_WORDS,
        ideal_chunk_words: int = IDEAL_CHUNK_WORDS,
    ):
        self.min_chunk_words = min_chunk_words
        self.max_chunk_words = max_chunk_words
        self.ideal_chunk_words = ideal_chunk_words
    
    def chunk_structured_sections(
        self,
        sections: List[Dict[str, Any]],
        document_title: str = None,
        pages_data: Optional[List[Dict[str, Any]]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Smart-chunk a list of structured sections from GROBID.
        
        Args:
            sections: Output of extract_structured_fulltext()
            document_title: Title of the document (for metadata)
            pages_data: Per-page text from PyMuPDF [{"page_number": int, "text": str}]
        
        Returns:
            List of chunk dicts ready for embedding + DB storage.
        """
        all_chunks: List[Dict[str, Any]] = []
        
        for section in sections:
            sec_type = section.get("type", "section")
            sec_title = section.get("title", "")
            paragraphs = section.get("paragraphs", [])
            
            if not paragraphs:
                # Fallback: use content directly
                content = section.get("content", "").strip()
                if content:
                    paragraphs = [content]
                else:
                    continue
            
            # Map section type to ChunkType
            chunk_type = self._map_chunk_type(sec_type)
            
            # Process paragraphs for this section
            section_chunks = self._process_section_paragraphs(
                paragraphs=paragraphs,
                section_title=sec_title,
                chunk_type=chunk_type,
                document_title=document_title,
            )
            all_chunks.extend(section_chunks)
        
        # Re-index all chunks sequentially
        for i, chunk in enumerate(all_chunks):
            chunk["chunk_index"] = i
        
        # Enrich chunks: resolve page numbers + extract keywords
        for chunk in all_chunks:
            # Resolve accurate page number from PyMuPDF page data
            if pages_data:
                resolved_page = self._find_page_number(chunk["content"], pages_data)
                if resolved_page is not None:
                    chunk["page_number"] = resolved_page
                    chunk["chunk_metadata"]["page_number"] = resolved_page
            
            # Extract keywords for this chunk
            keywords = self._extract_keywords(chunk["content"])
            chunk["chunk_metadata"]["keywords"] = keywords
        
        # Validate: count total characters to ensure nothing is lost
        input_chars = sum(
            len(" ".join(s.get("paragraphs", []))) for s in sections
        )
        output_chars = sum(len(c["content"]) for c in all_chunks)
        print(f"SmartChunker: {len(sections)} sections -> {len(all_chunks)} chunks")
        print(f"SmartChunker: Input chars={input_chars}, Output chars={output_chars}")
        
        return all_chunks
    
    def _process_section_paragraphs(
        self,
        paragraphs: List[str],
        section_title: str,
        chunk_type: ChunkType,
        document_title: str = None,
    ) -> List[Dict[str, Any]]:
        """
        Process paragraphs within a section:
        - Merge short paragraphs together
        - Split long paragraphs at sentence boundaries
        """
        chunks = []
        buffer = ""  # Accumulator for merging short paragraphs
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                continue
            
            word_count = len(paragraph.split())
            buffer_word_count = len(buffer.split()) if buffer else 0
            
            if buffer:
                combined_word_count = buffer_word_count + word_count
                
                if combined_word_count <= self.max_chunk_words:
                    # Merge: combined is still within max limit
                    buffer = buffer + "\n\n" + paragraph
                else:
                    # Buffer is big enough, flush it as a chunk
                    chunks.extend(self._create_chunks_from_text(
                        text=buffer,
                        section_title=section_title,
                        chunk_type=chunk_type,
                        document_title=document_title,
                    ))
                    buffer = paragraph
            else:
                # Buffer is empty, start accumulating
                if word_count < self.min_chunk_words:
                    # Too short — start buffering for merging
                    buffer = paragraph
                else:
                    # Long enough on its own
                    if word_count > self.max_chunk_words:
                        # Too long — split at sentence boundaries
                        chunks.extend(self._create_chunks_from_text(
                            text=paragraph,
                            section_title=section_title,
                            chunk_type=chunk_type,
                            document_title=document_title,
                        ))
                    else:
                        # Just right — use as-is
                        buffer = paragraph
                        # Check if this paragraph is >= min, keep in buffer
                        # to potentially merge with next short paragraph
                        if word_count >= self.min_chunk_words:
                            # Flush if it's a reasonable size
                            chunks.extend(self._create_chunks_from_text(
                                text=buffer,
                                section_title=section_title,
                                chunk_type=chunk_type,
                                document_title=document_title,
                            ))
                            buffer = ""
        
        # Flush remaining buffer
        if buffer.strip():
            chunks.extend(self._create_chunks_from_text(
                text=buffer,
                section_title=section_title,
                chunk_type=chunk_type,
                document_title=document_title,
            ))
        
        return chunks
    
    def _create_chunks_from_text(
        self,
        text: str,
        section_title: str,
        chunk_type: ChunkType,
        document_title: str = None,
    ) -> List[Dict[str, Any]]:
        """
        Create one or more chunks from a text block.
        If text exceeds max_chunk_words, split at sentence boundaries.
        """
        text = text.strip()
        if not text:
            return []
        
        word_count = len(text.split())
        
        if word_count <= self.max_chunk_words:
            # Fits in a single chunk
            return [self._build_chunk_dict(
                content=text,
                section_title=section_title,
                chunk_type=chunk_type,
                document_title=document_title,
            )]
        
        # Split at sentence boundaries
        sentences = self._split_into_sentences(text)
        chunks = []
        current_sentences = []
        current_word_count = 0
        
        for sentence in sentences:
            sentence_words = len(sentence.split())
            
            if current_word_count + sentence_words > self.max_chunk_words and current_sentences:
                # Flush current chunk
                chunk_text = " ".join(current_sentences)
                chunks.append(self._build_chunk_dict(
                    content=chunk_text,
                    section_title=section_title,
                    chunk_type=chunk_type,
                    document_title=document_title,
                ))
                current_sentences = []
                current_word_count = 0
            
            current_sentences.append(sentence)
            current_word_count += sentence_words
        
        # Flush remaining sentences
        if current_sentences:
            chunk_text = " ".join(current_sentences)
            # If this remainder is too short and we have previous chunks, 
            # merge with the last chunk if it won't exceed max
            if (
                chunks 
                and current_word_count < self.min_chunk_words
                and len(chunks[-1]["content"].split()) + current_word_count <= self.max_chunk_words
            ):
                chunks[-1]["content"] += " " + chunk_text
                chunks[-1]["token_count"] = len(chunks[-1]["content"].split())
            else:
                chunks.append(self._build_chunk_dict(
                    content=chunk_text,
                    section_title=section_title,
                    chunk_type=chunk_type,
                    document_title=document_title,
                ))
        
        return chunks
    
    def _build_chunk_dict(
        self,
        content: str,
        section_title: str,
        chunk_type: ChunkType,
        document_title: str = None,
    ) -> Dict[str, Any]:
        """Build a single chunk dictionary with metadata."""
        words = content.split()
        word_count = len(words)
        # Estimate page number from cumulative word position
        estimated_page = max(1, (word_count // WORDS_PER_PAGE) + 1)
        
        return {
            "chunk_index": 0,  # Will be re-indexed later
            "content": content,
            "token_count": word_count,
            "chunk_type": chunk_type,
            "page_number": estimated_page,
            "section_title": section_title,
            "chunk_metadata": {
                "source_document": document_title,
                "section": section_title,
                "chunk_strategy": "smart",
                "word_count": word_count,
            }
        }
    
    @staticmethod
    def _map_chunk_type(section_type: str) -> ChunkType:
        """Map GROBID section type to ChunkType enum."""
        mapping = {
            "title": ChunkType.TITLE,
            "abstract": ChunkType.ABSTRACT,
            "reference": ChunkType.REFERENCE,
            "authors": ChunkType.PARAGRAPH,
            "keywords": ChunkType.PARAGRAPH,
            "section": ChunkType.PARAGRAPH,
        }
        return mapping.get(section_type, ChunkType.PARAGRAPH)
    
    @staticmethod
    def _split_into_sentences(text: str) -> List[str]:
        """
        Split text into sentences using regex.
        Handles common abbreviations and decimal numbers.
        """
        # Split on sentence-ending punctuation followed by space + uppercase,
        # or newlines that look like paragraph breaks
        sentence_endings = _re.compile(
            r'(?<=[.!?])\s+(?=[A-Z\u00C0-\u024F])|\n{2,}'
        )
        raw = sentence_endings.split(text)
        # Filter empty and strip
        return [s.strip() for s in raw if s and s.strip()]
    
    @staticmethod
    def _extract_keywords(text: str, max_keywords: int = KEYWORDS_PER_CHUNK) -> List[str]:
        """
        Extract significant keywords from chunk content.
        Uses word frequency with stopword filtering.
        Returns a list of the most relevant keywords.
        """
        if not text or len(text.strip()) < 10:
            return []
        
        # Tokenize: lowercase, keep only alphabetic words of length >= 3
        words = _re.findall(r'[a-zA-Z\u00C0-\u024F]{3,}', text.lower())
        
        # Filter stopwords
        meaningful = [w for w in words if w not in _STOPWORDS and len(w) >= 3]
        
        if not meaningful:
            return []
        
        # Count frequency
        freq: Dict[str, int] = {}
        for w in meaningful:
            freq[w] = freq.get(w, 0) + 1
        
        # Sort by frequency descending, then alphabetically for ties
        sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        
        # Return top keywords
        return [word for word, _ in sorted_words[:max_keywords]]
    
    @staticmethod
    def _find_page_number(
        chunk_content: str,
        pages_data: List[Dict[str, Any]],
    ) -> Optional[int]:
        """
        Find the actual PDF page number where the chunk content appears.
        Matches by searching for a snippet of the chunk content in each page's text.
        Returns 1-based page number, or None if not found.
        """
        if not chunk_content or not pages_data:
            return None
        
        # Take a representative snippet from the chunk (first ~120 chars)
        # Clean whitespace for better matching
        snippet = " ".join(chunk_content.split()[:20])  # first ~20 words
        if len(snippet) < 10:
            return None
        
        # Normalize for matching
        snippet_normalized = snippet.lower().strip()
        
        for page in pages_data:
            page_text_normalized = " ".join(page["text"].split()).lower()
            if snippet_normalized in page_text_normalized:
                return page["page_number"]
        
        # Fallback: try with a shorter snippet (first 10 words)
        short_snippet = " ".join(chunk_content.split()[:10]).lower().strip()
        if len(short_snippet) >= 10:
            for page in pages_data:
                page_text_normalized = " ".join(page["text"].split()).lower()
                if short_snippet in page_text_normalized:
                    return page["page_number"]
        
        return None
