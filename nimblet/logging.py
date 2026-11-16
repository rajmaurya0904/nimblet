"""Logging configuration for Nimblet."""

import logging


def setup_logging(level: str) -> None:
    """Configure the root logger using ``logging.basicConfig``.

    Args:
        level: A logging level name such as ``"DEBUG"``, ``"INFO"``,
            ``"WARNING"``, ``"ERROR"``, or ``"CRITICAL"``.
    """
    level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(level=level, force=True)
