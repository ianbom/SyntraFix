"""Prompt generation and custom RAG prompt helpers."""
import json
import re
from typing import List

from app.services.llm import generate_response


DEFAULT_RAG_SYSTEM_PROMPT = """Anda adalah asisten AI berbasis dokumen.

ATURAN UTAMA:
1. Jawab HANYA menggunakan informasi yang tertulis di KONTEKS.
2. Jangan menambahkan fakta, angka, metode, hasil, definisi, atau kesimpulan yang tidak ada di KONTEKS.
3. Jika KONTEKS hanya relevan sebagian, jawab hanya bagian yang didukung KONTEKS.
4. Jika jawaban tidak ditemukan secara jelas di KONTEKS, katakan: "Informasi tersebut tidak ditemukan pada dokumen yang tersedia."
5. Jangan menebak, jangan menyimpulkan terlalu jauh, dan jangan memakai pengetahuan umum di luar KONTEKS.
6. Sebutkan sumber dokumen dengan format [Source: nama dokumen] untuk klaim yang Anda gunakan.
7. Gunakan bahasa yang sama dengan pertanyaan user.
8. Sebelum menjawab, periksa apakah setiap klaim penting benar-benar didukung oleh KONTEKS. Jika tidak didukung, hapus klaim tersebut.

FORMAT JAWABAN:
- Jawaban singkat dan langsung.
- Jika ada beberapa poin, gunakan bullet point.
- Akhiri dengan sumber yang digunakan."""


def build_custom_rag_prompt(system_prompt: str, question: str, context_text: str) -> str:
    """Build a RAG prompt from a custom system prompt."""
    if context_text:
        return f"""{system_prompt.strip()}

KONTEKS:
{context_text}

---

PERTANYAAN USER:
{question}

JAWABAN BERDASARKAN KONTEKS:"""

    return f"""{system_prompt.strip()}

Tidak ditemukan dokumen yang relevan di knowledge base untuk pertanyaan ini.

PERTANYAAN USER:
{question}

JAWABAN BERDASARKAN KONTEKS:
Informasi tersebut tidak ditemukan pada dokumen yang tersedia."""


def _extract_json_array(response_text: str) -> List[str]:
    """Parse a JSON array of prompt strings from LLM output."""
    if not response_text:
        return []

    match = re.search(r"\[[\s\S]*\]", response_text)
    if not match:
        return []

    try:
        parsed = json.loads(match.group(0))
    except json.JSONDecodeError:
        return []

    if not isinstance(parsed, list):
        return []

    return [item.strip() for item in parsed if isinstance(item, str) and item.strip()]


def _fallback_prompt_variants(base_prompt: str) -> List[str]:
    """Return deterministic fallback variants if LLM parsing fails."""
    return [
        f"""{base_prompt}

PRIORITAS TAMBAHAN:
- Utamakan faithfulness di atas kelengkapan jawaban.
- Tulis hanya klaim yang memiliki dukungan eksplisit di KONTEKS.""",
        f"""{base_prompt}

PRIORITAS TAMBAHAN:
- Jawab secara ringkas.
- Jika konteks tidak cukup, sebutkan batasan informasi yang tersedia.""",
        f"""{base_prompt}

PRIORITAS TAMBAHAN:
- Gunakan bullet point untuk memisahkan klaim.
- Setiap bullet harus dapat dilacak ke KONTEKS.""",
        f"""{base_prompt}

PRIORITAS TAMBAHAN:
- Jangan menyimpulkan hubungan sebab-akibat jika tidak tertulis jelas.
- Jangan memperluas jawaban memakai pengetahuan umum.""",
    ]


async def generate_prompt_variants(
    base_prompt: str,
    question: str,
    count: int = 5,
) -> List[str]:
    """Generate prompt variants, keeping the base prompt as the first item."""
    base_prompt = (base_prompt or DEFAULT_RAG_SYSTEM_PROMPT).strip()
    requested_variants = max(count - 1, 0)
    if requested_variants == 0:
        return [base_prompt]

    instruction = f"""Buat {requested_variants} variasi prompt RAG dari prompt awal berikut.

Tujuan variasi:
- meningkatkan faithfulness
- meningkatkan answer relevancy
- meningkatkan context precision
- meningkatkan context recall
- tetap melarang jawaban dari luar konteks

Pertanyaan uji yang sama untuk semua prompt:
{question}

Prompt awal:
{base_prompt}

Kembalikan HANYA JSON array string berisi {requested_variants} prompt lengkap.
Jangan gunakan markdown, komentar, atau penjelasan."""

    llm_variants = _extract_json_array(await generate_response(instruction))
    fallback_variants = _fallback_prompt_variants(base_prompt)
    variants: List[str] = []

    for prompt in llm_variants + fallback_variants:
        if prompt and prompt != base_prompt and prompt not in variants:
            variants.append(prompt)
        if len(variants) >= requested_variants:
            break

    return [base_prompt] + variants[:requested_variants]

