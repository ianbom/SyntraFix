"""RAG context and prompt formatting helpers."""
from typing import List

from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.document_chunk import DocumentChunk


def construct_context_text(db: Session, chunks: List[DocumentChunk]) -> str:
    """Format chunks into a context string."""
    context_parts = []
    for chunk in chunks:
        doc = db.query(Document).filter(Document.id == chunk.document_id).first()
        doc_title = doc.title if doc else "Unknown Document"

        context_parts.append(f"[Source: {doc_title}]\n{chunk.content}")

    return "\n\n---\n\n".join(context_parts) if context_parts else ""


def construct_rag_prompt(message: str, context_text: str) -> str:
    """Construct the prompt for the LLM."""
    if context_text:
        system_prompt = """Anda adalah asisten AI yang menjawab pertanyaan berdasarkan dokumen knowledge base.

INSTRUKSI:
1. Gunakan informasi dari KONTEKS di bawah untuk menjawab pertanyaan user.
2. Jawab dengan lengkap dan informatif menggunakan data yang ada di konteks.
3. Jika konteks membahas topik yang relevan, berikan jawaban terbaik berdasarkan informasi tersebut.
4. Sebutkan sumber dokumen ([Source: ...]) dalam jawaban Anda.
5. Gunakan bahasa yang sama dengan pertanyaan user.
6. Jika konteks benar-benar TIDAK MEMBAHAS topik pertanyaan sama sekali, katakan bahwa informasi tidak ditemukan."""

        return f"""{system_prompt}

KONTEKS DARI DOKUMEN:
{context_text}

---

PERTANYAAN USER: {message}

JAWABAN (berdasarkan konteks di atas):"""

    no_context_msg = "Maaf, saya tidak menemukan informasi yang relevan dengan pertanyaan Anda dalam dokumen yang tersedia."
    return f"""Anda adalah asisten AI berbasis dokumen knowledge base.

Tidak ditemukan dokumen yang relevan di knowledge base untuk pertanyaan ini.

PERTANYAAN USER: {message}

Jawab dengan: {no_context_msg}"""
