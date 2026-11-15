"""Tests for the suggestion engine stub."""

from nimblet.suggester import suggest_snippet


def test_suggest_snippet_for_loop() -> None:
    snippet = suggest_snippet("for loop")
    assert snippet is not None
    assert len(snippet) > 0
    assert "for" in snippet


def test_suggest_snippet_unknown() -> None:
    assert suggest_snippet("hello world") is None
    assert suggest_snippet("") is None
    assert suggest_snippet("FOR LOOP") is None
