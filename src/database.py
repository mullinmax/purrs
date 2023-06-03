from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Item(Base):
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

class ItemSource(Base):
    __tablename__ = 'item_source'

    item_source_id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    source_type = Column(String)
    auth = Column(String)

    items = relationship('Item', backref='source')

class ItemScore(Base):
    __tablename__ = 'item_score'

    item_id = Column(Integer, ForeignKey('item.item_id'), primary_key=True)
    model_id = Column(Integer, ForeignKey('model.model_id'))
    score = Column(Float)
    confidence = Column(Float)

    item = relationship('Item', backref='scores')

class Model(Base):
    __tablename__ = 'model'

    model_id = Column(Integer, primary_key=True)
    train_date = Column(Date)
    tp = Column(Integer)
    fp = Column(Integer)
    tn = Column(Integer)
    fn = Column(Integer)
    weights = Column(String)

    scores = relationship('ItemScore', backref='model')

class VectorSource(Base):
    __tablename__ = 'vector_source'

    vector_source_id = Column(Integer, primary_key=True)

class Vector(Base):
    __tablename__ = 'vector'

    item_id = Column(Integer, ForeignKey('item.item_id'), primary_key=True)
    source_id = Column(Integer, ForeignKey('vector_source.vector_source_id'))

    item = relationship('Item', backref='vectors')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hashed_password = Column(String)
    write = Column(Boolean)
    admin = Column(Boolean)

# now you can create the database
from sqlalchemy import create_engine
engine = create_engine('sqlite:///purrs.db')
Base.metadata.create_all(engine)
