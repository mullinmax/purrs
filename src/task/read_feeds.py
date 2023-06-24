from src.feed.rss import RSSFeed

def read_feeds(db):
    print('''
    
    READING FEEDS
    
    ''')
    # load feed configs from database
    feeds = [RSSFeed("https://www.reddit.com/r/StarWarsSquadrons/.rss")] # we're going to pretend we're loading this from the DB for now
    # for each feed
    for feed in feeds:
        items = feed.get_items()
        for item in items:
            print(item)
            item.save_to_db(db)
    