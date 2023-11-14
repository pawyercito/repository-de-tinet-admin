import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

class BaseRepository:
    def __init__(self, session):
        self.session = session
