from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from core.config import setting

engine = create_engine(
    setting.DATABASE_URL
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    base.metadata.create_all(bind=engine)