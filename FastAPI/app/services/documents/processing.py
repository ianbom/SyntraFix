"""Document processing orchestration."""
from typing import Any, Callable, Dict, List, Optional

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.models.document import Document, DocumentType
from app.models.document_chunk import DocumentChunk
from app.services.documents.chunking import SmartChunker, TextChunker
from app.services.documents.extraction import extract_raw_pdf_text, validate_metadata
from app.services.documents.storage import MinIOStorage
from app.services.documents.validation import FileValidator
from app.services.embedding import generate_embedding
from app.services.grobid import (
    extract_fulltext,
    extract_header,
    extract_references,
    extract_structured_fulltext,
    format_for_database,
)
from app.services.metadata_extractor import (
    extract_metadata_with_llm,
    is_metadata_incomplete,
    merge_metadata,
)

class DocumentBuilder:
    """Builds Document model from metadata."""
    
    @staticmethod
    def build_from_metadata(
        metadata: Dict[str, Any],
        file_path: str,
        document_type: DocumentType,
        is_private: bool
    ) -> Document:
        """Create Document model from metadata dictionary."""
        return Document(
            title=metadata["title"],
            creator=metadata["creator"],
            keywords=metadata["keywords"],
            description=metadata["description"],
            publisher=metadata["publisher"],
            contributor=metadata["contributor"],
            date=metadata["date"],
            type=document_type,
            format=metadata["format"],
            identifier=metadata["identifier"],
            source=metadata["source"],
            language=metadata["language"],
            relation=metadata["relation"],
            coverage=metadata.get("coverage"),
            rights=metadata.get("rights"),
            doi=metadata["doi"],
            abstract=metadata["abstract"],
            citation_count=metadata["citation_count"],
            file_path=file_path,
            is_private=is_private,
            is_metadata_complete=bool(metadata["title"] and metadata["creator"])
        )


# =============================================================================
# Chunk Processor
# =============================================================================

class ChunkProcessor:
    """Processes chunks and creates embeddings."""
    
    def __init__(self, db: Session):
        self.db = db
    
    async def process_chunks(
        self, 
        document: Document, 
        chunks: List[Dict[str, Any]],
        progress_callback: Optional[Callable] = None
    ) -> None:
        """Generate embeddings, hypothetical questions, and save chunks to database."""
        total_chunks = len(chunks)
        
        for i, chunk_data in enumerate(chunks):
            # Progress update
            if progress_callback and i % 5 == 0:
                percent = 60 + int((i / total_chunks) * 30)
                await progress_callback(percent, f"Processing chunk {i+1}/{total_chunks} (embedding + questions)...")
            
            content = chunk_data["content"]
            
            # Generate content embedding
            embedding = generate_embedding(content)
            
            # Generate hypothetical questions from chunk content
            possibly_questions = None
            possibly_question_embedding = None
            try:
                section_title = chunk_data.get("section_title")
                doc_title = chunk_data.get("chunk_metadata", {}).get("source_document")
                # questions = await generate_possibly_questions(
                #     chunk_content=content,
                #     section_title=section_title,
                #     document_title=doc_title,
                # )
                # if questions:
                #     possibly_questions = questions
                #     # Combine questions into a single text and generate embedding
                #     combined_questions = " ".join(questions)
                #     possibly_question_embedding = generate_embedding(combined_questions)
            except Exception as e:
                print(f"  Warning: question generation failed for chunk {i}: {e}")
            
            # Create chunk record
            chunk = DocumentChunk(
                document_id=document.id,
                chunk_index=chunk_data["chunk_index"],
                content=content,
                token_count=chunk_data["token_count"],
                embedding=embedding,
                chunk_type=chunk_data["chunk_type"],
                page_number=chunk_data.get("page_number"),
                section_title=chunk_data.get("section_title"),
                chunk_metadata=chunk_data.get("chunk_metadata"),
                possibly_questions=possibly_questions,
                possibly_question_embedding=possibly_question_embedding,
            )
            self.db.add(chunk)


# =============================================================================
# Main Document Service
# =============================================================================

