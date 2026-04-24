"""API routes for document management."""
from typing import Optional, List
from fastapi import APIRouter, Depends, File, UploadFile, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.document import Document, DocumentType
from app.models.document_chunk import DocumentChunk
from app.schemas.document import (
    DocumentResponse,
    DocumentListItem,
    DocumentListResponse,
    DocumentDetailResponse,
    DocumentUpdate,
    DocumentTypeEnum,
    ProcessingMonitorItem,
    ProcessingMonitorResponse,
    ProcessingMonitorSummary,
)
from app.services.document_responses import (
    PROCESS_MONITOR_STATUSES,
    build_document_response,
    normalize_processing_progress,
    normalize_processing_status,
)
from app.services.document import (
    get_document_download_url,
    get_document_detail_data,
    delete_document_file,
    FileValidator,
    MinIOStorage
)
from app.websockets import manager
from fastapi import WebSocket
from app.services.grobid import extract_header, extract_fulltext, extract_references
from app.tasks.document_tasks import generate_possibly_questions_task, process_document_task

router = APIRouter(prefix="/documents", tags=["Documents"])


def _get_possibly_question_counts(db: Session, document_id: int) -> dict:
    """Count eligible chunks and generated possibly question coverage."""
    eligible_chunks = (
        db.query(DocumentChunk)
        .filter(
            DocumentChunk.document_id == document_id,
            DocumentChunk.content.isnot(None),
            DocumentChunk.content != "",
            DocumentChunk.token_count >= 30,
        )
        .all()
    )
    chunk_count = len(eligible_chunks)
    possibly_question_count = sum(
        1
        for chunk in eligible_chunks
        if bool(chunk.possibly_questions) and chunk.possibly_question_embedding is not None
    )
    missing_count = max(0, chunk_count - possibly_question_count)
    progress = 100 if chunk_count == 0 else int((possibly_question_count / chunk_count) * 100)

    return {
        "chunk_count": chunk_count,
        "possibly_question_count": possibly_question_count,
        "possibly_question_missing_count": missing_count,
        "possibly_question_progress": progress,
    }


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            await websocket.receive_text()
    except Exception:
        manager.disconnect(client_id)


