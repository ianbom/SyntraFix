from app.models.document_chunk import ChunkType


def test_document_service_facade_keeps_legacy_exports():
    from app.services import document

    assert document.FileValidator is not None
    assert document.MinIOStorage is not None
    assert document.TextChunker is not None
    assert document.SmartChunker is not None
    assert document.DocumentService is not None
    assert callable(document.process_document)
    assert callable(document.get_document_detail_data)
    assert callable(document.upload_pdf_to_minio)
    assert callable(document.chunk_text)


def test_document_internal_modules_expose_focused_responsibilities():
    from app.services.documents import chunking, detail, extraction, storage, validation

    assert validation.FileValidator is not None
    assert storage.MinIOStorage is not None
    assert chunking.TextChunker is not None
    assert chunking.SmartChunker is not None
    assert callable(extraction.extract_raw_pdf_text)
    assert callable(extraction.extract_pdf_tables_and_images)
    assert callable(detail.get_document_detail_data)


def test_embedding_text_service_matches_legacy_task_wrapper():
    from app.services.embedding_text import build_embedding_text as service_build_embedding_text
    from app.tasks.document_tasks import build_embedding_text as task_build_embedding_text

    base_chunk = {
        "content": "CNN digunakan untuk klasifikasi citra.",
        "chunk_type": ChunkType.PARAGRAPH,
        "page_number": 3,
        "section_title": "Metode",
        "chunk_metadata": {
            "source_document": "Pengembangan Deteksi Kanker",
            "section": "Metode",
        },
    }

    service_chunk = {
        **base_chunk,
        "chunk_metadata": dict(base_chunk["chunk_metadata"]),
    }
    task_chunk = {
        **base_chunk,
        "chunk_metadata": dict(base_chunk["chunk_metadata"]),
    }

    assert service_build_embedding_text(service_chunk) == task_build_embedding_text(task_chunk)
    assert service_chunk["chunk_metadata"]["embedding_text"] == task_chunk["chunk_metadata"]["embedding_text"]


def test_chat_helper_modules_are_available_for_chat_service():
    from app.services.chat import ChatService
    from app.services import chat_query, rag_prompt, retrieval

    service = ChatService(db=None)

    assert service._clean_query(" Apa itu CNN??? ") == chat_query.clean_query(" Apa itu CNN??? ")
    assert callable(rag_prompt.construct_rag_prompt)
    assert callable(retrieval.merge_candidate_scores)


def test_grobid_facade_keeps_public_exports():
    from app.services import grobid
    from app.services import grobid_client, grobid_parser

    assert callable(grobid.extract_header)
    assert callable(grobid.extract_fulltext)
    assert callable(grobid.extract_references)
    assert callable(grobid.extract_structured_fulltext)
    assert callable(grobid.format_for_database)
    assert callable(grobid_client.post_grobid)
    assert callable(grobid_parser.parse_header_xml)
