# app.py

from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.base import Base  # Import the shared Base object
from src.database.FeedItem import FeedItem  # This must come after importing Base
from src.ingest.RSSFeed import RSSFeed

app = Flask(__name__)

engine = create_engine('sqlite:///rss.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def home():
    feed = RSSFeed('https://www.reddit.com/r/d100/.rss')
    items = feed.get_items()

    for item in items:  # Make sure to add items one by one, not the entire list
        session.add(item)
    session.commit()

    return render_template('index.html', items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

