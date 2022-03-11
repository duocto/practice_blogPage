# user 를 객체로 정의
from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String
engine = create_engine( "mysql+pymysql://root:@localhost:3306/blog_db", echo=True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

