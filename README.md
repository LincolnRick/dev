# dev

Utilities for syncing TCG card information from the Scryfall API.

## Usage

Initial import of all sets and cards:

```bash
python scripts/sync_cards.py
```

Update existing data with newly released sets:

```bash
python scripts/sync_cards.py --update
```

Limit operations to specific set codes:

```bash
python scripts/sync_cards.py --sets khm neo
```
