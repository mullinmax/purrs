from unittest.mock import patch, call, MagicMock
from src.database.feed import FeedModel
from src.task.read_feeds import load_feed_configs, create_feeds_from_configs, read_feeds

@patch("src.task.read_feeds.get_db_session")
def test_load_feed_configs(mock_get_db_session):
    # Given
    mock_session = mock_get_db_session.return_value.__enter__.return_value
    mock_session.query.return_value.all.return_value = [
        FeedModel(id=1, url="http://example.com/rss", last_pulled=None),
        FeedModel(id=2, url="http://anotherexample.com/rss", last_pulled=None),
    ]

    # When
    result = load_feed_configs()

    # Then
    assert mock_get_db_session.called, "get_db_session was not called"
    assert mock_session.query.called, "session.query was not called"
    assert result == mock_session.query.return_value.all.return_value

@patch("src.task.read_feeds.RSSFeed")
def test_create_feeds_from_configs(mock_RSSFeed):
    # Given
    feed_configs = [
        FeedModel(id=1, url="http://example.com/rss", last_pulled=None),
        FeedModel(id=2, url="http://anotherexample.com/rss", last_pulled=None),
    ]

    # When
    result = create_feeds_from_configs(feed_configs)

    # Then
    assert mock_RSSFeed.call_count == len(feed_configs), f"RSSFeed was called {mock_RSSFeed.call_count} times, expected {len(feed_configs)}"
    assert result == [mock_RSSFeed.return_value] * len(feed_configs)
    for feed_config, feed_call in zip(feed_configs, mock_RSSFeed.call_args_list):
        expected_call = call(feed_config.url, feed_config.id, feed_config.last_pulled)
        assert feed_call == expected_call, f"RSSFeed was not called with {feed_config}"

@patch("src.task.read_feeds.load_feed_configs")
@patch("src.task.read_feeds.RSSFeed")
@patch("src.task.read_feeds.get_db_session")
def test_read_feeds(mock_get_db_session, mock_RSSFeed, mock_load_feed_configs):
    # Given
    mock_feed = MagicMock()
    mock_RSSFeed.return_value = mock_feed
    mock_load_feed_configs.return_value = [MagicMock(), MagicMock()] # list of config mock objects

    # When
    read_feeds()

    # Then
    assert mock_load_feed_configs.called, "load_feed_configs was not called"
    assert mock_RSSFeed.call_count == len(mock_load_feed_configs.return_value), "Not all feed configs were converted to feeds"
    assert mock_feed.save_items_to_db.called, "save_items_to_db was not called for all feeds"
    assert mock_get_db_session.called, "get_db_session was not called"

