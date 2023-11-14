import os
from dotenv import load_dotenv
from app.database.database import get_db

load_dotenv()

class BaseRepository:
    def __init__(self, db):
        self.session = next(get_db())
        self.db = db
