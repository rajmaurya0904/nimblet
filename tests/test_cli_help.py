"""Test that the CLI help output works."""

import subprocess
import sys


def test_cli_help_output() -> None:
    # Run the CLI module with --help via the Python interpreter
    result = subprocess.run(
        [sys.executable, "-m", "nimblet.cli", "--help"],
        capture_output=True,
        text=True,
    )
    # Exit code should be 0
    assert result.returncode == 0
    # The help output should contain the word "usage"
    assert "usage" in result.stdout.lower()

