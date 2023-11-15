from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv

load_dotenv()


from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv

load_dotenv()

def get_db():
    driver = os.getenv('EXP_I3_QA_DRIVER')
    host = os.getenv('EXP_I3_QA_HOST')
    port = os.getenv('EXP_I3_QA_PORT')
    database = os.getenv('EXP_I3_QA_DATABASE')
    username = os.getenv('EXP_I3_QA_UID')
    password = os.getenv('EXP_I3_QA_PWD')

    connection_string = f'mssql+pyodbc://{username}:{password}@{host}:{port}/{database}?driver={driver}'
    
    engine = create_engine(connection_string, echo=True)
    Session = sessionmaker(bind=engine)

    # Use the context manager to manage the database session
    with Session() as db:
        try:
            yield db
            db.commit()  # Commit changes after the yield
        except Exception as e:
            db.rollback()  # Rollback changes in case of an exception
            raise e
        finally:
            db.close()
