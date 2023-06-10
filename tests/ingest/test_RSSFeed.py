import pytest
from unittest.mock import patch, MagicMock
from src.ingest.RSSFeed import RSSFeed
from src.database import FeedItem  

@pytest.fixture
def mock_feedparser():
    with patch('feedparser.parse') as mock_feedparser:
        yield mock_feedparser

def test_get_items(mock_feedparser):
    mock_feed = MagicMock()
    mock_feed.entries = [
        {
            'title': 'Test Title',
            'link': 'http://test.com',
            'published': 'Fri, 09 Jun 2023 10:00:00 GMT',
            'description': 'Test Description',
            'author': 'Test Author',
            'id': 'Test GUID'
        }
    ]
    mock_feedparser.parse.return_value = mock_feed

    rss = RSSFeed('http://test.com/rss')
    items = rss.get_items()

    assert len(items) == 1
    item = items[0]
    assert isinstance(item, FeedItem)
    assert item.title == 'Test Title'
    assert item.link == 'http://test.com'
    assert item.published.year == 2023
    assert item.published.month == 6
    assert item.published.day == 9
    assert item.description == 'Test Description'
    assert item.author == 'Test Author'
    assert item.guid == 'Test GUID'
