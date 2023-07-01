from werkzeug.security import generate_password_hash
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from src.database.base import Base

class User(UserMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    @classmethod
    def get(cls, username):
        return cls.query.filter_by(username=username).first()
