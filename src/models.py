from sqlalchemy import Column, Integer, String
from .database import Base


class CollectionItem(Base):
    __tablename__ = "collection_items"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    card_name = Column(String, nullable=False)
    quantity = Column(Integer, default=1)
