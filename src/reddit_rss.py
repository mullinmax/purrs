"""
This module provides functionality for fetching RSS feeds from Reddit.
"""

import os
import feedparser
from .rss_writer import write_feed


def fetch_entries(subreddits):
    """
    Fetches entries from specified subreddits.
    
    Args:
        subreddits (list): List of subreddit names.

    Returns:
        list: A list of entries from the subreddits.
    """
    all_entries = []

    for subreddit in subreddits:
        url = f"https://www.reddit.com/r/{subreddit}/.rss"
        feed = feedparser.parse(url)
        all_entries.extend(feed.entries)

    return all_entries


def main():
    """
    Main function for fetching and writing entries from subreddits to a feed file.
    """
    subreddits = ["python", "learnpython", "programming"]
    entries = fetch_entries(subreddits)

    # Use the data directory to write the feed file
    data_dir = os.getenv('DATA_DIR', '/app/data')
    feed_file = os.path.join(data_dir, 'my_feed.atom')

    write_feed(entries, feed_file)


if __name__ == "__main__":
    main()
