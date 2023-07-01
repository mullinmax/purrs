from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from contextlib import contextmanager
from werkzeug.security import generate_password_hash

from src.config import Config
from src.database.base import Base
from src.database.user import User

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = scoped_session(sessionmaker(bind=engine))

def init_db():
    Base.metadata.create_all(engine)
    create_admin_user()

def create_admin_user():
    session = Session()
    
    password = Config.ADMIN_PASSWORD
    username = 'admin'
    # Only create an admin if username and password are both set
    if username and password:
        admin = session.query(User).filter_by(username=username).first()

        if admin:
            session.delete(admin)
            session.commit()

        admin = User(username=username, password=password)
        session.add(admin)
        session.commit()

    session.close()

@contextmanager
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
