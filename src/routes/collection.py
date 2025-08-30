from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import schemas
from ..services import collection_service

router = APIRouter(prefix="/users/{user_id}/collection", tags=["collection"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.CollectionItemRead])
def read_collection(user_id: int, db: Session = Depends(get_db)):
    return collection_service.get_user_collection(db, user_id)


@router.post("/", response_model=schemas.CollectionItemRead, status_code=201)
def create_collection_item(
    user_id: int, item: schemas.CollectionItemCreate, db: Session = Depends(get_db)
):
    return collection_service.add_collection_item(db, user_id, item)


@router.delete("/", status_code=204)
def delete_collection_item(
    user_id: int, item_id: int, db: Session = Depends(get_db)
):
    item = collection_service.delete_collection_item(db, user_id, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
