"""Suggestion engine stub."""


def suggest_snippet(text: str) -> str | None:
    """Return a hard-coded snippet for a specific trigger phrase."""
    if text == "for loop":
        return "for item in collection:\n    pass"
    return None
