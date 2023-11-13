import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

class BaseRepository:
    def __init__(self, Session):
        driver = os.getenv('EXP_I3_QA_DRIVER')
        host = os.getenv('EXP_I3_QA_HOST')
        port = os.getenv('EXP_I3_QA_PORT')
        database = os.getenv('EXP_I3_QA_DATABASE')
        username = os.getenv('EXP_I3_QA_UID')
        password = os.getenv('EXP_I3_QA_PWD')

        connection_string = f'mssql+pyodbc://{username}:{password}@{host}:{port}/{database}?driver={driver}'
        
        engine = create_engine(connection_string)
        Session = sessionmaker(bind=engine)
        self.session = Session()
