"""Command line interface for Nimblet.

Provides a simple entry point that displays usage information.
"""

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="nimblet-monitor",
        description="Nimblet background clipboard monitor",
    )
    # No subcommands for now; placeholder for future extensions.
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    # Parse args; argparse will handle --help automatically.
    parser.parse_args(argv)
    # If we get here, no action was taken; just exit successfully.
    return 0


if __name__ == "__main__":
    sys.exit(main())
