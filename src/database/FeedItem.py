from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FeedItem(Base):
    """
    A class used to represent an item in an RSS Feed, as a database table

    ...

    Attributes
    ----------
    id : int
        the primary key of the FeedItem
    title : str
        the title of the FeedItem
    link : str
        the link of the FeedItem
    published : datetime
        the published date of the FeedItem
    description : str
        the description of the FeedItem
    author : str
        the author of the FeedItem
    guid : str
        the unique identifier of the FeedItem

    """
    __tablename__ = 'feed_items'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String)
    published = Column(DateTime)
    description = Column(Text)
    author = Column(String)
    guid = Column(String)

# Example usage:
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine('sqlite:///rss.db')
# Session = sessionmaker(bind=engine)
#
# Base.metadata.create_all(engine)
#
# session = Session()
# new_item = FeedItem(title='Example Title', link='http://example.com', published='2023-06-09 12:00:00',
#                     description='Example Description', author='Example Author', guid='Example GUID')
# session.add(new_item)
# session.commit()
