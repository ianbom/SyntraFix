from pathlib import Path
from datetime import datetime
import os
import re
import sys
import time
from typing import Any

from datasets import Dataset
from dotenv import load_dotenv
from langchain_ollama import ChatOllama, OllamaEmbeddings
import pandas as pd


CURRENT_DIR = Path(__file__).resolve().parent
current_dir_text = str(CURRENT_DIR)
removed_current_dir = False
if sys.path and Path(sys.path[0]).resolve() == CURRENT_DIR:
    sys.path.pop(0)
    removed_current_dir = True

try:
    from ragas import evaluate
    from ragas.metrics import AnswerRelevancy, Faithfulness
finally:
    if removed_current_dir:
        sys.path.insert(0, current_dir_text)


load_dotenv(override=True)

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = CURRENT_DIR / "data"
EVALUATE_OUTPUT_DIR = CURRENT_DIR / "evaluate"
MAX_EVALUATION_ATTEMPTS = int(os.getenv("RAGAS_MAX_EVALUATION_ATTEMPTS", "5"))
RETRY_DELAY_SECONDS = float(os.getenv("RAGAS_RETRY_DELAY_SECONDS", "3"))
BATCH_SIZE = int(os.getenv("RAGAS_OUTPUT_BATCH_SIZE", "5"))
RAGAS_EVALUATION_BATCH_SIZE = int(os.getenv("RAGAS_EVALUATION_BATCH_SIZE", "2"))

METRICS = [
    Faithfulness(),
    AnswerRelevancy(),
]


llm = ChatOllama(
    model=os.getenv("RAGAS_LLM_MODEL", "llama3.1:8b-instruct-q8_0"),
    base_url=os.getenv("RAGAS_OLLAMA_BASE_URL", "http://localhost:11435"),
    temperature=float(os.getenv("RAGAS_LLM_TEMPERATURE", "0.1")),
)

embeddings = OllamaEmbeddings(
    model=os.getenv("RAGAS_EMBEDDING_MODEL", "bge-m3:567m"),
    base_url=os.getenv("RAGAS_OLLAMA_BASE_URL", "http://localhost:11435"),
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
        "question",
        "contexts",
        "answer",
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


def _fallback_nan_score_dataframe(dataset: Dataset):
    df = dataset.to_pandas()
    for column in [
        "faithfulness",
        "answer_relevancy",
    ]:
        if column not in df.columns:
            df[column] = pd.NA
    return df


def evaluate_until_complete(dataset: Dataset, label: str = ""):
    """Run RAGAS repeatedly until the result has no NaN/null/empty values."""
    last_invalid_cells = []
    last_df = None
    label_suffix = f" for {label}" if label else ""

    for attempt in range(1, MAX_EVALUATION_ATTEMPTS + 1):
        print(f"\nRAGAS evaluation attempt {attempt}/{MAX_EVALUATION_ATTEMPTS}{label_suffix}")
        try:
            score = evaluate(
                dataset,
                metrics=METRICS,
                llm=llm,
                embeddings=embeddings,
                batch_size=RAGAS_EVALUATION_BATCH_SIZE,
            )
        except Exception as error:
            last_invalid_cells = [f"evaluation error: {error}"]
            print(f"RAGAS evaluation failed: {error}")
            if attempt < MAX_EVALUATION_ATTEMPTS:
                print(f"Retrying in {RETRY_DELAY_SECONDS} seconds...")
                time.sleep(RETRY_DELAY_SECONDS)
                continue

            print(
                "RAGAS failed after max attempts. "
                "Writing this batch with NaN score values."
            )
            return _fallback_nan_score_dataframe(dataset)

        df = score.to_pandas()
        last_df = df
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

    print(
        "RAGAS evaluation still produced NaN/null/empty values after "
        f"{MAX_EVALUATION_ATTEMPTS} attempts. Keeping the last result as-is "
        "and writing NaN/null/empty values to CSV."
    )
    for cell in last_invalid_cells[:20]:
        print(f"  - {cell}")

    if last_df is None:
        return _fallback_nan_score_dataframe(dataset)

    return last_df


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
                # Compatibility columns for older RAGAS versions.
                "question": user_input,
                "contexts": retrieved_contexts,
                "answer": response,
            }
        )

    if not rows:
        raise ValueError(f"No complete RAGAS samples found in {path}")

    return {
        "user_input": [row["user_input"] for row in rows],
        "retrieved_contexts": [row["retrieved_contexts"] for row in rows],
        "response": [row["response"] for row in rows],
        "question": [row["question"] for row in rows],
        "contexts": [row["contexts"] for row in rows],
        "answer": [row["answer"] for row in rows],
    }


