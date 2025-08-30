import httpx

API_BASE = "https://api.scryfall.com"

async def list_sets():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{API_BASE}/sets")
        resp.raise_for_status()
        return resp.json()

async def get_set(set_id: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{API_BASE}/sets/{set_id}")
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.json()
