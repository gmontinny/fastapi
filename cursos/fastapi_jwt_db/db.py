from pydantic import PostgresDsn
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import engine
from sqlalchemy.orm import sessionmaker

from config import setting

database_url = PostgresDsn.build(
    scheme="postgresql",
    user=setting.db_usr,
    password=setting.db_pwd,
    host=setting.db_host,
    path=f"/{setting.db_name}",
)

SQLALCHEMY_DATABASE_URL = str(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()