import os
import feedparser
from .rss_writer import write_feed

def fetch_entries(subreddits):
    all_entries = []

    for subreddit in subreddits:
        url = f"https://www.reddit.com/r/{subreddit}/.rss"
        feed = feedparser.parse(url)
        all_entries.extend(feed.entries)

    return all_entries

def main():
    subreddits = ["python", "learnpython", "programming"]
    entries = fetch_entries(subreddits)

    # Use the data directory to write the feed file
    data_dir = os.getenv('DATA_DIR', '/app/data')
    feed_file = os.path.join(data_dir, 'my_feed.atom')

    write_feed(entries, feed_file)

if __name__ == "__main__":
    main()