from src.reddit_rss import fetch_entries

def test_fetch_entries():
    entries = fetch_entries(["learnpython"])
    assert len(entries) > 0
    for entry in entries:
        assert 'title' in entry
        assert 'link' in entry
