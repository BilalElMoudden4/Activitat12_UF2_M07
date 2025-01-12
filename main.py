from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from connection import SessionLocal
from functs import create_record, read_records, read_record_by_id, update_record, delete_record
from models import User, Word, Attempt, Log, Alphabet
from schema import UserCreate, UserUpdate, WordCreate, WordUpdate

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD para usuarios
@app.post("/users/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_record(User, user, db)

@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return read_records(User, skip, limit, db)

@app.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return read_record_by_id(User, user_id, db)

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_record(User, user_id, user, db)

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_record(User, user_id, db)

# CRUD para palabras
@app.post("/words/")
async def create_word(word: WordCreate, db: Session = Depends(get_db)):
    return create_record(Word, word, db)

@app.get("/words/")
async def read_words(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return read_records(Word, skip, limit, db)

@app.get("/words/{word_id}")
async def read_word(word_id: int, db: Session = Depends(get_db)):
    return read_record_by_id(Word, word_id, db)

@app.put("/words/{word_id}")
async def update_word(word_id: int, word: WordUpdate, db: Session = Depends(get_db)):
    return update_record(Word, word_id, word, db)

@app.delete("/words/{word_id}")
async def delete_word(word_id: int, db: Session = Depends(get_db)):
    return delete_record(Word, word_id, db)
