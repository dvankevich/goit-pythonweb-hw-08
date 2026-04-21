from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.contact import Contact
from src.schemas.contact import ContactCreate


def get_all(db: Session):
    return db.scalars(select(Contact)).all()


def get_by_id(db: Session, contact_id: int):
    return db.get(Contact, contact_id)


def create(db: Session, contact_data: ContactCreate):
    db_contact = Contact(**contact_data.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def delete(db: Session, contact_id: int) -> bool:
    contact = get_by_id(db, contact_id)
    if contact:
        db.delete(contact)
        db.commit()
        return True
    return False
