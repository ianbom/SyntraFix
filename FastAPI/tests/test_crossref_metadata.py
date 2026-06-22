from datetime import date
from types import SimpleNamespace

import pytest

from app.services import crossref


CROSSREF_ITEM = {
    "DOI": "10.1234/Example.DOI",
    "title": ["A Reliable RAG Pipeline"],
    "author": [
        {"given": "Ada", "family": "Lovelace"},
        {"given": "Alan", "family": "Turing"},
    ],
    "container-title": ["Journal of RAG"],
    "publisher": "ACM",
    "published-print": {"date-parts": [[2024, 5, 12]]},
    "abstract": "<jats:p>This is the abstract.</jats:p>",
    "subject": ["retrieval", "metadata"],
    "language": "en",
    "is-referenced-by-count": 7,
    "license": [{"URL": "https://creativecommons.org/licenses/by/4.0/"}],
    "URL": "https://doi.org/10.1234/example.doi",
}


class FakeResponse:
    def __init__(self, status_code, payload):
        self.status_code = status_code
        self._payload = payload

    def json(self):
        return self._payload


@pytest.fixture(autouse=True)
def crossref_settings(monkeypatch):
    monkeypatch.setattr(
        crossref,
        "settings",
        SimpleNamespace(
            CROSSREF_BASE_URL="https://api.crossref.test",
            CROSSREF_MAILTO=None,
            CROSSREF_TIMEOUT_SECONDS=3,
        ),
    )


def test_extract_doi_from_text_normalizes_and_trims_trailing_punctuation():
    text = "DOI: https://doi.org/10.1234/Example.DOI)."

    assert crossref.extract_doi_from_text(text) == "10.1234/example.doi"


def test_format_crossref_for_database_maps_dublin_core_fields():
    metadata = crossref.format_crossref_for_database(CROSSREF_ITEM)

    assert metadata["title"] == "A Reliable RAG Pipeline"
    assert metadata["creator"] == "Ada Lovelace"
    assert metadata["contributor"] == "Alan Turing"
    assert metadata["source"] == "Journal of RAG"
    assert metadata["publisher"] == "ACM"
    assert metadata["date"] == date(2024, 5, 12)
    assert metadata["doi"] == "10.1234/example.doi"
    assert metadata["identifier"] == "10.1234/example.doi"
    assert metadata["keywords"] == "retrieval, metadata"
    assert metadata["abstract"] == "This is the abstract."
    assert metadata["description"] == "This is the abstract."
    assert metadata["citation_count"] == 7


def test_lookup_crossref_metadata_uses_doi_first(monkeypatch):
    calls = []

    def fake_get(url, **kwargs):
        calls.append((url, kwargs))
        return FakeResponse(200, {"message": CROSSREF_ITEM})

    monkeypatch.setattr(crossref.requests, "get", fake_get)

    metadata = crossref.lookup_crossref_metadata({"doi": "10.1234/Example.DOI", "title": "Different"})

    assert metadata["title"] == "A Reliable RAG Pipeline"
    assert calls[0][0] == "https://api.crossref.test/works/10.1234/example.doi"


def test_lookup_crossref_metadata_accepts_high_similarity_title(monkeypatch):
    def fake_get(url, **kwargs):
        assert kwargs["params"]["query.title"] == "A Reliable RAG Pipeline"
        return FakeResponse(200, {"message": {"items": [CROSSREF_ITEM]}})

    monkeypatch.setattr(crossref.requests, "get", fake_get)

    metadata = crossref.lookup_crossref_metadata({"title": "A Reliable RAG Pipeline"})

    assert metadata["doi"] == "10.1234/example.doi"


def test_lookup_crossref_metadata_rejects_low_similarity_title(monkeypatch):
    def fake_get(url, **kwargs):
        return FakeResponse(200, {"message": {"items": [CROSSREF_ITEM]}})

    monkeypatch.setattr(crossref.requests, "get", fake_get)

    assert crossref.lookup_crossref_metadata({"title": "Completely Different Research"}) == {}


def test_lookup_crossref_metadata_returns_empty_on_request_exception(monkeypatch):
    def fake_get(url, **kwargs):
        raise crossref.requests.exceptions.Timeout("slow")

    monkeypatch.setattr(crossref.requests, "get", fake_get)

    assert crossref.lookup_crossref_metadata({"doi": "10.1234/example"}) == {}
