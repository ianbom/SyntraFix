"""Reference generation helpers for prompt search experiments."""
from typing import List

from app.services.llm import generate_response


async def generate_reference_from_context(
    question: str,
    answer: str,
    contexts: List[str],
) -> str:
    """Generate a RAGAS reference using only retrieved contexts."""
    clean_contexts = [context.strip() for context in contexts if context and context.strip()]
    if not clean_contexts:
        return "Retrieved context kosong, sehingga informasi tidak ditemukan pada dokumen yang tersedia."

    joined_contexts = "\n\n---\n\n".join(clean_contexts)
    prompt = f"""Anda adalah evaluator RAGAS.

Buat reference/ground truth ideal untuk pertanyaan user.
ATURAN WAJIB:
1. Gunakan HANYA informasi dari RETRIEVED_CONTEXT.
2. Jangan memakai pengetahuan luar.
3. Jangan menambahkan fakta yang tidak ada di RETRIEVED_CONTEXT.
4. Jika RETRIEVED_CONTEXT tidak cukup untuk menjawab, tulis bahwa informasi tidak ditemukan pada retrieved context.
5. Jawab ringkas dalam Bahasa Indonesia.

PERTANYAAN:
{question}

JAWABAN MODEL:
{answer}

RETRIEVED_CONTEXT:
{joined_contexts}

REFERENCE:"""
    reference = (await generate_response(prompt)).strip()
    return reference or "Informasi tidak ditemukan pada retrieved context."

