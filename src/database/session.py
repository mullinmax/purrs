import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from contextlib import contextmanager

# Default to sqlite if DATABASE_URI is not set
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///purrs.sqlite') 
engine = create_engine(DATABASE_URI)
Session = scoped_session(sessionmaker(bind=engine))

@contextmanager
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
