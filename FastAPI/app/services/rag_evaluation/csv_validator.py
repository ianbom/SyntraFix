import csv
import json
from dataclasses import dataclass
from io import StringIO
from typing import Any, Iterable, Literal

EvaluationMode = Literal["pipeline", "score_only"]


@dataclass
class ValidatedCsvRow:
    row_number: int
    test_case_id: str | None
    user_input: str
    reference: str | None
    response: str | None
    retrieved_contexts: list[str] | None
    category: str | None
    source_document_ids: list[Any] | None
    notes: str | None
    validation_status: str
    validation_message: str | None


@dataclass
class CsvValidationResult:
    total_rows: int
    valid_rows: int
    invalid_rows: int
    rows: list[ValidatedCsvRow]
    errors: list[dict[str, Any]]


PIPELINE_REQUIRED_HEADERS = {"user_input", "reference"}
SCORE_ONLY_REQUIRED_HEADERS = {"user_input", "response", "retrieved_contexts", "reference"}


def read_csv_text(content: bytes) -> list[dict[str, str]]:
    try:
        text = content.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        raise ValueError("CSV harus menggunakan encoding UTF-8") from error

    reader = csv.DictReader(StringIO(text))
    if not reader.fieldnames:
        raise ValueError("CSV tidak memiliki header")

    return [dict(row) for row in reader]


def validate_headers(headers: Iterable[str], evaluation_mode: EvaluationMode) -> None:
    normalized = {header.strip() for header in headers if header}
    required = PIPELINE_REQUIRED_HEADERS if evaluation_mode == "pipeline" else SCORE_ONLY_REQUIRED_HEADERS
    missing = sorted(required - normalized)
    if missing:
        raise ValueError(f"Header CSV kurang: {', '.join(missing)}")


def validate_csv_rows(rows: list[dict[str, Any]], evaluation_mode: EvaluationMode) -> CsvValidationResult:
    if evaluation_mode not in {"pipeline", "score_only"}:
        raise ValueError("evaluation_mode harus pipeline atau score_only")
    if not rows:
        raise ValueError("CSV harus memiliki minimal satu baris data")

    validate_headers(rows[0].keys(), evaluation_mode)
    validated_rows: list[ValidatedCsvRow] = []
    errors: list[dict[str, Any]] = []

    for index, raw_row in enumerate(rows, start=1):
        row = {key: _clean(value) for key, value in raw_row.items()}
        messages: list[str] = []
        user_input = row.get("user_input") or ""
        reference = row.get("reference") or None
        response = row.get("response") or None
        retrieved_contexts = _parse_json_array(row.get("retrieved_contexts"))
        source_document_ids = _parse_json_array(row.get("source_document_ids"))

        if not user_input:
            messages.append("user_input wajib diisi")
        if not reference:
            messages.append("reference wajib diisi")

        if evaluation_mode == "score_only":
            if not response:
                messages.append("response wajib diisi")
            if row.get("retrieved_contexts") and retrieved_contexts is None:
                messages.append("retrieved_contexts harus JSON array")
            elif not row.get("retrieved_contexts"):
                messages.append("retrieved_contexts wajib diisi")

        validation_status = "invalid" if messages else "valid"
        validation_message = "; ".join(messages) if messages else None
        if validation_message:
            errors.append({"row_number": index, "message": validation_message})

        validated_rows.append(
            ValidatedCsvRow(
                row_number=index,
                test_case_id=row.get("test_case_id") or None,
                user_input=user_input,
                reference=reference,
                response=response,
                retrieved_contexts=_string_array(retrieved_contexts),
                category=row.get("category") or None,
                source_document_ids=source_document_ids,
                notes=row.get("notes") or None,
                validation_status=validation_status,
                validation_message=validation_message,
            )
        )

    valid_count = sum(1 for row in validated_rows if row.validation_status == "valid")
    return CsvValidationResult(
        total_rows=len(validated_rows),
        valid_rows=valid_count,
        invalid_rows=len(validated_rows) - valid_count,
        rows=validated_rows,
        errors=errors,
    )


def _clean(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _parse_json_array(value: str | None) -> list[Any] | None:
    if not value:
        return None
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, list) else None


def _string_array(value: list[Any] | None) -> list[str] | None:
    if value is None:
        return None
    return [str(item) for item in value if str(item).strip()]
