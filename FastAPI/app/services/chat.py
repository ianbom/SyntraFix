from typing import AsyncGenerator, List, Optional, Dict, Any, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import desc, func, extract, or_, case, literal
from fastapi import HTTPException
import re
import time

from app.models.chat import Conversation, Chat, ChatReference, ChatRole
from app.models.document_chunk import ChunkType, DocumentChunk
from app.schemas.chat import ChatRequest, ChatResponse, ConversationResponse
from app.services.llm import generate_response, generate_response_stream
from app.services.embedding import generate_embedding
from app.services.reranker import rerank_chunks
from app.services import chat_query, rag_prompt, retrieval
from app.models.document import Document, DocumentType

class ChatService:
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def _print_timing(function_name: str, elapsed_seconds: float):
        print(f"[SERVICE TIMING] {function_name}: {elapsed_seconds:.4f}s")

    @staticmethod
    def _chunk_type_value(chunk: DocumentChunk) -> Optional[str]:
        if chunk.chunk_type is None:
            return None
        return getattr(chunk.chunk_type, "value", str(chunk.chunk_type))

    @staticmethod
    def _is_noisy_visual_or_table_summary(candidate: Dict[str, Any]) -> bool:
        chunk_type = str(candidate.get("chunk_type") or "").lower()
        if chunk_type not in {ChunkType.IMAGE.value, ChunkType.TABLE.value}:
            return False

        content = " ".join(str(candidate.get("content") or "").lower().split())
        if not content:
            return True

        noisy_phrases = (
            "maaf, saya tidak dapat",
            "tidak dapat menginterpretasikan",
            "tidak dapat melihat",
            "tidak bisa melihat",
            "gambar tersebut tidak tersedia",
            "gambar tidak tersedia",
            "table tidak tersedia",
            "tabel tidak tersedia",
            "tidak tersedia dalam konteks",
            "unable to interpret",
            "cannot interpret",
            "cannot see",
            "image is not available",
            "table is not available",
        )
        return any(phrase in content for phrase in noisy_phrases)

    def create_conversation(self, user_id: int, title: str) -> Conversation:
        conversation = Conversation(user_id=user_id, title=title)
        self.db.add(conversation)
        self.db.commit()
        self.db.refresh(conversation)
        return conversation

    def get_conversation(self, conversation_id: int, user_id: int) -> Optional[Conversation]:
        return self.db.query(Conversation).filter(
            Conversation.id == conversation_id,
            Conversation.user_id == user_id
        ).first()

    def list_conversations(self, user_id: int, limit: int = 20, offset: int = 0) -> List[Conversation]:
        return self.db.query(Conversation).filter(
            Conversation.user_id == user_id
        ).order_by(desc(Conversation.updated_at)).offset(offset).limit(limit).all()

    def _handle_conversation(self, user_id: int, request: ChatRequest) -> Conversation:
        """Handle conversation creation or retrieval."""
        if request.conversation_id:
            conversation = self.get_conversation(request.conversation_id, user_id)
            if not conversation:
                raise HTTPException(status_code=404, detail="Conversation not found")
            return conversation
        else:
            title = " ".join(request.message.split()[:5])
            return self.create_conversation(user_id, title)

    def _save_chat_message(self, conversation_id: int, role: ChatRole, message: str) -> Chat:
        """Save a chat message to the database."""
        chat_msg = Chat(
            conversation_id=conversation_id,
            role=role,
            message=message
        )
        self.db.add(chat_msg)
        self.db.commit()
        self.db.refresh(chat_msg)
        return chat_msg

    # =========================================================================
    # Query Processing
    # =========================================================================

    def _process_query(self, query: str) -> Dict[str, Any]:
        """
        Process user query: clean text and extract Dublin Core entities.
        
        Returns:
            {
                "cleaned_query": str,
                "entities": { "year": ..., "creator": ..., ... },
                "keywords": [str]
            }
        """
        return chat_query.process_query(query)

    def _clean_query(self, query: str) -> str:
        """Clean and normalize the query text."""
        return chat_query.clean_query(query)

    def _extract_entities(self, query: str) -> Dict[str, Any]:
        """
        Extract Dublin Core-mapped entities from query using regex patterns.
        
        Mappings:
            year        → Document.date
            creator     → Document.creator / Document.contributor
            language    → Document.language
            publisher   → Document.publisher
            location    → Document.coverage
            source      → Document.source (journal/conference)
            doi         → Document.doi
            doc_type    → Document.type
            topic       → used for semantic search (not a hard filter)
        """
        query_lower = query.lower()
        entities = {}
        
        # 1. Year (4-digit number 1900-2099)
        year_match = re.search(r'\b(19\d{2}|20\d{2})\b', query)
        if year_match:
            entities["year"] = int(year_match.group(1))
        
        # 2. Creator/Author - patterns: "oleh X", "penulis X", "author X", "ditulis oleh X"
        author_patterns = [
            r'(?:oleh|penulis|author|ditulis oleh|karya)\s+([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*)',
            r'(?:oleh|penulis|author|ditulis oleh|karya)\s+([a-zA-Z]+(?:\s+[a-zA-Z]+){0,3})',
        ]
        for pattern in author_patterns:
            author_match = re.search(pattern, query, re.IGNORECASE)
            if author_match:
                author_name = author_match.group(1).strip()
                # Filter out stopwords that might be captured
                stopwords = {'dan', 'di', 'yang', 'untuk', 'dari', 'pada', 'tahun', 'tentang'}
                name_words = [w for w in author_name.split() if w.lower() not in stopwords]
                if name_words:
                    entities["creator"] = " ".join(name_words)
                break
        
        # 3. Language - patterns: "bahasa X", "berbahasa X", "dalam bahasa X"
        lang_patterns = {
            r'(?:bahasa|berbahasa|dalam bahasa)\s+(indonesia|inggris|english|indonesian|melayu|arab|jepang|mandarin)': {
                'indonesia': 'id', 'indonesian': 'id',
                'inggris': 'en', 'english': 'en',
                'melayu': 'ms', 'arab': 'ar', 'jepang': 'ja', 'mandarin': 'zh'
            }
        }
        for pattern, lang_map in lang_patterns.items():
            lang_match = re.search(pattern, query_lower)
            if lang_match:
                lang_name = lang_match.group(1)
                entities["language"] = lang_map.get(lang_name, lang_name)
                break
        
        # 4. Publisher - patterns: "diterbitkan X", "penerbit X", "published by X"
        publisher_match = re.search(
            r'(?:diterbitkan(?:\s+oleh)?|penerbit|published\s+by)\s+([a-zA-Z]+(?:\s+[a-zA-Z]+){0,4})',
            query, re.IGNORECASE
        )
        if publisher_match:
            entities["publisher"] = publisher_match.group(1).strip()
        
        # 5. Location/Coverage - patterns: "di X" (place names)
        location_match = re.search(
            r'\bdi\s+(Indonesia|Jawa|Sumatera|Kalimantan|Sulawesi|Bali|Papua|'
            r'Jakarta|Bandung|Surabaya|Medan|Yogyakarta|Semarang|Malang|'
            r'Asia|Eropa|Amerika|Afrika|Australia)\b',
            query, re.IGNORECASE
        )
        if location_match:
            entities["location"] = location_match.group(1)
        
        # 6. Source/Journal - patterns: "jurnal X", "journal X", "di jurnal X"
        journal_match = re.search(
            r'(?:jurnal|journal|majalah|di\s+jurnal|di\s+journal)\s+([a-zA-Z]+(?:\s+[a-zA-Z]+){0,4})',
            query, re.IGNORECASE
        )
        if journal_match:
            entities["source"] = journal_match.group(1).strip()
        
        # 7. DOI pattern
        doi_match = re.search(r'(10\.\d{4,}/[^\s]+)', query)
        if doi_match:
            entities["doi"] = doi_match.group(1)
        
        # 8. Document type - patterns: specific keywords
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

    def _extract_keywords(self, cleaned_query: str, entities: Dict[str, Any] = None) -> List[str]:
        """Extract meaningful keywords from query, excluding already-extracted entity values."""
        stopwords = {
            'di', 'dan', 'yang', 'untuk', 'dengan', 'dari', 'ke', 'ini', 'itu',
            'adalah', 'pada', 'dalam', 'oleh', 'akan', 'atau', 'juga', 'sudah',
            'ada', 'bisa', 'dapat', 'saya', 'apa', 'bagaimana', 'mengapa', 'kapan',
            'tentang', 'mengenai', 'terkait', 'seputar', 'informasi', 'jelaskan',
            'hasil', 'penelitian', 'penulis', 'author', 'bahasa', 'berbahasa',
            'tahun', 'diterbitkan', 'penerbit', 'jurnal', 'journal', 'oleh',
            'karya', 'ditulis', 'published'
        }
        
        words = cleaned_query.split()
        keywords = [w for w in words if w not in stopwords and len(w) > 2]
        
        # Remove entity values from keywords to avoid duplication
        if entities:
            entity_words = set()
            for key, val in entities.items():
                if isinstance(val, str):
                    entity_words.update(val.lower().split())
                elif isinstance(val, int):
                    entity_words.add(str(val))
            keywords = [k for k in keywords if k not in entity_words]
        
        return keywords

    # =========================================================================
    # Metadata Filtering
    # =========================================================================

    def _build_metadata_filters(self, entities: Dict[str, Any]) -> List:
        """
        Build SQLAlchemy filter conditions from extracted entities.
        Maps entities to Dublin Core columns in Document table.
        """
        filters = []
        
        if not entities:
            return filters
        
        # Year → Document.date (extract year)
        if "year" in entities:
            filters.append(
                extract('year', Document.date) == entities["year"]
            )
        
        # Creator → Document.creator OR Document.contributor
        if "creator" in entities:
            creator_val = f"%{entities['creator']}%"
            filters.append(
                or_(
                    Document.creator.ilike(creator_val),
                    Document.contributor.ilike(creator_val)
                )
            )
        
        # Language → Document.language
        if "language" in entities:
            filters.append(
                Document.language.ilike(f"%{entities['language']}%")
            )
        
        # Publisher → Document.publisher
        if "publisher" in entities:
            filters.append(
                Document.publisher.ilike(f"%{entities['publisher']}%")
            )
        
        # Location → Document.coverage
        if "location" in entities:
            filters.append(
                Document.coverage.ilike(f"%{entities['location']}%")
            )
        
        # Source/Journal → Document.source
        if "source" in entities:
            filters.append(
                Document.source.ilike(f"%{entities['source']}%")
            )
        
        # DOI → Document.doi
        if "doi" in entities:
            filters.append(
                Document.doi == entities["doi"]
            )
        
        # Document type → Document.type
        if "doc_type" in entities:
            filters.append(
                Document.type == entities["doc_type"]
            )
        
        print(f"  Metadata filters: {len(filters)} applied")
        return filters

    # =========================================================================
    # Hybrid Search (Semantic + Question Embedding)
    # =========================================================================

    def _calculate_keyword_score(self, content: str, doc: 'Document', keywords: List[str]) -> float:
        """
        Calculate keyword matching score (0.0 to 1.0) using all Dublin Core metadata.
        Searches in: title, creator, keywords, description, publisher, contributor, 
                     date, abstract, language, relation
        """
        if not keywords:
            return 0.0
        
        content_lower = content.lower()
        
        # Convert date to string for matching
        date_str = str(doc.date) if doc.date else ""
        
        # All Dublin Core metadata fields with weights
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
            
            for field_name, (field_value, weight) in metadata_fields.items():
                if keyword in field_value:
                    total_score += weight
                    keyword_matched = True
                    break
            
            if not keyword_matched and keyword in content_lower:
                total_score += 0.5
            
            max_possible += 3
        
        return min(total_score / max_possible, 1.0) if max_possible > 0 else 0.0

    async def _expand_query(self, query: str) -> List[str]:
        """
        Generate query variations to improve retrieval recall.
        Returns original query + Indonesian and English variations.
        """
        prompt = f"""Buat 2 variasi berbeda dari pertanyaan berikut untuk meningkatkan pencarian dokumen akademik.
WAJIB menghasilkan tepat dua baris:
Bahasa Indonesia: <parafrasa pertanyaan dalam Bahasa Indonesia>
English: <translation or equivalent search query in English>
Jangan menambahkan nomor, markdown, JSON, atau penjelasan tambahan.
Pertanyaan asli: {query}"""
        try:
            result = await generate_response(prompt)
            variations = self._parse_bilingual_query_expansion(query, result)
            all_queries = [query] + variations
            print(f"  Query expansion: {len(all_queries)} queries total")
            for i, q in enumerate(all_queries):
                print(f"    [{i}] {q[:80]}")
            return all_queries
        except Exception as e:
            print(f"  Query expansion failed: {e}, using bilingual fallback")
            return [query] + self._build_bilingual_query_fallback(query)

    def _parse_bilingual_query_expansion(self, query: str, response_text: str) -> List[str]:
        """Parse LLM output into Indonesian and English query variations."""
        lines = [line.strip() for line in (response_text or "").strip().split('\n') if line.strip()]
        indonesian_query = None
        english_query = None
        unlabeled_lines = []

        for line in lines:
            normalized = re.sub(r'^\s*[-*\d.)]+\s*', '', line).strip()
            label_match = re.match(
                r'^(bahasa\s+indonesia|indonesia|indonesian|id|english|inggris|en)\s*[:\-]\s*(.+)$',
                normalized,
                flags=re.IGNORECASE,
            )
            if label_match:
                label = label_match.group(1).lower()
                value = label_match.group(2).strip()
                if not value:
                    continue
                if label in {"bahasa indonesia", "indonesia", "indonesian", "id"}:
                    indonesian_query = value
                else:
                    english_query = value
                continue

            if len(normalized) > 5:
                unlabeled_lines.append(normalized)

        if indonesian_query is None and unlabeled_lines:
            indonesian_query = unlabeled_lines.pop(0)
        if english_query is None and unlabeled_lines:
            english_query = unlabeled_lines.pop(0)

        fallback_indonesian, fallback_english = self._build_bilingual_query_fallback(query)
        indonesian_query = indonesian_query or fallback_indonesian
        english_query = english_query or fallback_english

        variations = []
        for value in (indonesian_query, english_query):
            if value and value.lower() != query.lower() and value not in variations:
                variations.append(value)
            elif value and value not in variations:
                variations.append(value)

        return variations

    def _build_bilingual_query_fallback(self, query: str) -> List[str]:
        """Return safe Indonesian and English slots when expansion parsing fails."""
        return [query, f"English query: {query}"]

    def _retrieve_relevant_chunks(
        self,
        query: str,
        metadata_filters: List = None,
        limit: int = 8,
        threshold: float = 0.35,
        query_embeddings: Optional[List] = None,
    ) -> Tuple[List[DocumentChunk], List[float]]:
        """Retrieve relevant chunks using hybrid search without LLM reranking."""
        candidates = self._retrieve_relevant_chunk_candidates(
            query=query,
            metadata_filters=metadata_filters,
            limit=limit,
            query_embeddings=query_embeddings,
        )

        selected = self._select_ranked_candidates(candidates, limit=limit, threshold=threshold)
        return self._candidate_dicts_to_chunks(selected)

    def _retrieve_relevant_chunk_candidates(
        self,
        query: str,
        metadata_filters: List = None,
        limit: int = 8,
        query_embeddings: Optional[List] = None,
    ) -> List[Dict[str, Any]]:
        """Build a larger candidate pool from content and question embeddings."""
        MIN_CONTENT_LENGTH = 100
        candidate_limit = limit * 10
        has_metadata_filters = bool(metadata_filters and len(metadata_filters) > 0)

        embeddings_to_search = query_embeddings or []
        if not embeddings_to_search:
            primary_emb = generate_embedding(query)
            if primary_emb is None:
                print("Warning: Failed to generate query embedding")
                return []
            embeddings_to_search = [primary_emb]

        print(f"  Multi-query retrieval: searching with {len(embeddings_to_search)} embedding(s)")

        best_scores: Dict[int, Dict] = {}

        for emb_idx, query_embedding in enumerate(embeddings_to_search):
            content_rows = self._fetch_similarity_candidates(
                query_embedding=query_embedding,
                metadata_filters=metadata_filters,
                candidate_limit=candidate_limit,
                min_content_length=MIN_CONTENT_LENGTH,
                retrieval_source="content",
                has_metadata_filters=has_metadata_filters,
            )
            question_rows = self._fetch_similarity_candidates(
                query_embedding=query_embedding,
                metadata_filters=metadata_filters,
                candidate_limit=candidate_limit,
                min_content_length=MIN_CONTENT_LENGTH,
                retrieval_source="question",
                has_metadata_filters=has_metadata_filters,
            )

            print(
                f"  [emb#{emb_idx}] Candidate rows: "
                f"content={len(content_rows)}, question={len(question_rows)}"
            )

            candidate_rows = [
                self._build_candidate_score(row, "content")
                for row in content_rows
            ]
            candidate_rows.extend(
                self._build_candidate_score(row, "question")
                for row in question_rows
            )
            before_filter_count = len(candidate_rows)
            candidate_rows = [
                candidate
                for candidate in candidate_rows
                if not self._is_noisy_visual_or_table_summary(candidate)
            ]
            removed_count = before_filter_count - len(candidate_rows)
            if removed_count:
                print(f"  [emb#{emb_idx}] Removed {removed_count} noisy table/image candidates")

            best_scores = self._merge_candidate_scores(best_scores, candidate_rows)

        scored_chunks = sorted(best_scores.values(), key=lambda x: x['hybrid_score'], reverse=True)

        for item in scored_chunks[:20]:  # log top 20 for debugging
            print(
                f"  Chunk {item['chunk'].id}: "
                f"content_sim={item['semantic_score']:.4f}, "
                f"q_sim={item['question_score']:.4f}, "
                f"hybrid={item['hybrid_score']:.4f}"
            )

        return scored_chunks

    def _fetch_similarity_candidates(
        self,
        query_embedding,
        metadata_filters: List,
        candidate_limit: int,
        min_content_length: int,
        retrieval_source: str,
        has_metadata_filters: bool,
    ):
        content_sim = (1 - DocumentChunk.embedding.cosine_distance(query_embedding)).label("semantic_score")
        question_sim = case(
            (
                DocumentChunk.possibly_question_embedding.isnot(None),
                1 - DocumentChunk.possibly_question_embedding.cosine_distance(query_embedding),
            ),
            else_=literal(0.0),
        ).label("question_score")

        base_query = self.db.query(
            DocumentChunk,
            Document,
            content_sim,
            question_sim,
        ).join(
            Document, DocumentChunk.document_id == Document.id
        ).filter(
            Document.title.isnot(None),
            Document.title != "",
            Document.title != "Untitled Document",
            ~Document.title.ilike("untitled%"),
            DocumentChunk.content.isnot(None),
            DocumentChunk.content != "",
            func.length(DocumentChunk.content) >= min_content_length,
        )

        if retrieval_source == "question":
            base_query = base_query.filter(DocumentChunk.possibly_question_embedding.isnot(None))
            order_expr = question_sim
        else:
            base_query = base_query.filter(DocumentChunk.embedding.isnot(None))
            order_expr = content_sim

        if has_metadata_filters:
            filtered_query = base_query.filter(*metadata_filters)
            rows = filtered_query.order_by(desc(order_expr)).limit(candidate_limit).all()
            if len(rows) >= 2:
                return rows
            print(f"  [{retrieval_source}] Too few metadata-filtered results, fallback to unfiltered")

        return base_query.order_by(desc(order_expr)).limit(candidate_limit).all()

    def _build_candidate_score(
        self,
        row,
        retrieval_source: str,
    ) -> Dict[str, Any]:
        chunk, doc, semantic_score, question_score = row
        sem_score = float(semantic_score) if semantic_score is not None else 0.0
        q_score = float(question_score) if question_score is not None else 0.0
        combined_semantic = max(sem_score, q_score)

        return {
            "chunk": chunk,
            "chunk_id": chunk.id,
            "document_id": doc.id,
            "document_title": doc.title,
            "section_title": chunk.section_title,
            "page_number": chunk.page_number,
            "chunk_type": self._chunk_type_value(chunk),
            "content": chunk.content,
            "semantic_score": sem_score,
            "question_score": q_score,
            "combined_semantic": combined_semantic,
            "keyword_score": 0.0,
            "hybrid_score": combined_semantic,
            "retrieval_source": retrieval_source,
        }

    def _merge_candidate_scores(
        self,
        existing: Dict[int, Dict[str, Any]],
        rows: List[Dict[str, Any]],
    ) -> Dict[int, Dict[str, Any]]:
        """Merge content/question candidate rows by chunk id, keeping best score."""
        return retrieval.merge_candidate_scores(existing, rows)

    def _select_ranked_candidates(
        self,
        candidates: List[Dict[str, Any]],
        limit: int = 8,
        threshold: float = 0.35,
    ) -> List[Dict[str, Any]]:
        MAX_CHUNKS_PER_DOCUMENT = 10
        selected: List[Dict[str, Any]] = []
        doc_chunk_count: Dict[int, int] = {}

        for item in sorted(candidates, key=lambda x: x["hybrid_score"], reverse=True):
            if item['hybrid_score'] < threshold:
                break

            doc_id = item['document_id']
            if doc_chunk_count.get(doc_id, 0) >= MAX_CHUNKS_PER_DOCUMENT:
                continue

            selected.append(item)
            doc_chunk_count[doc_id] = doc_chunk_count.get(doc_id, 0) + 1

            if len(selected) >= limit:
                break

        print(f"  Final retrieved: {len(selected)} chunks (threshold={threshold}, limit={limit})")
        return selected

    def _candidate_dicts_to_chunks(
        self,
        candidates: List[Dict[str, Any]],
    ) -> Tuple[List[DocumentChunk], List[float]]:
        return retrieval.candidate_dicts_to_chunks(candidates)

    async def _retrieve_and_rerank_chunks(
        self,
        query: str,
        metadata_filters: List = None,
        limit: int = 8,
        threshold: float = 0.35,
        query_embeddings: Optional[List] = None,
    ) -> Tuple[List[DocumentChunk], List[float]]:
        candidates = self._retrieve_relevant_chunk_candidates(
            query=query,
            metadata_filters=metadata_filters,
            limit=limit,
            query_embeddings=query_embeddings,
        )
        selected_candidates = self._select_ranked_candidates(
            candidates,
            limit=limit * 4,
            threshold=threshold,
        )
        reranked_candidates = await rerank_chunks(query, selected_candidates, limit=limit)
        return self._candidate_dicts_to_chunks(reranked_candidates)

    # =========================================================================
    # Context & Prompt Construction
    # =========================================================================

    def _construct_context_text(self, chunks: List[DocumentChunk]) -> str:
        """Format chunks into a context string."""
        return rag_prompt.construct_context_text(self.db, chunks)

    def _construct_rag_prompt(self, message: str, context_text: str) -> str:
        """Construct the prompt for the LLM."""
        return rag_prompt.construct_rag_prompt(message, context_text)

    # =========================================================================
    # References
    # =========================================================================

    def _save_rag_references(self, bot_chat_id: int, chunks: List[DocumentChunk], similarities: List[float]):
        """Save references for the RAG response."""
        for i, chunk in enumerate(chunks):
            reference = ChatReference(
                chat_id=bot_chat_id,
                document_id=chunk.document_id,
                chunk_id=chunk.id,
                relevance_score=float(similarities[i]),
                quote=chunk.content[:200],
                page_number=chunk.page_number
            )
            self.db.add(reference)
        self.db.commit()

    def _serialize_chat_references(self, chat_id: int) -> List[Dict[str, Any]]:
        references = self.db.query(ChatReference).filter(ChatReference.chat_id == chat_id).all()
        return [
            {
                "id": reference.id,
                "document_id": reference.document_id,
                "quote": reference.quote,
                "page_number": reference.page_number,
                "document_title": reference.document_title,
            }
            for reference in references
        ]

    # =========================================================================
    # Main Chat Processing
    # =========================================================================

    async def process_chat(self, user_id: int, request: ChatRequest) -> ChatResponse:
        total_started_at = time.perf_counter()
        # 1. Handle Conversation
        started_at = time.perf_counter()
        conversation = self._handle_conversation(user_id, request)
        self._print_timing("ChatService._handle_conversation", time.perf_counter() - started_at)

        # 2. Save User Message
        started_at = time.perf_counter()
        self._save_chat_message(conversation.id, ChatRole.USER, request.message)
        self._print_timing("ChatService._save_chat_message[user]", time.perf_counter() - started_at)

        # 3. Query Processing: clean + extract entities
        started_at = time.perf_counter()
        query_info = self._process_query(request.message)
        self._print_timing("ChatService._process_query", time.perf_counter() - started_at)
        print("========== QUERY INFO ==========")
        print(query_info)
        print("============================================")

        # 4. Build metadata filters from extracted entities
        started_at = time.perf_counter()
        metadata_filters = self._build_metadata_filters(query_info["entities"])
        self._print_timing("ChatService._build_metadata_filters", time.perf_counter() - started_at)
        print("========== METADATA FILTERS ==========")
        print(metadata_filters)
        print("============================================")

        # 5. Query Expansion — generate bilingual variations
        print("========== QUERY EXPANSION ==========")
        expansion_started_at = time.perf_counter()
        expanded_queries = await self._expand_query(query_info["cleaned_query"])
        self._print_timing("ChatService._expand_query", time.perf_counter() - expansion_started_at)
        query_embeddings = []
        embedding_batch_started_at = time.perf_counter()
        for q in expanded_queries:
            emb = generate_embedding(q)
            if emb is not None:
                query_embeddings.append(emb)
        self._print_timing("ChatService.generate_query_embeddings", time.perf_counter() - embedding_batch_started_at)
        print(f"  Generated {len(query_embeddings)} valid embeddings from {len(expanded_queries)} queries")
        print("============================================")

        # 6. RAG: Retrieve Context (multi-query + metadata filtering)
        retrieval_started_at = time.perf_counter()
        chunks, similarities = await self._retrieve_and_rerank_chunks(
            query=query_info["cleaned_query"],
            metadata_filters=metadata_filters,
            query_embeddings=query_embeddings,
        )
        self._print_timing("ChatService._retrieve_and_rerank_chunks", time.perf_counter() - retrieval_started_at)
        print("========== SIMILARITIES ==========")
        print(similarities)
        print("============================================")
        
        context_started_at = time.perf_counter()
        context_text = self._construct_context_text(chunks)
        self._print_timing("ChatService._construct_context_text", time.perf_counter() - context_started_at)
        
        # 6. Construct Prompt
        prompt_started_at = time.perf_counter()
        full_prompt = self._construct_rag_prompt(request.message, context_text)
        self._print_timing("ChatService._construct_rag_prompt", time.perf_counter() - prompt_started_at)
        print("========== FULL PROMPT ==========")
        print(full_prompt[:2000])
        print("============================================")
        # 7. Generate Response
        generation_started_at = time.perf_counter()
        answer = await generate_response(full_prompt)
        self._print_timing("ChatService.generate_response", time.perf_counter() - generation_started_at)

        # Print RAGAS evaluation data
        retrieved_docs = [chunk.content for chunk in chunks]
        ragas_data = {
            "query": [request.message],
            "generated_response": [answer],
            "retrieved_documents": [retrieved_docs]
        }
        print("========== RAGAS EVALUATION DATA ==========")
        print(ragas_data)
        print("============================================")

        # 8. Save Bot Message
        started_at = time.perf_counter()
        bot_chat = self._save_chat_message(conversation.id, ChatRole.BOT, answer)
        self._print_timing("ChatService._save_chat_message[bot]", time.perf_counter() - started_at)

        # 9. Save References
        started_at = time.perf_counter()
        self._save_rag_references(bot_chat.id, chunks, similarities)
        self._print_timing("ChatService._save_rag_references", time.perf_counter() - started_at)
        self._print_timing("ChatService.process_chat.total", time.perf_counter() - total_started_at)

        return ChatResponse(
            id=bot_chat.id,
            conversation_id=conversation.id,
            role=bot_chat.role,
            message=bot_chat.message,
            created_at=bot_chat.created_at,
            references=[]
        )

    async def process_chat_stream(
        self, user_id: int, request: ChatRequest
    ) -> AsyncGenerator[Dict[str, Any], None]:
        total_started_at = time.perf_counter()
        # 1. Handle Conversation
        started_at = time.perf_counter()
        conversation = self._handle_conversation(user_id, request)
        self._print_timing("ChatService._handle_conversation[stream]", time.perf_counter() - started_at)

        # 2. Save User Message
        started_at = time.perf_counter()
        self._save_chat_message(conversation.id, ChatRole.USER, request.message)
        self._print_timing("ChatService._save_chat_message[user][stream]", time.perf_counter() - started_at)
        yield {"type": "start", "conversation_id": conversation.id}

        # 3. Query Processing: clean + extract entities
        started_at = time.perf_counter()
        query_info = self._process_query(request.message)
        self._print_timing("ChatService._process_query[stream]", time.perf_counter() - started_at)
        print("========== QUERY INFO ==========")
        print(query_info)
        print("============================================")

        # 4. Build metadata filters from extracted entities
        started_at = time.perf_counter()
        metadata_filters = self._build_metadata_filters(query_info["entities"])
        self._print_timing("ChatService._build_metadata_filters[stream]", time.perf_counter() - started_at)
        print("========== METADATA FILTERS ==========")
        print(metadata_filters)
        print("============================================")

        # 5. Query Expansion — generate bilingual variations
        print("========== QUERY EXPANSION ==========")
        expansion_started_at = time.perf_counter()
        expanded_queries = await self._expand_query(query_info["cleaned_query"])
        self._print_timing("ChatService._expand_query[stream]", time.perf_counter() - expansion_started_at)
        query_embeddings = []
        embedding_batch_started_at = time.perf_counter()
        for q in expanded_queries:
            emb = generate_embedding(q)
            if emb is not None:
                query_embeddings.append(emb)
        self._print_timing(
            "ChatService.generate_query_embeddings[stream]",
            time.perf_counter() - embedding_batch_started_at,
        )
        print(f"  Generated {len(query_embeddings)} valid embeddings from {len(expanded_queries)} queries")
        print("============================================")

        # 6. RAG: Retrieve Context (multi-query + metadata filtering)
        retrieval_started_at = time.perf_counter()
        chunks, similarities = await self._retrieve_and_rerank_chunks(
            query=query_info["cleaned_query"],
            metadata_filters=metadata_filters,
            query_embeddings=query_embeddings,
        )
        self._print_timing(
            "ChatService._retrieve_and_rerank_chunks[stream]",
            time.perf_counter() - retrieval_started_at,
        )
        print("========== SIMILARITIES ==========")
        print(similarities)
        print("============================================")

        context_started_at = time.perf_counter()
        context_text = self._construct_context_text(chunks)
        self._print_timing("ChatService._construct_context_text[stream]", time.perf_counter() - context_started_at)

        # 6. Construct Prompt
        prompt_started_at = time.perf_counter()
        full_prompt = self._construct_rag_prompt(request.message, context_text)
        self._print_timing("ChatService._construct_rag_prompt[stream]", time.perf_counter() - prompt_started_at)
        print("========== FULL PROMPT ==========")
        print(full_prompt[:2000])
        print("============================================")

        # 7. Generate Streaming Response
        answer_chunks: List[str] = []
        generation_started_at = time.perf_counter()
        async for chunk in generate_response_stream(full_prompt):
            answer_chunks.append(chunk)
            yield {"type": "chunk", "content": chunk}
        self._print_timing("ChatService.generate_response_stream", time.perf_counter() - generation_started_at)

        answer = "".join(answer_chunks).strip()
        if not answer:
            answer = "Maaf, saya belum dapat menghasilkan jawaban."

        # Print RAGAS evaluation data
        retrieved_docs = [chunk.content for chunk in chunks]
        ragas_data = {
            "query": [request.message],
            "generated_response": [answer],
            "retrieved_documents": [retrieved_docs],
        }
        print("========== RAGAS EVALUATION DATA ==========")
        print(ragas_data)
        print("============================================")

        # 8. Save Bot Message
        started_at = time.perf_counter()
        bot_chat = self._save_chat_message(conversation.id, ChatRole.BOT, answer)
        self._print_timing("ChatService._save_chat_message[bot][stream]", time.perf_counter() - started_at)

        # 9. Save References
        started_at = time.perf_counter()
        self._save_rag_references(bot_chat.id, chunks, similarities)
        references_payload = self._serialize_chat_references(bot_chat.id)
        self._print_timing("ChatService._save_rag_references[stream]", time.perf_counter() - started_at)
        self._print_timing("ChatService.process_chat_stream.total", time.perf_counter() - total_started_at)

        yield {
            "type": "done",
            "chat": {
                "id": bot_chat.id,
                "conversation_id": conversation.id,
                "role": bot_chat.role.value,
                "message": bot_chat.message,
                "created_at": bot_chat.created_at.isoformat() if bot_chat.created_at else None,
                "references": references_payload,
            },
        }
