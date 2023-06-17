from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.base import Base  # Import the shared Base object
from src.database.FeedItem import FeedItem  # This must come after importing Base
from src.ingest.RSSFeed import RSSFeed

engine = create_engine('sqlite:///rss.sqlite.')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)  # This will now create tables for all models that inherit from Base

session = Session()

feed = RSSFeed('https://www.reddit.com/r/d100/.rss')
items = feed.get_items()

for item in items:  # Make sure to add items one by one, not the entire list
    session.add(item)
session.commit()
