import os
from dotenv import load_dotenv
from app.database.database import get_db
from sqlalchemy.orm import Session

load_dotenv()

class BaseRepository:
    def __init__(self, session):
        self.session : Session = session
        
