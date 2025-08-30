from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from . import Base


class Set(Base):
    __tablename__ = "sets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
    release_date = Column(Date)

    cards = relationship("Card", back_populates="set")

