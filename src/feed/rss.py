import feedparser
from typing import List
from datetime import datetime
from dateutil.parser import parse
from croniter import croniter

from src.item.generic import GenericItem
from src.database.session import get_db_session
from src.database.feed import FeedModel

def is_valid_cron_expression(cron_expression):
    try:
        croniter(cron_expression, datetime.now())
        return True
    except CroniterBadCronError:
        return False

class RSSFeed:
    def __init__(self, url: str, id: int, last_pulled: datetime, cron_expression: str):
        self.url = url
        self.id = id
        self.last_pulled = last_pulled
        self.cron_expression = cron_expression
        if not is_valid_cron_expression(cron_expression):
            raise ValueError("Invalid cron expression")
        self._feed = None

    @property
    def feed(self):
        if self._feed is None:
            self._feed = feedparser.parse(self.url)
        return self._feed

    def should_update(self):
        if self.last_pulled is None:
            return True

        cron_schedule = croniter(self.cron_expression, self.last_pulled)
        next_update_time = cron_schedule.get_next(datetime)

        return datetime.now() >= next_update_time

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

    def save_items_to_db(self):
        if self.should_update():
            with get_db_session() as session:
                items = self.get_items()
                for item in items:
                    item.save_to_db(session)

                feed_model = session.query(FeedModel).filter(FeedModel.id == self.id).first()
                if feed_model:
                    feed_model.last_pulled = datetime.now()
                    session.commit()