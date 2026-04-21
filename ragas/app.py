from pathlib import Path
import os
import re
import time
from typing import Any

from datasets import Dataset
from dotenv import load_dotenv
from langchain_ollama import ChatOllama, OllamaEmbeddings
from ragas import evaluate
from ragas.metrics import AnswerRelevancy, ContextPrecision, ContextRecall, Faithfulness


load_dotenv(override=True)

BASE_DIR = Path(__file__).resolve().parents[1]
RAGAS_SAMPLE_PATH = BASE_DIR / "FastAPI" / "ragas-sample-bge.md"
OUTPUT_CSV_PATH = Path(__file__).resolve().parent / "score_ragas_sample_bge4.csv"
MAX_EVALUATION_ATTEMPTS = int(os.getenv("RAGAS_MAX_EVALUATION_ATTEMPTS", "5"))
RETRY_DELAY_SECONDS = float(os.getenv("RAGAS_RETRY_DELAY_SECONDS", "3"))

METRICS = [
    Faithfulness(),
    AnswerRelevancy(),
    ContextPrecision(),
    ContextRecall(),
]


llm = ChatOllama(
    model="llama3.1:8b",
    base_url="http://localhost:11435",
    temperature=0.1,
)

embeddings = OllamaEmbeddings(
    model="bge-m3:567m",
    base_url="http://localhost:11435",
)


def _extract_section(sample_text: str, section_name: str) -> str:
    pattern = rf"### {re.escape(section_name)}\s*\n\n(.*?)(?=\n### |\n---\s*$|\Z)"
    match = re.search(pattern, sample_text, flags=re.DOTALL)
    return match.group(1).strip() if match else ""


def _parse_retrieved_contexts(context_text: str) -> list[str]:
    context_text = context_text.strip()
    if not context_text:
        return []

    parts = re.split(r"\n(?=\d+\.\s)", context_text)
    contexts = []
    for part in parts:
        cleaned = re.sub(r"^\d+\.\s*", "", part.strip())
        if cleaned:
            contexts.append(cleaned)

    return contexts or [context_text]


def _is_empty_value(value: Any) -> bool:
    if value is None:
        return True

    if isinstance(value, str):
        cleaned = value.strip()
        return cleaned == "" or cleaned.lower() in {"nan", "none", "null"}

    if isinstance(value, list):
        return len(value) == 0 or all(_is_empty_value(item) for item in value)

    return False


def _validate_samples(data_samples: dict) -> None:
    required_fields = [
        "user_input",
        "retrieved_contexts",
        "response",
        "reference",
        "question",
        "contexts",
        "answer",
        "ground_truth",
    ]
    row_count = len(data_samples.get("user_input", []))
    errors = []

    for field in required_fields:
        values = data_samples.get(field)
        if values is None:
            errors.append(f"Missing field: {field}")
            continue
        if len(values) != row_count:
            errors.append(f"Field {field} length mismatch: {len(values)} != {row_count}")
            continue
        for index, value in enumerate(values, start=1):
            if _is_empty_value(value):
                errors.append(f"Empty value at sample {index}, field {field}")

    if errors:
        joined_errors = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"Invalid RAGAS dataset. Fix these values first:\n{joined_errors}")


def _find_invalid_dataframe_cells(df) -> list[str]:
    invalid_cells = []
    for column in df.columns:
        for row_index, value in enumerate(df[column].tolist(), start=1):
            is_invalid = False
            try:
                is_invalid = bool(df[column].isna().iloc[row_index - 1])
            except TypeError:
                is_invalid = False

            if is_invalid or _is_empty_value(value):
                invalid_cells.append(f"row={row_index}, column={column}, value={value!r}")

    return invalid_cells


