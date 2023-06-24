import feedparser
from typing import List
import datetime
from dateutil.parser import parse

from src.item.reddit import ReditItem

class RedditFeed(RSSFeed):
    def __init__(self, url: str) -> None:
        super().__init__(url)

    def get_items(self) -> List[GenericItem]:
        items = []
        for entry in self.feed.entries:
            try:
                published_datetime = parse(entry['published'])
            except ValueError:
                print(f"Warning: could not parse date: {entry['published']}")
                published_datetime = None

            item = RedditItem(
                url=entry['link'], 
                published_date=published_datetime,
                author=entry.get('author', ''),
                title=entry.get('title', ''),
                description=entry.get('description', ''),
                image=entry.get('media', {}).get('url')
            )
            items.append(item)
        return items