'''
Contains database session and engine.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from core.config import get_settings

SQLALCHEMY_DATABASE_URL = get_settings().MYSQL_DB_URL

engine = create_engine(url=SQLALCHEMY_DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
