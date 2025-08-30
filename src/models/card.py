from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    set_id = Column(Integer, ForeignKey("sets.id"), nullable=False)
    card_number = Column(String)
    rarity = Column(String)
    card_type = Column(String)

    set = relationship("Set", back_populates="cards")
    collections = relationship("CollectionItem", back_populates="card")
    wishlists = relationship("WishlistItem", back_populates="card")

