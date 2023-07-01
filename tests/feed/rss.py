from unittest.mock import Mock, patch
from src.feed.rss import RSSFeed

@patch("src.item.generic.GenericItem")
def test_save_items_to_db(mock_GenericItem):
    # Given
    mock_session = Mock()
    mock_item = Mock()
    mock_GenericItem.return_value = mock_item
    feed = RSSFeed("http://example.com/rss", 1, None)
    feed.get_items = Mock(return_value=[mock_item, mock_item])

    # When
    feed.save_items_to_db(mock_session)

    # Then
    assert feed.get_items.call_count == 1
    assert mock_item.save_to_db.call_count == 2
    mock_item.save_to_db.assert_called_with(mock_session)
