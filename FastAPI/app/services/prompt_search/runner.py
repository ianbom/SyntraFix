"""Prompt search experiment runner."""
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.document_chunk import DocumentChunk
from app.services.chat import ChatService
from app.services.embedding import generate_embedding
from app.services.llm import generate_response
from app.services.prompt_search.prompt_variants import (
    DEFAULT_RAG_SYSTEM_PROMPT,
    build_custom_rag_prompt,
    generate_prompt_variants,
)
from app.services.prompt_search.ragas_evaluator import (
    calculate_final_score,
    evaluate_iteration_with_ragas,
    select_best_iteration,
)
from app.services.prompt_search.reference_generator import generate_reference_from_context
from app.services.prompt_search.storage import save_prompt_search_result


class PromptSearchRunner:
    """Run prompt search without writing to chat/conversation tables."""

    def __init__(self, db: Session, output_dir: Optional[Path] = None):
        self.db = db
        self.output_dir = output_dir

    async def run(self, question: str, prompt: Optional[str] = None) -> Dict[str, Any]:
        base_prompt = (prompt or DEFAULT_RAG_SYSTEM_PROMPT).strip()
        run_id = uuid4().hex[:10]
        prompts = await generate_prompt_variants(base_prompt, question, count=5)
        chat_service = ChatService(self.db)

        iterations = []
        for index, system_prompt in enumerate(prompts, start=1):
            iterations.append(
                await self._run_iteration(
                    chat_service=chat_service,
                    iteration=index,
                    question=question,
                    system_prompt=system_prompt,
                )
            )

        best = select_best_iteration(iterations)
        result: Dict[str, Any] = {
            "run_id": run_id,
            "question": question,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "best_iteration": best.get("iteration") if best else None,
            "best_score": best.get("final_score") if best else None,
            "best_prompt": best.get("prompt") if best else None,
            "iterations": iterations,
        }
        output_path = save_prompt_search_result(result, self.output_dir)
        result["output_file"] = str(output_path)
        return result

    async def _run_iteration(
        self,
        chat_service: ChatService,
        iteration: int,
        question: str,
        system_prompt: str,
    ) -> Dict[str, Any]:
        chunks: List[DocumentChunk] = []
        similarities: List[float] = []
        contexts: List[str] = []
        answer = ""
        reference = ""

        try:
            chunks, similarities = await self._retrieve_chunks(chat_service, question)
            context_text = chat_service._construct_context_text(chunks)
            full_prompt = build_custom_rag_prompt(system_prompt, question, context_text)
            answer = await generate_response(full_prompt)
            contexts = [chunk.content for chunk in chunks if chunk.content]
            reference = await generate_reference_from_context(question, answer, contexts)
            ragas_metrics = evaluate_iteration_with_ragas(
                question=question,
                contexts=contexts,
                answer=answer,
                reference=reference,
            )
            final_score = calculate_final_score(ragas_metrics)
            error = None
        except Exception as exc:
            ragas_metrics = {
                "faithfulness": None,
                "answer_relevancy": None,
                "context_precision": None,
                "context_recall": None,
            }
            final_score = None
            error = str(exc)

        return {
            "iteration": iteration,
            "prompt": system_prompt,
            "question": question,
            "answer": answer,
            "reference": reference,
            "chunks": self._serialize_chunks(chunks, similarities),
            "ragas": ragas_metrics,
            "final_score": final_score,
            "error": error,
        }

    async def _retrieve_chunks(
        self,
        chat_service: ChatService,
        question: str,
    ):
        query_info = chat_service._process_query(question)
        metadata_filters = chat_service._build_metadata_filters(query_info["entities"])
        expanded_queries = await chat_service._expand_query(query_info["cleaned_query"])
        query_embeddings = []
        for query in expanded_queries:
            embedding = generate_embedding(query)
            if embedding is not None:
                query_embeddings.append(embedding)

        return await chat_service._retrieve_and_rerank_chunks(
            query=query_info["cleaned_query"],
            metadata_filters=metadata_filters,
            query_embeddings=query_embeddings,
        )

    def _serialize_chunks(
        self,
        chunks: List[DocumentChunk],
        similarities: List[float],
    ) -> List[Dict[str, Any]]:
        return [
            {
                "chunk_id": chunk.id,
                "document_id": chunk.document_id,
                "document_title": self._get_document_title(chunk.document_id),
                "section_title": chunk.section_title,
                "page_number": chunk.page_number,
                "relevance_score": float(similarities[index]) if index < len(similarities) else None,
                "content": chunk.content,
            }
            for index, chunk in enumerate(chunks)
        ]

    def _get_document_title(self, document_id: int) -> str:
        if not self.db or not document_id:
            return "Unknown Document"
        doc = self.db.query(Document).filter(Document.id == document_id).first()
        return doc.title if doc and doc.title else "Unknown Document"