class DocumentService:
    """Main service for document processing."""
    
    def __init__(self, db: Session):
        self.db = db
        self.storage = MinIOStorage()
        self.chunker = TextChunker()           # Legacy fallback
        self.smart_chunker = SmartChunker()     # Primary: smart chunking
        self.chunk_processor = ChunkProcessor(db)
    
    async def process_document(
        self,
        file: UploadFile,
        document_type: DocumentType = DocumentType.JOURNAL,
        is_private: bool = False,
        progress_callback: Optional[Callable] = None
    ) -> Document:
        """
        Full document processing pipeline.
        
        Steps:
        1. Validate PDF
        2. Upload to MinIO
        3. Extract metadata via GROBID
        4. Create document record
        5. Create chunks with embeddings
        """
        # Step 1: Validate
        FileValidator.validate_pdf(file)
        file_content = await file.read()
        FileValidator.validate_size(file_content)
        
        # Step 2: Upload to storage
        if progress_callback:
            await progress_callback(10, "Uploading document to storage...")
        file_path = self.storage.upload_file(file_content, file.filename)
        
        try:
            # Step 3: Extract metadata
            if progress_callback:
                await progress_callback(30, "Extracting metadata with GROBID...")
            
            metadata = await self._extract_metadata(file_content, progress_callback)
            
            # Step 4: Create document record
            document = DocumentBuilder.build_from_metadata(
                metadata, file_path, document_type, is_private
            )
            self.db.add(document)
            self.db.flush()
            
            # Step 5: Process chunks
            if progress_callback:
                await progress_callback(60, "Processing content chunks...")
            
            chunks = self._prepare_chunks(metadata)
            await self.chunk_processor.process_chunks(document, chunks, progress_callback)
            
            # Commit and finish
            self.db.commit()
            self.db.refresh(document)
            
            if progress_callback:
                await progress_callback(100, "Document processing complete!")
            
            return document
            
        except HTTPException:
            raise
        except Exception as e:
            self.db.rollback()
            self.storage.delete_file(file_path)
            raise HTTPException(status_code=500, detail=f"Document processing failed: {str(e)}")
    
    async def _extract_metadata(self, file_content: bytes, progress_callback: Optional[Callable] = None) -> Dict[str, Any]:
        """Extract and format metadata from PDF using GROBID + LLM fallback."""
        # Step 1: Extract with GROBID
        header = await extract_header(file_content)
        references = extract_references(file_content)
        fulltext = extract_fulltext(file_content)
        
        # Step 1b: Extract structured sections for smart chunking
        structured_sections = []
        try:
            if progress_callback:
                await progress_callback(35, "Extracting document structure for smart chunking...")
            structured_sections = extract_structured_fulltext(file_content)
            print(f"Extracted {len(structured_sections)} structured sections for smart chunking")
        except Exception as e:
            print(f"Structured extraction failed, will use legacy chunking: {e}")
        
        metadata = format_for_database(header, references)
        metadata["fulltext"] = fulltext or ""
        metadata["structured_sections"] = structured_sections
        
        # Step 2: Extract raw PDF text for LLM (includes title page)
        raw_pdf_text = self._extract_raw_pdf_text(file_content)
        
        # Step 3: Check if metadata is incomplete and use LLM fallback
        if is_metadata_incomplete(metadata):
            print("Metadata incomplete from GROBID, using LLM fallback...")
            if progress_callback:
                await progress_callback(45, "Extracting metadata with LLM (GROBID incomplete)...")
            
            # Use raw PDF text for LLM (not GROBID fulltext) to ensure title page is included
            llm_input_text = raw_pdf_text if raw_pdf_text else (fulltext or "")
            # print('=============llm_input_text============')
            # print(llm_input_text)
            # print('====================================')
            # print('=============fulltext============')
            # print(fulltext)
            # print('=============raw_pdf_text============')
            # print(raw_pdf_text)
            try:
                llm_metadata = await extract_metadata_with_llm(llm_input_text, metadata)
                if llm_metadata:
                    metadata = merge_metadata(metadata, llm_metadata)
                    print("LLM metadata merge complete")
            except Exception as e:
                print(f"LLM metadata extraction failed: {str(e)}")
                # Continue with GROBID metadata only
        
        # Step 4: Final validation - ensure critical fields are never empty
        raw_text_for_fallback = raw_pdf_text if raw_pdf_text else (fulltext or "")
        metadata = self._validate_metadata(metadata, raw_text_for_fallback)
        
        return metadata
    
    def _extract_raw_pdf_text(self, file_content: bytes) -> str:
        """
        Extract raw text from PDF using PyMuPDF.
        Wrapper around the public extract_raw_pdf_text function.
        Also populates self._pages_data for page-number resolution.
        """
        raw_text, pages_data = extract_raw_pdf_text(file_content)
        self._pages_data = pages_data
        return raw_text
    
    def _validate_metadata(self, metadata: Dict[str, Any], fulltext: str) -> Dict[str, Any]:
        """Wrapper around the public validate_metadata function."""
        return validate_metadata(metadata, fulltext)
    
    def _prepare_chunks(self, metadata: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Prepare all chunks using smart chunking (paragraph/section-aware).
        Falls back to legacy fixed-size chunking if structured extraction failed.
        
        Smart chunking ensures:
        - Chunks respect paragraph and section boundaries
        - Short paragraphs are merged with the next one
        - Long paragraphs are split at sentence boundaries
        - ALL text from the document is preserved (no text loss)
        """
        structured_sections = metadata.get("structured_sections", [])
        
        if structured_sections:
            # === PRIMARY: Smart chunking from structured sections ===
            print("Using SMART CHUNKING (section & paragraph-aware)")
            pages_data = getattr(self, '_pages_data', None)
            chunks = self.smart_chunker.chunk_structured_sections(
                sections=structured_sections,
                document_title=metadata.get("title"),
                pages_data=pages_data,
            )
            
            if chunks:
                print(f"Smart chunking produced {len(chunks)} chunks")
                return chunks
            else:
                print("Smart chunking produced 0 chunks, falling back to legacy")
        
        # === FALLBACK: Legacy fixed-size chunking ===
        print("Using LEGACY CHUNKING (fixed word-count)")
        chunks = self.chunker.chunk_text(
            metadata.get("fulltext", ""),
            document_title=metadata["title"]
        )
        
        # Add abstract chunk
        if metadata.get("abstract"):
            abstract_chunk = TextChunker.create_abstract_chunk(
                metadata["abstract"],
                metadata["title"]
            )
            chunks.insert(0, abstract_chunk)
            TextChunker.reindex_chunks(chunks)
        
        # Add title chunk
        if metadata.get("title"):
            title_chunk = TextChunker.create_title_chunk(
                metadata["title"],
                metadata.get("creator"),
                metadata.get("doi")
            )
            chunks.insert(0, title_chunk)
            TextChunker.reindex_chunks(chunks)
        
        return chunks


async def process_document(
    file: UploadFile,
    db: Session,
    document_type: DocumentType = DocumentType.JOURNAL,
    is_private: bool = False,
    progress_callback: Optional[Callable] = None,
) -> Document:
    """Process document - wrapper for backward compatibility."""
    service = DocumentService(db)
    return await service.process_document(file, document_type, is_private, progress_callback)
