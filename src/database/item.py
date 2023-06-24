from sqlalchemy import Column, Integer, String, DateTime, Text
from .base import Base 

class ItemModel(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    short_url = Column(String)
    title = Column(String)
    description = Column(String)
    image = Column(String)