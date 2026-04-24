from app.api.routes.documents import _get_possibly_question_counts
from app.models.document_chunk import DocumentChunk
from app.tasks.document_tasks import _chunk_has_possibly_questions


class FakeQuery:
    def __init__(self, rows):
        self.rows = rows

    def filter(self, *_args, **_kwargs):
        return self

    def all(self):
        return self.rows


class FakeDb:
    def __init__(self, rows):
        self.rows = rows

    def query(self, *_args, **_kwargs):
        return FakeQuery(self.rows)


def make_chunk(questions=None, question_embedding=None):
    chunk = DocumentChunk()
    chunk.content = "Konten chunk yang cukup panjang untuk diproses."
    chunk.token_count = 45
    chunk.possibly_questions = questions
    chunk.possibly_question_embedding = question_embedding
    return chunk


def test_chunk_has_possibly_questions_requires_questions_and_embedding():
    assert _chunk_has_possibly_questions(make_chunk(["Apa isi chunk?"], [0.1, 0.2]))
    assert not _chunk_has_possibly_questions(make_chunk(["Apa isi chunk?"], None))
    assert not _chunk_has_possibly_questions(make_chunk([], [0.1, 0.2]))
    assert not _chunk_has_possibly_questions(make_chunk(None, None))


def test_possibly_question_counts_use_complete_question_rows():
    chunks = [
        make_chunk(["Apa isi chunk pertama?"], [0.1, 0.2]),
        make_chunk(["Apa isi chunk kedua?"], None),
        make_chunk(None, None),
    ]

    counts = _get_possibly_question_counts(FakeDb(chunks), document_id=1)

    assert counts["chunk_count"] == 3
    assert counts["possibly_question_count"] == 1
    assert counts["possibly_question_missing_count"] == 2
    assert counts["possibly_question_progress"] == 33
