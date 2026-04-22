"""Prompt search result storage helpers."""
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parents[2] / "prompt_search_results"


def save_prompt_search_result(
    result: Dict[str, Any],
    output_dir: Optional[Path] = None,
) -> Path:
    """Save prompt search result as JSON without overwriting older files."""
    target_dir = output_dir or DEFAULT_OUTPUT_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    run_id = str(result.get("run_id") or "unknown")
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_path = target_dir / f"prompt-search-{timestamp}-{run_id}.json"
    suffix = 1
    while output_path.exists():
        output_path = target_dir / f"prompt-search-{timestamp}-{run_id}-{suffix:02d}.json"
        suffix += 1

    result["output_file"] = str(output_path)
    output_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_path

