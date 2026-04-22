from pathlib import Path

import pytest

from app.services.prompt_search import prompt_variants, ragas_evaluator, storage
from app.services.prompt_search.runner import PromptSearchRunner


def test_default_prompt_is_syntra_grounded_prompt():
    prompt = prompt_variants.DEFAULT_RAG_SYSTEM_PROMPT

    assert "Anda adalah asisten AI berbasis dokumen." in prompt
    assert "Jawab HANYA menggunakan informasi yang tertulis di KONTEKS." in prompt
    assert "Informasi tersebut tidak ditemukan pada dokumen yang tersedia." in prompt


def test_prompt_search_route_is_registered():
    from app.main import app

    paths = {route.path for route in app.routes}

    assert "/prompt-search/run" in paths


def test_prompt_search_route_has_no_auth_dependency():
    from app.api.deps import get_current_user
    from app.main import app

    route = next(route for route in app.routes if route.path == "/prompt-search/run")
    dependency_calls = {dependency.call for dependency in route.dependant.dependencies}

    assert get_current_user not in dependency_calls


def test_build_custom_rag_prompt_uses_prompt_context_and_question():
    full_prompt = prompt_variants.build_custom_rag_prompt(
        system_prompt="PROMPT KHUSUS",
        question="Apa itu CNN?",
        context_text="[Source: Dokumen]\nCNN adalah model visual.",
    )

    assert "PROMPT KHUSUS" in full_prompt
    assert "KONTEKS:\n[Source: Dokumen]\nCNN adalah model visual." in full_prompt
    assert "PERTANYAAN USER:\nApa itu CNN?" in full_prompt
    assert full_prompt.endswith("JAWABAN BERDASARKAN KONTEKS:")


@pytest.mark.asyncio
async def test_generate_prompt_variants_keeps_first_prompt_and_parses_llm_json(monkeypatch):
    async def fake_generate_response(_prompt: str) -> str:
        return """
        [
          "Prompt variasi 1",
          "Prompt variasi 2",
          "Prompt variasi 3",
          "Prompt variasi 4"
        ]
        """

    monkeypatch.setattr(prompt_variants, "generate_response", fake_generate_response)

    prompts = await prompt_variants.generate_prompt_variants("Prompt awal", "Apa itu CNN?", count=5)

    assert prompts == [
        "Prompt awal",
        "Prompt variasi 1",
        "Prompt variasi 2",
        "Prompt variasi 3",
        "Prompt variasi 4",
    ]


@pytest.mark.asyncio
async def test_generate_prompt_variants_uses_deterministic_fallback_when_llm_invalid(monkeypatch):
    async def fake_generate_response(_prompt: str) -> str:
        return "bukan json"

    monkeypatch.setattr(prompt_variants, "generate_response", fake_generate_response)

    prompts = await prompt_variants.generate_prompt_variants("Prompt awal", "Apa itu CNN?", count=5)

    assert len(prompts) == 5
    assert prompts[0] == "Prompt awal"
    assert len(set(prompts)) == 5


def test_calculate_final_score_uses_weighted_ragas_metrics():
    metrics = {
        "faithfulness": 0.8,
        "answer_relevancy": 0.6,
        "context_precision": 0.4,
        "context_recall": 1.0,
    }

    score = ragas_evaluator.calculate_final_score(metrics)

    assert score == pytest.approx(0.75)


def test_select_best_iteration_ignores_null_scores():
    iterations = [
        {"iteration": 1, "final_score": None},
        {"iteration": 2, "final_score": 0.71},
        {"iteration": 3, "final_score": 0.84},
    ]

    best = ragas_evaluator.select_best_iteration(iterations)

    assert best["iteration"] == 3


def test_save_prompt_search_result_writes_json(tmp_path: Path):
    result = {
        "run_id": "run-test",
        "question": "Apa itu CNN?",
        "iterations": [],
    }

    output_path = storage.save_prompt_search_result(result, output_dir=tmp_path)

    assert output_path.exists()
    assert output_path.name.startswith("prompt-search-")
    assert "run-test" in output_path.read_text(encoding="utf-8")


@pytest.mark.asyncio
async def test_runner_returns_five_iterations_with_same_question(monkeypatch, tmp_path: Path):
    class FakeChunk:
        id = 10
        document_id = 20
        section_title = "Metode"
        page_number = 7
        content = "CNN digunakan untuk memproses data visual."

    class FakeChatService:
        def __init__(self, _db):
            pass

        def _process_query(self, query):
            return {"cleaned_query": query, "entities": {}}

        def _build_metadata_filters(self, _entities):
            return []

        async def _expand_query(self, query):
            return [query]

        async def _retrieve_and_rerank_chunks(self, **_kwargs):
            return [FakeChunk()], [0.91]

        def _construct_context_text(self, _chunks):
            return "[Source: Dokumen]\nCNN digunakan untuk memproses data visual."

    async def fake_generate_prompt_variants(prompt, _question, count=5):
        return [prompt] + [f"Prompt variasi {index}" for index in range(2, count + 1)]

    async def fake_generate_response(_prompt):
        return "CNN adalah model untuk memproses data visual."

    async def fake_generate_reference(_question, _answer, contexts):
        return contexts[0]

    def fake_evaluate_iteration(_question, _contexts, _answer, _reference):
        return {
            "faithfulness": 0.8,
            "answer_relevancy": 0.7,
            "context_precision": 0.9,
            "context_recall": 0.6,
        }

    monkeypatch.setattr("app.services.prompt_search.runner.ChatService", FakeChatService)
    monkeypatch.setattr("app.services.prompt_search.runner.generate_prompt_variants", fake_generate_prompt_variants)
    monkeypatch.setattr("app.services.prompt_search.runner.generate_response", fake_generate_response)
    monkeypatch.setattr("app.services.prompt_search.runner.generate_reference_from_context", fake_generate_reference)
    monkeypatch.setattr("app.services.prompt_search.runner.evaluate_iteration_with_ragas", fake_evaluate_iteration)

    runner = PromptSearchRunner(db=None, output_dir=tmp_path)
    result = await runner.run(question="Apa itu CNN?", prompt="Prompt awal")

    assert result["question"] == "Apa itu CNN?"
    assert len(result["iterations"]) == 5
    assert {item["question"] for item in result["iterations"]} == {"Apa itu CNN?"}
    assert result["best_iteration"] == 1
    assert Path(result["output_file"]).exists()
