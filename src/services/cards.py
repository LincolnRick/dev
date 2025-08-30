import httpx

API_BASE = "https://api.scryfall.com"

async def list_cards(query: str = "*", page: int = 1):
    params = {"q": query, "page": page}
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{API_BASE}/cards/search", params=params)
        resp.raise_for_status()
        return resp.json()

async def get_card(card_id: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{API_BASE}/cards/{card_id}")
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.json()