def evaluate_until_complete(dataset: Dataset):
    """Run RAGAS repeatedly until the result has no NaN/null/empty values."""
    last_invalid_cells = []

    for attempt in range(1, MAX_EVALUATION_ATTEMPTS + 1):
        print(f"\nRAGAS evaluation attempt {attempt}/{MAX_EVALUATION_ATTEMPTS}")
        score = evaluate(
            dataset,
            metrics=METRICS,
            llm=llm,
            embeddings=embeddings,
            batch_size=2,
        )

        df = score.to_pandas()
        invalid_cells = _find_invalid_dataframe_cells(df)
        if not invalid_cells:
            print("RAGAS result is complete. No NaN/null/empty values found.")
            return df

        last_invalid_cells = invalid_cells
        print("RAGAS result still contains invalid values:")
        for cell in invalid_cells[:20]:
            print(f"  - {cell}")
        if len(invalid_cells) > 20:
            print(f"  ... and {len(invalid_cells) - 20} more invalid cells")

        if attempt < MAX_EVALUATION_ATTEMPTS:
            print(f"Retrying in {RETRY_DELAY_SECONDS} seconds...")
            time.sleep(RETRY_DELAY_SECONDS)

    joined_cells = "\n".join(f"- {cell}" for cell in last_invalid_cells)
    raise RuntimeError(
        "RAGAS evaluation still produced NaN/null/empty values after "
        f"{MAX_EVALUATION_ATTEMPTS} attempts:\n{joined_cells}"
    )


def load_ragas_markdown(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"RAGAS sample file not found: {path}")

    markdown = path.read_text(encoding="utf-8")
    sample_blocks = re.split(r"\n(?=## Sample \d+\b)", markdown)
    rows = []

    for block in sample_blocks:
        if not block.lstrip().startswith("## Sample"):
            continue

        user_input = _extract_section(block, "user_input")
        retrieved_context = _extract_section(block, "retrieved_context")
        response = _extract_section(block, "response")
        reference = _extract_section(block, "reference")
        retrieved_contexts = _parse_retrieved_contexts(retrieved_context)

        sample_match = re.search(r"## Sample (\d+)", block)
        sample_label = sample_match.group(1) if sample_match else "unknown"

        missing_fields = []
        if _is_empty_value(user_input):
            missing_fields.append("user_input")
        if _is_empty_value(retrieved_contexts):
            missing_fields.append("retrieved_context")
        if _is_empty_value(response):
            missing_fields.append("response")
        if _is_empty_value(reference):
            missing_fields.append("reference")

        if missing_fields:
            raise ValueError(
                f"Sample {sample_label} has empty required field(s): "
                f"{', '.join(missing_fields)}"
            )

        rows.append(
            {
                # Newer RAGAS schema.
                "user_input": user_input,
                "retrieved_contexts": retrieved_contexts,
                "response": response,
                "reference": reference,
                # Compatibility columns for older RAGAS versions.
                "question": user_input,
                "contexts": retrieved_contexts,
                "answer": response,
                "ground_truth": reference,
            }
        )

    if not rows:
        raise ValueError(f"No complete RAGAS samples found in {path}")

    return {
        "user_input": [row["user_input"] for row in rows],
        "retrieved_contexts": [row["retrieved_contexts"] for row in rows],
        "response": [row["response"] for row in rows],
        "reference": [row["reference"] for row in rows],
        "question": [row["question"] for row in rows],
        "contexts": [row["contexts"] for row in rows],
        "answer": [row["answer"] for row in rows],
        "ground_truth": [row["ground_truth"] for row in rows],
    }


def main() -> None:
    data_samples = load_ragas_markdown(RAGAS_SAMPLE_PATH)
    _validate_samples(data_samples)
    dataset = Dataset.from_dict(data_samples)

    print(f"Loaded {len(dataset)} RAGAS samples from {RAGAS_SAMPLE_PATH}")

    df = evaluate_until_complete(dataset)
    df.to_csv(OUTPUT_CSV_PATH, index=False)

    print(f"Evaluasi selesai! Hasil disimpan di {OUTPUT_CSV_PATH}")
    print("\nHasil Evaluasi:")
    print(df)

    invalid_cells = _find_invalid_dataframe_cells(df)
    if invalid_cells:
        raise RuntimeError(f"CSV output still contains invalid values: {invalid_cells}")

    print("\nTidak ada NaN/null/kosong.")


if __name__ == "__main__":
    main()
