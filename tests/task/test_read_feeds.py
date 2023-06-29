import pytest
from unittest.mock import MagicMock
from src.feed.rss import RSSFeed
from src.database.feed import FeedModel
from src.database.session import get_db_session, Session
from src.task.read_feeds import read_feeds

def test_read_feeds(mocker, tmpdir):
    # Mock RSSFeed
    mock_RSSFeed = mocker.patch('src.feed.rss.RSSFeed', autospec=True)
    
    # Mock get_db_session
    mock_get_db_session = mocker.patch('src.database.session.get_db_session', autospec=True)
    
    # Setup
    mock_session = mock_get_db_session.return_value.__enter__.return_value
    mock_feed_config = MagicMock(spec=FeedModel)
    mock_feed_config.id = 1
    mock_feed_config.url = 'http://example.com/feed'
    mock_feed_config.last_pulled = None
    mock_session.query.return_value.all.return_value = [mock_feed_config]

    mock_feed = mock_RSSFeed.return_value
    mock_item = MagicMock()
    mock_item.save_to_db = MagicMock()
    mock_feed.get_items.return_value = [mock_item]

    # Call function
    read_feeds()

    # Assert calls were made correctly
    mock_get_db_session.assert_called()
    mock_session.query.assert_called_with(FeedModel)
    mock_session.query.return_value.all.assert_called()
    mock_RSSFeed.assert_called_with(mock_feed_config.id, mock_feed_config.url, mock_feed_config.last_pulled)
    mock_feed.get_items.assert_called()
    mock_item.save_to_db.assert_called_with(mock_session)
