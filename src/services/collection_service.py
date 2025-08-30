from sqlalchemy.orm import Session

from .. import models, schemas


def get_user_collection(db: Session, user_id: int):
    return (
        db.query(models.CollectionItem)
        .filter(models.CollectionItem.user_id == user_id)
        .all()
    )


def add_collection_item(db: Session, user_id: int, item: schemas.CollectionItemCreate):
    db_item = models.CollectionItem(**item.dict(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_collection_item(db: Session, user_id: int, item_id: int):
    db_item = (
        db.query(models.CollectionItem)
        .filter(
            models.CollectionItem.user_id == user_id,
            models.CollectionItem.id == item_id,
        )
        .first()
    )
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
