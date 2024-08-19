from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from trino.auth import BasicAuthentication

from settings import Settings

settings = Settings()

SQLALCHEMY_DATABASE_URL = f"""trino://{settings.USER}:{settings.PASSWORD}@{settings.HOST}:{settings.PORT}/{settings.CATALOG}/{settings.SCHEMA}"""

engine = create_engine(SQLALCHEMY_DATABASE_URL,
   connect_args={
       "auth": BasicAuthentication(settings.USER, settings.PASSWORD),
       "http_scheme": "https",
})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
