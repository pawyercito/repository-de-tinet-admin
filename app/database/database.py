from sqlalchemy.orm import Session
from app.repository.base_repository import BaseRepository

def get_db() -> Session:
    db = BaseRepository(Session)  # Pass Session as an argument
    try:
        yield db.session
    finally:
        db.session.close()
