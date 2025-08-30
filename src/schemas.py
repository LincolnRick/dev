from pydantic import BaseModel


class CollectionItemBase(BaseModel):
    card_name: str
    quantity: int = 1


class CollectionItemCreate(CollectionItemBase):
    pass


class CollectionItemRead(CollectionItemBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
