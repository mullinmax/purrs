from datetime import datetime, timedelta
from src.feed.rss import RSSFeed
from src.database.feed import FeedModel
from src.database.session import get_db_session

def load_feed_configs():
    with get_db_session() as session:
        feed_configs = session.query(FeedModel).all()
    return feed_configs

def create_feeds_from_configs(feed_configs):
    return [RSSFeed(config.url, config.id, config.last_pulled, config.cron_expression) for config in feed_configs]

def read_feeds():
    print('reading feeds')
    feed_configs = load_feed_configs()
    feeds = create_feeds_from_configs(feed_configs)
    for feed in feeds:
        # Only update the feed if the last pull time + pull interval is earlier than the current time
        if feed.last_pulled is None or feed.last_pulled + timedelta(seconds=feed.pull_every_n_seconds) < datetime.now():
            feed.save_items_to_db()
