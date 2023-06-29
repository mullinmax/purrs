import feedparser
from typing import List
from datetime import datetime
from dateutil.parser import parse

from src.item.generic import GenericItem

class RSSFeed:
    def __init__(self, url: str, id:int, last_pulled:datetime):
        self.url = url
        self.id = id
        self.feed = feedparser.parse(self.url)

    def get_items(self) -> List[GenericItem]:
        items = []
        for entry in self.feed.entries:
            try:
                published_datetime = parse(entry['published'])
            except ValueError:
                print(f"Warning: could not parse date: {entry['published']}")
                published_datetime = None
            item = GenericItem(
                url=entry['link'], 
                published_date=published_datetime,
                author=entry.get('author', ''),
                title=entry.get('title', ''),
                description=entry.get('description', ''),
                image=entry.get('media', {}).get('url')  # Image location can vary by feed, adjust as necessary
            )
            items.append(item)
        return items