@router.post("/upload", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    type: DocumentTypeEnum = Query(default=DocumentTypeEnum.JOURNAL),
    is_private: bool = Query(default=False),
    client_id: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Upload and process a PDF document.
    
    The document will be:
    1. Validated and stored in MinIO (instant)
    2. Processed in background by Celery pipeline:
       - GROBID metadata + structure extraction
       - PyMuPDF text/table/image extraction
       - Smart chunking + content embeddings
    
    Returns immediately with processing_status='processing'.
    Use GET /documents/{id}/status to poll for completion.
    """
    # Step 1: Validate file
    FileValidator.validate_pdf(file)
    file_content = await file.read()
    FileValidator.validate_size(file_content)
    
    # Step 2: Upload to MinIO (fast)
    storage = MinIOStorage()
    file_path = storage.upload_file(file_content, file.filename)
    
    # Step 3: Create document record with status="processing"
    doc_type = DocumentType(type.value)
    document = Document(
        title="Sedang diproses...",
        file_path=file_path,
        type=doc_type,
        is_private=is_private,
        format="application/pdf",
        processing_status="processing",
        processing_progress=0,
    )
    db.add(document)
    db.commit()
    db.refresh(document)
    
    # Step 4: Send processing task to Celery (non-blocking)
    process_document_task.delay(document.id, file_path)
    print(f"Celery task dispatched for document {document.id}")
    
    # Notify via WebSocket
    if client_id:
        await manager.send_personal_message(
            {
                "status": "processing",
                "progress": normalize_processing_progress(
                    document.processing_progress,
                    document.processing_status,
                ),
                "message": "Document uploaded, pipeline processing started...",
                "document_id": document.id,
            },
            client_id
        )
    
    return build_document_response(document, 0)


@router.get("/{document_id}/status")
async def get_document_status(
    document_id: int,
    db: Session = Depends(get_db)
):
    """
    Get the processing status of a document.
    Used by frontend to poll for completion after upload.
    """
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    question_counts = _get_possibly_question_counts(db, document.id)
    
    return {
        "id": document.id,
        "title": document.title,
        "processing_status": normalize_processing_status(document.processing_status),
        "processing_progress": normalize_processing_progress(
            document.processing_progress,
            document.processing_status,
        ),
        "processing_error": document.processing_error,
        **question_counts,
        "is_metadata_complete": document.is_metadata_complete or False
    }


@router.post("/{document_id}/possibly-questions/generate")
async def generate_document_possibly_questions(
    document_id: int,
    db: Session = Depends(get_db),
):
    """Queue background generation of possibly questions for one document."""
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    question_counts = _get_possibly_question_counts(db, document.id)
    if question_counts["chunk_count"] == 0:
        raise HTTPException(status_code=400, detail="Document has no eligible chunks")

    task = generate_possibly_questions_task.delay(document.id)

    return {
        "document_id": document.id,
        "task_id": task.id,
        "status": "queued",
        "chunk_count": question_counts["chunk_count"],
        "possibly_question_count": question_counts["possibly_question_count"],
        "missing_possibly_question_count": question_counts["possibly_question_missing_count"],
    }


@router.get("/processing-monitor", response_model=ProcessingMonitorResponse)
async def list_processing_monitor_documents(
    db: Session = Depends(get_db)
):
    """List documents for process monitoring (processing/completed/failed)."""
    documents = (
        db.query(Document)
        .filter(Document.processing_status.in_(PROCESS_MONITOR_STATUSES))
        .order_by(Document.created_at.desc())
        .all()
    )

    summary = {
        "processing": 0,
        "completed": 0,
        "failed": 0,
    }

    monitor_documents = []
    for document in documents:
        normalized_status = normalize_processing_status(document.processing_status)
        summary[normalized_status] += 1
        question_counts = _get_possibly_question_counts(db, document.id)

        monitor_documents.append(
            ProcessingMonitorItem(
                id=document.id,
                title=document.title,
                creator=document.creator,
                uploaded_at=document.created_at,
                processing_status=normalized_status,
                processing_progress=normalize_processing_progress(
                    document.processing_progress,
                    normalized_status,
                ),
                processing_error=document.processing_error,
                **question_counts,
            )
        )

    return ProcessingMonitorResponse(
        documents=monitor_documents,
        summary=ProcessingMonitorSummary(
            total=len(monitor_documents),
            processing=summary["processing"],
            completed=summary["completed"],
            failed=summary["failed"],
        ),
    )


@router.get("/", response_model=DocumentListResponse)
async def list_documents(
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1, le=100),
    type: Optional[DocumentTypeEnum] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    List all documents with pagination.
    Optionally filter by type or search in title/creator.
    """
    query = db.query(Document)
    
    # Apply filters
    if type:
        query = query.filter(Document.type == DocumentType(type.value))
    
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            (Document.title.ilike(search_term)) |
            (Document.creator.ilike(search_term)) |
            (Document.keywords.ilike(search_term))
        )
    
    # Get total count
    total = query.count()
    
    # Paginate
    offset = (page - 1) * per_page
    documents = query.order_by(Document.created_at.desc()).offset(offset).limit(per_page).all()
    
    # Calculate total pages
    pages = (total + per_page - 1) // per_page if total > 0 else 1
    
    return DocumentListResponse(
        documents=[
            DocumentListItem(
                id=doc.id,
                title=doc.title,
                creator=doc.creator,
                publication_date=doc.date,
                type=DocumentTypeEnum(doc.type.value),
                doi=doc.doi,
                is_private=doc.is_private,
                created_at=doc.created_at
            )
            for doc in documents
        ],
        total=total,
        page=page,
        per_page=per_page,
        pages=pages
    )


@router.get("/{document_id}", response_model=DocumentDetailResponse)
async def get_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    """Get complete detail data from documents + document_chunks tables."""
    return get_document_detail_data(db, document_id)


@router.get("/{document_id}/detail", response_model=DocumentDetailResponse)
async def get_document_detail(
    document_id: int,
    db: Session = Depends(get_db)
):
    """Get complete detail data from documents + document_chunks tables."""
    return get_document_detail_data(db, document_id)


@router.patch("/{document_id}", response_model=DocumentResponse)
async def update_document(
    document_id: int,
    update_data: DocumentUpdate,
    db: Session = Depends(get_db)
):
    """Update document metadata."""
    document = db.query(Document).filter(Document.id == document_id).first()
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    # Update fields
    update_dict = update_data.model_dump(exclude_unset=True)
    for field, value in update_dict.items():
        if field == "type" and value:
            setattr(document, field, DocumentType(value.value))
        else:
            setattr(document, field, value)
    
    db.commit()
    db.refresh(document)
    
    chunk_count = db.query(func.count(DocumentChunk.id)).filter(
        DocumentChunk.document_id == document.id
    ).scalar() or 0
    
    return build_document_response(document, chunk_count)


@router.delete("/{document_id}")
async def delete_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    """Delete a document and its chunks."""
    document = db.query(Document).filter(Document.id == document_id).first()
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    # Delete file from MinIO
    if document.file_path:
        delete_document_file(document.file_path)
    
    # Delete from database (chunks will cascade)
    db.delete(document)
    db.commit()
    
    return {"message": "Document deleted successfully", "id": document_id}


