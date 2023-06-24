from sqlalchemy import Column, Integer, String, DateTime, Text
from .base import Base 

class FeedModel(Base):
    __tablename__ = 'feed'

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    last_pulled = Column(DateTime)
    