def _slice_data_samples(data_samples: dict, start_index: int, end_index: int) -> dict:
    return {
        field: values[start_index:end_index]
        for field, values in data_samples.items()
    }


def _resolve_sample_path(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = BASE_DIR / path
    return path


def _get_sample_path() -> Path:
    if len(sys.argv) > 1:
        return _resolve_sample_path(sys.argv[1])

    configured_path = os.getenv("RAGAS_SAMPLE_PATH")
    if configured_path:
        return _resolve_sample_path(configured_path)

    default_path = DATA_DIR / "sample-solo.md"
    if default_path.exists():
        return default_path

    markdown_paths = sorted(DATA_DIR.glob("*.md"))
    if len(markdown_paths) == 1:
        return markdown_paths[0]

    if not markdown_paths:
        raise FileNotFoundError(
            f"No markdown sample file found in {DATA_DIR}. "
            "Set RAGAS_SAMPLE_PATH or pass the file path as the first argument."
        )

    raise ValueError(
        "More than one markdown sample file found. "
        "Set RAGAS_SAMPLE_PATH or pass the file path as the first argument."
    )


def _create_run_output_dir() -> Path:
    run_id = os.getenv("RAGAS_RUN_ID") or datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = EVALUATE_OUTPUT_DIR / f"run-{run_id}"
    suffix = 1

    while output_dir.exists():
        output_dir = EVALUATE_OUTPUT_DIR / f"run-{run_id}-{suffix:02d}"
        suffix += 1

    output_dir.mkdir(parents=True, exist_ok=False)
    return output_dir


def _get_batch_output_path(sample_path: Path, output_dir: Path, start_index: int, end_index: int) -> Path:
    output_path = output_dir / f"{sample_path.stem}-samples-{start_index + 1:03d}-{end_index:03d}.csv"
    suffix = 1

    while output_path.exists():
        output_path = (
            output_dir
            / f"{sample_path.stem}-samples-{start_index + 1:03d}-{end_index:03d}-{suffix:02d}.csv"
        )
        suffix += 1

    return output_path


def _save_batch_result(df, sample_path: Path, output_dir: Path, start_index: int, end_index: int) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = _get_batch_output_path(sample_path, output_dir, start_index, end_index)
    df.insert(0, "source_file", sample_path.name)
    df.insert(1, "sample_start", start_index + 1)
    df.insert(2, "sample_end", end_index)
    df.to_csv(
        output_path,
        index=False,
        na_rep="NaN",
    )
    return output_path


def main() -> None:
    sample_path = _get_sample_path()
    data_samples = load_ragas_markdown(sample_path)
    _validate_samples(data_samples)
    run_output_dir = _create_run_output_dir()
    sample_count = len(data_samples["user_input"])

    print(f"Loaded 1 sample file: {sample_path}")
    print("Evaluation mode: without reference/ground_truth")
    metric_names = [
        getattr(metric, "name", metric.__class__.__name__)
        for metric in METRICS
    ]
    print(f"Metrics: {', '.join(metric_names)}")
    print(f"CSV file size: {BATCH_SIZE} samples per file")
    print(f"Total samples: {sample_count}")
    print(f"CSV output folder: {run_output_dir}")

    output_paths = []
    for start_index in range(0, sample_count, BATCH_SIZE):
        end_index = min(start_index + BATCH_SIZE, sample_count)
        batch_samples = _slice_data_samples(data_samples, start_index, end_index)
        dataset = Dataset.from_dict(batch_samples)
        label = f"{sample_path.name} samples {start_index + 1}-{end_index}"

        print("\n" + "=" * 80)
        print(f"Evaluating {label}")
        print("=" * 80)

        df = evaluate_until_complete(dataset, label=label)
        output_path = _save_batch_result(
            df,
            sample_path,
            run_output_dir,
            start_index,
            end_index,
        )
        output_paths.append(output_path)
        print(f"Batch {start_index + 1}-{end_index} selesai. CSV dibuat di {output_path}")

    print("\nEvaluasi selesai untuk semua sample.")
    print(f"CSV tersimpan di folder: {run_output_dir}")
    for output_path in output_paths:
        print(f"- {output_path}")


if __name__ == "__main__":
    main()
