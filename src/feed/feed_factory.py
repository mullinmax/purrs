from srd.feed.rss import RSSFeed
from srd.feed.reddit import RedditFeed

def feed_factory(url):
    # If not an RSS feed error
    if 'reddit.com' in url:
        return RedditFeed(url)
    else:
        return RSSFeed(url)