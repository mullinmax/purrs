import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from src.database import Base, Item, ItemSource, User  # assuming models.py is your script file

# Setup a fixture to create a new database for each test
@pytest.fixture(scope='function')
def session():
    engine = create_engine('sqlite:///:memory:')  # Use an in-memory SQLite database for tests
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_create_item(session):
    item_source = ItemSource(name='Test Source', url='http://example.com', source_type='rss', auth='None')
    session.add(item_source)
    session.commit()

    # Note the change here - we're using datetime.strptime to parse the date string into a date object
    item = Item(source_id=item_source.item_source_id, title='Test Item', body='This is a test item', raw_xml='<item>This is a test item</item>', ingest_date=datetime.strptime('2023-06-01', '%Y-%m-%d').date(), seen=False, opened=False, liked=None)
    session.add(item)
    session.commit()

    assert item in session

def test_item_relationship(session):
    item_source = ItemSource(name='Test Source', url='http://example.com', source_type='rss', auth='None')
    session.add(item_source)
    session.commit()

    # Note the change here - we're using datetime.strptime to parse the date string into a date object
    item = Item(source_id=item_source.item_source_id, title='Test Item', body='This is a test item', raw_xml='<item>This is a test item</item>', ingest_date=datetime.strptime('2023-06-01', '%Y-%m-%d').date(), seen=False, opened=False, liked=None)
    session.add(item)
    session.commit()

    assert item.source == item_source


def test_create_user(session):
    user = User(name='Test User', hashed_password='hashedpassword', write=True, admin=False)
    session.add(user)
    session.commit()

    assert user in session