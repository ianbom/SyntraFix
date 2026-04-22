"""Post test questions to Syntra's chat API.

Usage examples:
    python scripts/chat_agent_runner.py --token "YOUR_ACCESS_TOKEN"
    python scripts/chat_agent_runner.py --token "YOUR_ACCESS_TOKEN" --conversation-id 123
    python scripts/chat_agent_runner.py --base-url http://localhost:8000 --delay 3
    python scripts/chat_agent_runner.py --questions-file scripts/chat_agent_questions.txt

Environment variables:
    SYNTRA_BASE_URL        Default: http://localhost:8000
    SYNTRA_ACCESS_TOKEN    Required unless --token is provided
    SYNTRA_CONVERSATION_ID Optional conversation id to continue
    SYNTRA_QUESTIONS_FILE  Optional path to a line-based questions file
"""
from __future__ import annotations

import argparse
import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests


DEFAULT_QUESTIONS_FILE = Path(__file__).resolve().parent / "chat_agent_questions.txt"


def load_questions(path: Path) -> list[str]:
    """Load one question per line, ignoring blank lines and comments."""
    if not path.exists():
        raise FileNotFoundError(f"Questions file not found: {path}")

    questions = []
    for line in path.read_text(encoding="utf-8").splitlines():
        question = line.strip()
        if not question or question.startswith("#"):
            continue
        questions.append(question)

    if not questions:
        raise ValueError(f"No questions found in file: {path}")

    return questions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Send test questions to Syntra POST /chats/ with one conversation_id."
    )
    parser.add_argument(
        "--base-url",
        default=os.getenv("SYNTRA_BASE_URL", "http://localhost:8000"),
        help="Syntra FastAPI base URL. Default: %(default)s",
    )
    parser.add_argument(
        "--token",
        default=os.getenv("SYNTRA_ACCESS_TOKEN"),
        help="Bearer access token. Can also use SYNTRA_ACCESS_TOKEN.",
    )
    parser.add_argument(
        "--conversation-id",
        type=int,
        default=(
            int(os.environ["SYNTRA_CONVERSATION_ID"])
            if os.getenv("SYNTRA_CONVERSATION_ID")
            else 8
        ),
        help="Existing conversation id. If omitted, first request creates one.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=2.0,
        help="Delay between requests in seconds. Default: %(default)s",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=3000.0,
        help="Request timeout in seconds. Default: %(default)s",
    )
    parser.add_argument(
        "--questions-file",
        default=os.getenv("SYNTRA_QUESTIONS_FILE", str(DEFAULT_QUESTIONS_FILE)),
        help="Text file containing one question per line. Default: %(default)s",
    )
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parent / "chat_agent_outputs"),
        help="Directory for JSON and Markdown output.",
    )
    return parser.parse_args()


def post_chat(
    base_url: str,
    token: str,
    message: str,
    conversation_id: int | None,
    timeout: float,
) -> dict[str, Any]:
    payload: dict[str, Any] = {"message": message}
    if conversation_id is not None:
        payload["conversation_id"] = conversation_id

    response = requests.post(
        f"{base_url.rstrip('/')}/chats/",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


def write_outputs(output_dir: Path, rows: list[dict[str, Any]], conversation_id: int | None) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    suffix = f"conversation_{conversation_id or 'new'}_{timestamp}"

    json_path = output_dir / f"chat_agent_{suffix}.json"
    md_path = output_dir / f"chat_agent_{suffix}.md"

    json_path.write_text(
        json.dumps(rows, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# Chat Agent Run",
        "",
        f"- conversation_id: {conversation_id}",
        f"- total_questions: {len(rows)}",
        f"- generated_at: {datetime.now().isoformat(timespec='seconds')}",
        "",
    ]
    for row in rows:
        lines.extend(
            [
                f"## Question {row['index']}",
                "",
                "### user_input",
                "",
                row["question"],
                "",
                "### response",
                "",
                row.get("response_message") or row.get("error") or "-",
                "",
                "---",
                "",
            ]
        )
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"\nSaved JSON output: {json_path}")
    print(f"Saved Markdown output: {md_path}")


def main() -> None:
    args = parse_args()
    if not args.token:
        raise SystemExit(
            "Missing access token. Pass --token or set SYNTRA_ACCESS_TOKEN."
        )

    conversation_id = args.conversation_id
    questions = load_questions(Path(args.questions_file))
    output_rows: list[dict[str, Any]] = []

    print(f"Base URL        : {args.base_url}")
    print(f"Conversation ID: {conversation_id or 'create from first request'}")
    print(f"Questions file : {args.questions_file}")
    print(f"Total questions: {len(questions)}")
    print("-" * 80)

    for index, question in enumerate(questions, start=1):
        print(f"[{index:02d}/{len(questions)}] {question}")
        row: dict[str, Any] = {
            "index": index,
            "question": question,
            "conversation_id_before_request": conversation_id,
        }

        try:
            data = post_chat(
                base_url=args.base_url,
                token=args.token,
                message=question,
                conversation_id=conversation_id,
                timeout=args.timeout,
            )
            conversation_id = int(data["conversation_id"])
            row.update(
                {
                    "status": "success",
                    "chat_id": data.get("id"),
                    "conversation_id": conversation_id,
                    "response_message": data.get("message"),
                    "raw_response": data,
                }
            )
            print(f"  OK chat_id={data.get('id')} conversation_id={conversation_id}")
            print(f"  Bot: {(data.get('message') or '')[:180]}")
        except Exception as error:
            row.update(
                {
                    "status": "error",
                    "conversation_id": conversation_id,
                    "error": str(error),
                }
            )
            print(f"  ERROR: {error}")

        output_rows.append(row)

        if index < len(questions):
            time.sleep(args.delay)

    write_outputs(Path(args.output_dir), output_rows, conversation_id)

    if conversation_id is not None:
        print(
            "\nRAGAS export endpoint for this run:\n"
            f"{args.base_url.rstrip('/')}/chats/ragas/export?conversation_id={conversation_id}"
        )


if __name__ == "__main__":
    main()
