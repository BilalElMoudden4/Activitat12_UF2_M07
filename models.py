from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    total_points = Column(Integer, default=0)
    total_games = Column(Integer, default=0)
    games_won = Column(Integer, default=0)
    best_game_points = Column(Integer, default=0)
    best_game_date = Column(TIMESTAMP)

class Word(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String(50), nullable=False)
    theme = Column(String(50), nullable=False)

class Attempt(Base):
    __tablename__ = "attempts"
    id = Column(Integer, primary_key=True, index=True)
    log_id = Column(Integer, ForeignKey("logs.id"), nullable=False)
    letter = Column(String(1), nullable=False)
    is_correct = Column(Boolean, nullable=False)
    attempt_number = Column(Integer, nullable=False)

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)
    points = Column(Integer, default=0)
    user = relationship("User")

class Alphabet(Base):
    __tablename__ = "alphabet"
    id = Column(Integer, primary_key=True, index=True)
    letter = Column(String(1), nullable=False)
    lang = Column(String(20), nullable=False)
