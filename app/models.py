from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True, unique=True)
    email = Column(String(50), unique=True, index=True)
    hashedPassword = Column(String(500))
    firstName = Column(String(30))
    lastName = Column(String(30))