@router.get("/{document_id}/download")
async def download_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    """Get download URL for a document."""
    document = db.query(Document).filter(Document.id == document_id).first()
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    if not document.file_path:
        raise HTTPException(status_code=404, detail="Document file not found")
    
    download_url = get_document_download_url(document.file_path)
    
    return {
        "download_url": download_url,
        "filename": f"{document.title}.pdf"
    }



@router.post("/upload-bulk")
async def upload_documents_bulk(
    files: List[UploadFile] = File(...),
    type: DocumentTypeEnum = Query(default=DocumentTypeEnum.JOURNAL),
    is_private: bool = Query(default=False),
    client_id: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Upload and process multiple PDF documents at once.
    
    Each document will be:
    1. Validated and stored in MinIO (instant)
    2. Processed in background by Celery pipeline (GROBID + PyMuPDF + chunking/embedding)
    
    Returns immediately with document IDs and processing_status='processing'.
    Use GET /documents/{id}/status to poll for completion.
    """
    doc_type = DocumentType(type.value)
    storage = MinIOStorage()
    results = []
    total_files = len(files)
    
    for file in files:
        file_result = {
            "filename": file.filename,
            "status": "pending",
            "document_id": None,
            "error": None
        }
        
        try:
            # Validate
            FileValidator.validate_pdf(file)
            file_content = await file.read()
            FileValidator.validate_size(file_content)
            
            # Upload to MinIO
            file_path = storage.upload_file(file_content, file.filename)
            
            # Create document record
            document = Document(
                title=f"Sedang diproses... ({file.filename})",
                file_path=file_path,
                type=doc_type,
                is_private=is_private,
                format="application/pdf",
                processing_status="processing",
                processing_progress=0,
            )
            db.add(document)
            db.commit()
            db.refresh(document)
            
            # Dispatch Celery task
            process_document_task.delay(document.id, file_path)
            
            file_result["status"] = "processing"
            file_result["document_id"] = document.id
            
        except Exception as e:
            file_result["status"] = "error"
            file_result["error"] = str(e)
        
        results.append(file_result)
    
    if client_id:
        await manager.send_personal_message(
            {
                "status": "processing",
                "message": f"Uploaded {total_files} files, processing in background...",
                "total_files": total_files,
                "success_count": sum(1 for r in results if r["status"] == "processing"),
                "error_count": sum(1 for r in results if r["status"] == "error")
            },
            client_id
        )
    
    return {
        "total": total_files,
        "processing_count": sum(1 for r in results if r["status"] == "processing"),
        "error_count": sum(1 for r in results if r["status"] == "error"),
        "results": results
    }

@router.post("/test-grobid-header")
async def test_grobid_header(file: UploadFile = File(...)):
    file_bytes = await file.read()
    header = await extract_header(file_bytes)
    print(header)
    return {"header": header}

@router.post("/test-grobid-full")
async def test_grobid_full(file: UploadFile = File(...)):
    file_bytes = await file.read()
    fulltext = extract_fulltext(file_bytes)
    with open("grobid_fulltext_response.txt", "w", encoding="utf-8") as f:
        f.write("==grobid_fulltext_response \n")
        f.write(fulltext + "\n")
        f.write("=====================================\n")
    return { 
        "length": len(fulltext),
        "fulltext": fulltext}

@router.post("/test-grobid-references")
async def test_grobid_references(file: UploadFile = File(...)):
    file_bytes = await file.read()
    references = extract_references(file_bytes)
    print(references)
    return {"references": references}

@router.post("/test-pymupdf")
async def test_pymupdf(file: UploadFile = File(...)):
    file_bytes = await file.read()

    try:
        import pymupdf
    except ImportError:
        try:
            import fitz as pymupdf
        except ImportError:
            raise HTTPException(status_code=500, detail="PyMuPDF not installed")

    doc = pymupdf.open(stream=file_bytes, filetype="pdf")
    pages = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        if text and text.strip():
            pages.append({
                "page": page_num + 1,
                "text": text.strip()
            })
    doc.close()

    full_text = "\n\n".join([p["text"] for p in pages])
    print(f"PyMuPDF: {len(full_text)} chars from {len(pages)} pages")


    with open("pymupdf_response.txt", "w", encoding="utf-8") as f:
        f.write("==pymupdf_response \n")
        f.write(full_text + "\n")
        f.write("=====================================\n")

    return {
        "total_pages": len(pages),
        "total_chars": len(full_text),
        "full_text": full_text,
        "per_page": pages
    }
