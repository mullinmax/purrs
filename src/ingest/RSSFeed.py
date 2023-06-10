import feedparser
from typing import List
import datetime

from ..database.FeedItem import FeedItem

class RSSFeed:
    """
    A class used to represent and interact with an RSS Feed

    ...

    Attributes
    ----------
    url : str
        a string holding the URL of the RSS Feed
    feed : feedparser.FeedParserDict
        the parsed RSS Feed

    Methods
    -------
    get_items() -> List[FeedItem]:
        Returns the items/entries in the RSS Feed as a list of FeedItem objects
    """
    def __init__(self, url: str) -> None:
        """
        Constructs all the necessary attributes for the RSSFeed object.

        Parameters
        ----------
            url : str
                the URL of the RSS Feed
        """
        self.url = url
        self.feed = feedparser.parse(self.url)

    def get_items(self) -> List[FeedItem]:
        """
        Returns the items/entries in the RSS Feed as a list of FeedItem objects

        Returns
        -------
        list
            a list of FeedItem objects, each representing an item/entry in the RSS Feed
        """
        items = []
        for entry in self.feed.entries:
            published_datetime = datetime.datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')
            item = FeedItem(
                title=entry.title, 
                link=entry.link, 
                published=published_datetime,
                description=entry.get('description', ''),  # Use dict.get to handle optional fields
                author=entry.get('author', ''),
                guid=entry.get('id', '')
            )
            items.append(item)
        return items
