from pydantic import BaseModel
from typing import Optional

class WishlistItem(BaseModel):
    card_id: str
    name: str
    set_name: str
    quantity: int = 1
    note: Optional[str] = None
