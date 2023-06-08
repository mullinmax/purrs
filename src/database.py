"""
Module for database models used in the application.
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey  
from sqlalchemy.orm import relationship  
from sqlalchemy.orm import declarative_base  

Base = declarative_base()  

class Item(Base):  
    """
    Represents an Item in the database.
    """
    __tablename__ = 'item'  

    item_id = Column(Integer, primary_key=True)  
    source_id = Column(Integer, ForeignKey('item_source.item_source_id'))  
    title = Column(String)  
    body = Column(String)  
    raw_xml = Column(String)  
    ingest_date = Column(Date)  
    seen = Column(Boolean)  
    opened = Column(Boolean)  
    liked = Column(Boolean)  

    def __repr__(self):
        return f"<Item(id={self.item_id}, title={self.title})>"

class ItemSource(Base):  
    """
    Represents an ItemSource in the database.
    """
    __tablename__ = 'item_source'  

    item_source_id = Column(Integer, primary_key=True)  
    name = Column(String)  
    url = Column(String)  
    source_type = Column(String)  
    auth = Column(String)  

    items = relationship('Item', backref='source')

    def __repr__(self):
        return f"<ItemSource(id={self.item_source_id}, name={self.name})>"

class ItemScore(Base):  
    """
    Represents an ItemScore in the database.
    """
    __tablename__ = 'item_score'  

    item_id = Column(Integer, ForeignKey('item.item_id'), primary_key=True)  
    model_id = Column(Integer, ForeignKey('model.model_id'))  
    score = Column(Float)  
    confidence = Column(Float)  

    item = relationship('Item', backref='scores') 

    def __repr__(self):
        return f"<ItemScore(item_id={self.item_id}, model_id={self.model_id}, score={self.score})>"

class Model(Base):  
    """
    Represents a Model in the database.
    """
    __tablename__ = 'model'  

    model_id = Column(Integer, primary_key=True)  
    train_date = Column(Date)  
    tp = Column(Integer)  
    fp = Column(Integer)  
    tn = Column(Integer)  
    fn = Column(Integer)  
    weights = Column(String)  

    scores = relationship('ItemScore', backref='model')  

    def __repr__(self):
        return f"<Model(id={self.model_id}, train_date={self.train_date})>"

class VectorSource(Base):  
    """
    Represents a VectorSource in the database.
    """
    __tablename__ = 'vector_source'  

    vector_source_id = Column(Integer, primary_key=True)  

    def __repr__(self):
        return f"<VectorSource(id={self.vector_source_id})>"

class Vector(Base):  
    """
    Represents a Vector in the database.
    """
    __tablename__ = 'vector'  

    item_id = Column(Integer, ForeignKey('item.item_id'), primary_key=True)  
    source_id = Column(Integer, ForeignKey('vector_source.vector_source_id'))  

    item = relationship('Item', backref='vectors')

    def __repr__(self):
        return f"<Vector(item_id={selfitem_id}, source_id={self.source_id})>"

class User(Base):  
    """
    Represents a User in the database.
    """
    __tablename__ = 'users'  

    id = Column(Integer, primary_key=True)  
    name = Column(String)  
    hashed_password = Column(String)  
    write = Column(Boolean)  
    admin = Column(Boolean)  

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"
