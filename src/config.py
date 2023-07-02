import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE = os.getenv("DATABASE")
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE}'
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
