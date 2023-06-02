import feedparser

def fetch_entries(subreddits):
    all_entries = []

    for subreddit in subreddits:
        url = f"https://www.reddit.com/r/{subreddit}/.rss"
        feed = feedparser.parse(url)
        all_entries.extend(feed.entries)

    return all_entries
