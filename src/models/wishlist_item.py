from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class WishlistItem(Base):
    __tablename__ = "wishlist_items"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    desired_quantity = Column(Integer, default=1)

    card = relationship("Card", back_populates="wishlists")

