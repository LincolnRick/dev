"""Service for syncing TCG card data from external API.

Provides functions to perform an initial import of all sets and cards
from the Scryfall API and to update the local data when new sets are
released.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List, Dict

import requests

API_BASE = "https://api.scryfall.com"


def fetch_all_sets() -> List[Dict]:
    """Return metadata for all available card sets."""
    resp = requests.get(f"{API_BASE}/sets")
    resp.raise_for_status()
    data = resp.json()
    return data.get("data", [])


def fetch_cards_in_set(set_code: str) -> List[Dict]:
    """Fetch all cards for a given set code."""
    cards: List[Dict] = []
    page = 1
    while True:
        resp = requests.get(
            f"{API_BASE}/cards/search",
            params={"q": f"set:{set_code}", "page": page},
        )
        resp.raise_for_status()
        payload = resp.json()
        cards.extend(payload.get("data", []))
        if payload.get("has_more"):
            page += 1
        else:
            break
    return cards


def _save_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)


def initial_import(output_dir: str = "data", set_codes: Iterable[str] | None = None) -> None:
    """Perform the initial import of sets and cards.

    Args:
        output_dir: Directory where JSON files will be stored.
        set_codes: Optional iterable of set codes to restrict the import.
            If omitted, all sets are imported.
    """
    sets = fetch_all_sets()
    if set_codes:
        set_codes = set(set_codes)
        sets = [s for s in sets if s.get("code") in set_codes]
    _save_json(Path(output_dir) / "sets.json", sets)
    for s in sets:
        code = s.get("code")
        cards = fetch_cards_in_set(code)
        _save_json(Path(output_dir) / f"cards_{code}.json", cards)


def update(output_dir: str = "data", set_codes: Iterable[str] | None = None) -> List[Dict]:
    """Update local data with newly released sets.

    Returns a list of newly imported sets.
    """
    sets_file = Path(output_dir) / "sets.json"
    existing_sets: Dict[str, Dict] = {}
    if sets_file.exists():
        with sets_file.open("r", encoding="utf-8") as fh:
            existing_sets = {s["code"]: s for s in json.load(fh)}
    sets = fetch_all_sets()
    if set_codes:
        set_codes = set(set_codes)
        sets = [s for s in sets if s.get("code") in set_codes]
    new_sets = [s for s in sets if s.get("code") not in existing_sets]
    if new_sets:
        _save_json(sets_file, sets)
        for s in new_sets:
            code = s.get("code")
            cards = fetch_cards_in_set(code)
            _save_json(Path(output_dir) / f"cards_{code}.json", cards)
    return new_sets
