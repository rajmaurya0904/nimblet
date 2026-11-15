"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import nimblet


def test_version_is_set() -> None:
    assert nimblet.__version__
