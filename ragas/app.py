from pathlib import Path
import os
import re
import time
from typing import Any

from datasets import Dataset
from dotenv import load_dotenv
from langchain_ollama import ChatOllama, OllamaEmbeddings
import pandas as pd
from ragas import evaluate
from ragas.metrics import AnswerRelevancy, ContextPrecision, ContextRecall, Faithfulness


load_dotenv(override=True)

BASE_DIR = Path(__file__).resolve().parents[1]
SPLIT_SAMPLE_DIR = Path(__file__).resolve().parent / "data" / "split"
EVALUATE_OUTPUT_DIR = Path(__file__).resolve().parent / "evaluate"
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


def _replace_invalid_dataframe_values(df, replacement: Any = pd.NA):
    """Replace invalid result cells with a visible fallback value."""
    cleaned_df = df.copy().astype(object)

    for column in cleaned_df.columns:
        for row_index, value in enumerate(cleaned_df[column].tolist()):
            is_invalid = False
            try:
                is_invalid = bool(cleaned_df[column].isna().iloc[row_index])
            except TypeError:
                is_invalid = False

            if is_invalid or _is_empty_value(value):
                cleaned_df.at[row_index, column] = replacement

    return cleaned_df


def _fallback_nan_score_dataframe(dataset: Dataset):
    """Build a NaN-score result row when RAGAS evaluation cannot complete."""
    df = dataset.to_pandas()
    for column in [
        "faithfulness",
        "answer_relevancy",
        "context_precision",
        "context_recall",
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
                batch_size=2,
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
                "Writing this sample with NaN score values."
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


def _merge_data_samples(sample_sets: list[dict]) -> dict:
    if not sample_sets:
        raise ValueError("No RAGAS sample sets were provided")

    fields = [
        "user_input",
        "retrieved_contexts",
        "response",
        "reference",
        "question",
        "contexts",
        "answer",
        "ground_truth",
    ]
    merged = {field: [] for field in fields}
    for sample_set in sample_sets:
        for field in fields:
            merged[field].extend(sample_set[field])
    return merged


def _slice_data_samples(data_samples: dict, start_index: int, end_index: int) -> dict:
    """Slice row-oriented RAGAS sample dict from start_index inclusive to end_index exclusive."""
    return {
        field: values[start_index:end_index]
        for field, values in data_samples.items()
    }


def _get_sample_paths() -> list[Path]:
    configured_paths = os.getenv("RAGAS_SAMPLE_PATHS")
    if not configured_paths:
        paths = sorted(SPLIT_SAMPLE_DIR.glob("*.md"))
        if not paths:
            raise FileNotFoundError(f"No split sample files found in {SPLIT_SAMPLE_DIR}")
        return paths

    paths = []
    for raw_path in configured_paths.split(";"):
        raw_path = raw_path.strip()
        if not raw_path:
            continue
        path = Path(raw_path)
        if not path.is_absolute():
            path = BASE_DIR / path
        paths.append(path)

    if not paths:
        raise ValueError("RAGAS_SAMPLE_PATHS is set but contains no valid paths")
    return paths


def _get_file_output_path(sample_path: Path) -> Path:
    return EVALUATE_OUTPUT_DIR / f"{sample_path.stem}.csv"


def _clear_previous_outputs() -> None:
    EVALUATE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for output_path in EVALUATE_OUTPUT_DIR.glob("sample-conv*-samples-*.csv"):
        output_path.unlink()


def _save_file_result(df, sample_path: Path) -> Path:
    EVALUATE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = _get_file_output_path(sample_path)
    df.insert(0, "source_file", sample_path.name)
    df.to_csv(
        output_path,
        index=False,
        na_rep="NaN",
    )
    return output_path


def main() -> None:
    sample_paths = _get_sample_paths()
    _clear_previous_outputs()

    print(f"Loaded {len(sample_paths)} split sample file(s)")
    print("Evaluation step: 1 split file at a time")
    print("CSV file size: follows each split sample file")
    print(f"CSV output folder: {EVALUATE_OUTPUT_DIR}")

    output_paths = []
    for file_index, sample_path in enumerate(sample_paths, start=1):
        data_samples = load_ragas_markdown(sample_path)
        _validate_samples(data_samples)
        dataset = Dataset.from_dict(data_samples)
        sample_count = len(data_samples["user_input"])
        label = f"{sample_path.name} ({sample_count} samples)"

        print("\n" + "=" * 80)
        print(f"Evaluating file {file_index}/{len(sample_paths)}: {label}")
        print("=" * 80)

        df = evaluate_until_complete(dataset, label=label)
        output_path = _save_file_result(df, sample_path)
        output_paths.append(output_path)
        print(f"File {sample_path.name} selesai. CSV dibuat di {output_path}")

    print("\nEvaluasi selesai untuk semua file sample.")
    print(f"CSV tersimpan di folder: {EVALUATE_OUTPUT_DIR}")
    for output_path in output_paths:
        print(f"- {output_path}")


if __name__ == "__main__":
    main()
