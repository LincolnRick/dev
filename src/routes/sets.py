from fastapi import APIRouter, HTTPException

# Similar to the cards route, use an absolute import for the service layer to
# avoid issues when the module is imported as part of the application
# initialisation.
from services import sets as sets_service

router = APIRouter(prefix="/sets", tags=["sets"])

@router.get("/", summary="List all sets")
async def list_sets():
    return await sets_service.list_sets()

@router.get("/{set_id}", summary="Get set by ID")
async def get_set(set_id: str):
    data = await sets_service.get_set(set_id)
    if not data:
        raise HTTPException(status_code=404, detail="Set not found")
    return data
