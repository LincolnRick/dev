from fastapi import APIRouter, HTTPException

# Import the card service using an absolute import.  The previous relative
# import attempted to traverse beyond the top-level package when the module
# was imported as part of the application start-up, leading to an
# ``ImportError``.  Using an absolute import keeps the module usable both when
# running the app and during test collection.
from services import cards as cards_service

router = APIRouter(prefix="/cards", tags=["cards"])

@router.get("/", summary="List cards")
async def list_cards():
    return await cards_service.list_cards()

@router.get("/{card_id}", summary="Get card by ID")
async def get_card(card_id: str):
    data = await cards_service.get_card(card_id)
    if not data:
        raise HTTPException(status_code=404, detail="Card not found")
    return data
