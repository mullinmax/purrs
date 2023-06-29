from src.feed.rss import RSSFeed
from src.database.feed import FeedModel
from src.database.session import get_db_session

def read_feeds():
    # load feed configs from database
    with get_db_session() as session:
        feed_configs = session.query(FeedModel).all()
        feeds = [RSSFeed(config.id, config.url, config.last_pulled) for config in feed_configs]

    # for each feed
    for feed in feeds:
        items = feed.get_items()
        for item in items:
            with get_db_session() as session:
                item.save_to_db(session)
