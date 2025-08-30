from typing import List
from fastapi import APIRouter, HTTPException

from models.wishlist import WishlistItem
from services import wishlist_service

router = APIRouter(prefix="/users/{user_id}/wishlist", tags=["wishlist"])

@router.get("/", response_model=List[WishlistItem])
def read_wishlist(user_id: int):
    return wishlist_service.get_wishlist(user_id)

@router.post("/", response_model=WishlistItem, status_code=201)
def create_wishlist_item(user_id: int, item: WishlistItem):
    return wishlist_service.add_wishlist_item(user_id, item)

@router.delete("/", status_code=204)
def delete_wishlist_item(user_id: int, card_id: str):
    removed = wishlist_service.remove_wishlist_item(user_id, card_id)
    if not removed:
        raise HTTPException(status_code=404, detail="Item not found")
