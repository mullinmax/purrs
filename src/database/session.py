import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Default to sqlite if DATABASE_URI is not set
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///purrs.sqlite') 
engine = create_engine(DATABASE_URI)
db_session = sessionmaker(bind=engine)
