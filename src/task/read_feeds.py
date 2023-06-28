from src.feed.rss import RSSFeed
from src.database.feed import FeedModel

def read_feeds(sqlalchemy_session):
    # load feed configs from database
    feed_configs = sqlalchemy_session.query(FeedModel).all()
    feeds = [RSSFeed(config.id, config.url, config.last_pulled) for config in feed_configs]
    # for each feed
    for feed in feeds:
        items = feed.get_items()
        for item in items:
            item.save_to_db(sqlalchemy_session)
    