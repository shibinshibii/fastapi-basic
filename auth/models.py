from database import Base
from sqlalchemy import Column, String,Integer

class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True)
    access_token = Column(String)
    token_type = Column(String)

class TokenData(Base):
    __tablename__ = "tokendatas"
    id = Column(Integer,primary_key=True)
    email = Column(String)