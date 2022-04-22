from flask_login import UserMixin, user_accessed
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import pymysql



Base = declarative_base()

engine = create_engine("mysql+pymysql://root:password@localhost:3306/blog_db", echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class User(Base, UserMixin):
    __tablename__ = 'users'

    # user 를 정의하기 위한 column
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)

    # session 정보를 저장하기 위한 column
    session_ip = Column(String)
    pageName = Column(String)
    access_time = Column(DateTime)

    def __init__(self, id, pageName, name, email):
        self.id = id
        self.pageName = pageName
        self.name = name
        self.email = email

    def get_id(self):
        return str(self.id)

    # db 에서 user id 를 통해서 user 찾기
    @staticmethod
    def get(user_id):
        find_user = session.query(User).filter( User.id == user_id )
        return find_user.one_or_none()

    # db 에서 user email 를 통해서 user 찾기
    @staticmethod
    def find(user_email):
        find_user = session.query(User).filter( User.email == user_email )
        return find_user.one_or_none()

    # 구독 등록한 user 의 blog 이름과 email 을 등록
    @staticmethod
    def create(user_email, blog_id):
        user = User.find( user_email )
        if user is None:
            new_user = User( id=None, pageName=blog_id, name="practice", email=user_email)
            session.add( new_user )
            session.commit()
            user = User.find( user_email )
        
        return user
        

    # db 에서 user 를 제거
    @staticmethod
    def delete(user_id):
        session.query(User).filter( User.id== user_id ).delete()
        session.commit()
        
