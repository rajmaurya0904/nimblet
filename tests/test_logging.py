"""Test logging configuration."""

import logging

from nimblet.logging import setup_logging


def test_setup_logging_debug() -> None:
    """Verify that setup_logging('DEBUG') sets root logger level to DEBUG."""
    setup_logging("DEBUG")
    assert logging.getLogger().level == logging.DEBUG


def test_setup_logging_info() -> None:
    """Verify that setup_logging('INFO') sets root logger level to INFO."""
    setup_logging("INFO")
    assert logging.getLogger().level == logging.INFO


def test_setup_logging_warning() -> None:
    """Verify that setup_logging('WARNING') sets root logger level to WARNING."""
    setup_logging("WARNING")
    assert logging.getLogger().level == logging.WARNING


def test_setup_logging_error() -> None:
    """Verify that setup_logging('ERROR') sets root logger level to ERROR."""
    setup_logging("ERROR")
    assert logging.getLogger().level == logging.ERROR


def test_setup_logging_critical() -> None:
    """Verify that setup_logging('CRITICAL') sets root logger level to CRITICAL."""
    setup_logging("CRITICAL")
    assert logging.getLogger().level == logging.CRITICAL