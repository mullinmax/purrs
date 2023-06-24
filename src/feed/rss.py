import feedparser
from typing import List
import datetime
from dateutil.parser import parse

from src.item.url import URLItem

class RSSFeed:
    def __init__(self, url: str) -> None:
        self.url = url
        self.feed = feedparser.parse(self.url)

    def get_items(self) -> List[FeedItem]:
        items = []
        for entry in self.feed.entries:
            try:
                published_datetime = parse(entry['published'])
            except ValueError:
                print(f"Warning: could not parse date: {entry['published']}")
                published_datetime = None  # or some default value
            item = FeedItem(
                title=entry['title'], 
                link=entry['link'], 
                published=published_datetime,
                description=entry.get('description', ''),  # Use dict.get to handle optional fields
                author=entry.get('author', ''),
                guid=entry.get('id', '')
            )
            items.append(item)
        return items
