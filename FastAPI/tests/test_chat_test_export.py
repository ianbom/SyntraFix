from types import SimpleNamespace

from app.models.chat import ChatRole
from app.services.chat_test_export import (
    build_single_chat_test_markdown,
    export_single_chat_test_markdown,
    format_retrieved_context,
    safe_filename,
)


def test_format_retrieved_context_matches_ragas_sample_shape():
    references = [
        SimpleNamespace(
            quote="CNN adalah jaringan saraf untuk data visual.",
            document_title="Prediction of Ball Position",
            page_number=7,
        ),
        SimpleNamespace(
            quote="CNN digunakan untuk mendeteksi bola.",
            document_title="Prediction of Ball Position",
            page_number=None,
        ),
    ]

    markdown = format_retrieved_context(references)

    assert "1. CNN adalah jaringan saraf untuk data visual. (Prediction of Ball Position, page 7)" in markdown
    assert "2. CNN digunakan untuk mendeteksi bola. (Prediction of Ball Position)" in markdown


def test_build_single_chat_test_markdown_has_empty_reference():
    conversation = SimpleNamespace(id=8)
    user_chat = SimpleNamespace(id=235, role=ChatRole.USER, message="Apa itu CNN?")
    bot_chat = SimpleNamespace(
        id=236,
        role=ChatRole.BOT,
        message="CNN adalah jaringan saraf untuk data visual.",
        references=[],
    )

    markdown = build_single_chat_test_markdown(
        conversation=conversation,
        user_chat=user_chat,
        bot_chat=bot_chat,
    )

    assert markdown.startswith("# RAGAS Test Data")
    assert "- conversation_id: 8" in markdown
    assert "- user_chat_id: 235" in markdown
    assert "- bot_chat_id: 236" in markdown
    assert "### user_input\n\nApa itu CNN?" in markdown
    assert "### response\n\nCNN adalah jaringan saraf untuk data visual." in markdown
    assert "### reference\n\n\n---" in markdown


def test_export_single_chat_test_markdown_writes_unique_file(tmp_path):
    conversation = SimpleNamespace(id=8)
    user_chat = SimpleNamespace(id=235, role=ChatRole.USER, message="Apa itu CNN?")
    bot_chat = SimpleNamespace(
        id=236,
        role=ChatRole.BOT,
        message="CNN adalah jaringan saraf untuk data visual.",
        references=[],
    )

    first_path = export_single_chat_test_markdown(
        conversation=conversation,
        user_chat=user_chat,
        bot_chat=bot_chat,
        output_dir=tmp_path,
    )
    second_path = export_single_chat_test_markdown(
        conversation=conversation,
        user_chat=user_chat,
        bot_chat=bot_chat,
        output_dir=tmp_path,
    )

    assert first_path.exists()
    assert second_path.exists()
    assert first_path != second_path
    assert safe_filename("Apa itu CNN?") in first_path.name
