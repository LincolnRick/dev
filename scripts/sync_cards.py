#!/usr/bin/env python3
"""Command line utility for syncing TCG card data."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Ensure repository root is on sys.path for importing from ``src``
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.services.sync_cards import initial_import, update


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync card data from Scryfall")
    parser.add_argument(
        "--update",
        action="store_true",
        help="Run update routine instead of initial import",
    )
    parser.add_argument(
        "--sets",
        nargs="*",
        help="Optional list of set codes to import/update",
    )
    parser.add_argument(
        "--output",
        default="data",
        help="Directory where JSON files will be stored",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.update:
        new_sets = update(output_dir=args.output, set_codes=args.sets)
        print(f"Updated. {len(new_sets)} new sets imported.")
    else:
        initial_import(output_dir=args.output, set_codes=args.sets)
        print("Initial import complete.")


if __name__ == "__main__":
    main()
