from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    total_points: Optional[int] = 0
    total_games: Optional[int] = 0
    games_won: Optional[int] = 0
    best_game_points: Optional[int] = 0
    best_game_date: Optional[str] = None

class UserUpdate(BaseModel):
    username: Optional[str]
    total_points: Optional[int]
    total_games: Optional[int]
    games_won: Optional[int]
    best_game_points: Optional[int]
    best_game_date: Optional[str]

class WordCreate(BaseModel):
    word: str
    theme: str

class WordUpdate(BaseModel):
    word: Optional[str]
    theme: Optional[str]
