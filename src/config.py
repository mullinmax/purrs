class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE = 'purrs.sqlite'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE}'
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
