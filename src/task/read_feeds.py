from src.feed.rss import RSSFeed
from src.database.feed import FeedModel
from src.database.session import get_db_session

def read_feeds():
    print('reading feeds')
    # load feed configs from database
    with get_db_session() as session:
        feed_configs = session.query(FeedModel).all()
        print(f'feed configs: {str(feed_configs)}')
        feeds = [RSSFeed(config.id, config.url, config.last_pulled) for config in feed_configs]
        print(f'feeds: {feeds}')
    # for each feed
    for feed in feeds:
        items = feed.get_items()
        print(f'items from feed {feed.id}: {items}')
        with get_db_session() as session:
            for item in items:
                print('saving item')
                print(item)
                item.save_to_db(session)
                print('item saved')
