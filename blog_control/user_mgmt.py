# user 를 객체로 정의
from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = 'users'

    # user 를 정의하기 위한 column
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    # session 정보를 저장하기 위한 column
    session_ip = Column(String)
    pageName = Column(String)
    access_time = Column(DateTime)

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def get_id(self):
        return str(self.id)

    # db 에서 user id 를 통해서 user 찾기
    @staticmethod
    def get(user_id):
        pass

    # db 에서 user email 를 통해서 user 찾기
    @staticmethod
    def find(user_email):
        pass

    # db 에 새로운 user 를 생성
    @staticmethod
    def create(user_email, blog_id):
        pass

    # db 에서 user 를 제거
    @staticmethod
    def delete(user_id):
        pass
