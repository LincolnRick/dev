from typing import Dict, List
from models.wishlist import WishlistItem

# Simple in-memory storage for demonstration purposes
_wishlists: Dict[int, List[WishlistItem]] = {}

def get_wishlist(user_id: int) -> List[WishlistItem]:
    return _wishlists.get(user_id, [])

def add_wishlist_item(user_id: int, item: WishlistItem) -> WishlistItem:
    wishlist = _wishlists.setdefault(user_id, [])
    wishlist.append(item)
    return item

def remove_wishlist_item(user_id: int, card_id: str) -> bool:
    wishlist = _wishlists.get(user_id, [])
    new_wishlist = [i for i in wishlist if i.card_id != card_id]
    if len(new_wishlist) == len(wishlist):
        return False
    _wishlists[user_id] = new_wishlist
    return True
