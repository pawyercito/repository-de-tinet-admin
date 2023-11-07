from sqlalchemy.orm import Session
from app.repository.base_repository import BaseRepository

def get_db() -> Session:
    db = BaseRepository()
    try:
        yield db.session
    finally:
        db.session.close()
