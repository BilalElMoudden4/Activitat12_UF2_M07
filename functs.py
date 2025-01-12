from sqlalchemy.orm import Session
from models import User, Word, Attempt, Log, Alphabet
from schema import UserCreate, WordCreate, UserUpdate, WordUpdate


# Helper para crear un registro
def create_record(model, data, db: Session):
    new_record = model(**data.dict())
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record


# Helper para leer todos los registros
def read_records(model, skip: int, limit: int, db: Session):
    return db.query(model).offset(skip).limit(limit).all()


# Helper para leer un registro por ID
def read_record_by_id(model, record_id, db: Session):
    return db.query(model).filter(model.id == record_id).first()


# Helper para actualizar un registro
def update_record(model, record_id, data, db: Session):
    record = db.query(model).filter(model.id == record_id).first()
    if not record:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(record, key, value)
    db.commit()
    db.refresh(record)
    return record


# Helper para eliminar un registro
def delete_record(model, record_id, db: Session):
    record = db.query(model).filter(model.id == record_id).first()
    if not record:
        return None
    db.delete(record)
    db.commit()
    return {"message": f"{model.__name__} deleted successfully"}
