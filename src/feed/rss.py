import feedparser
from typing import List
from datetime import datetime
from dateutil.parser import parse

from src.item.generic import GenericItem

class RSSFeed:
    def __init__(self, url: str, id: int, last_pulled: datetime):
        self.url = url
        self.id = id
        self._feed = None

    @property
    def feed(self):
        if self._feed is None:
            self._feed = feedparser.parse(self.url)
        return self._feed

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

    def save_items_to_db(self, session):
        items = self.get_items()
        for item in items:
            item.save_to_db(session)