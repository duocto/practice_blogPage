from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
import pymysql

Base = declarative_base()

engine = create_engine("mysql+pymysql://root:fpdlels2@localhost:3306/blog_db", echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# 현재 user의 정보를 받아서 어떤 blog page 를 전달해줄 것인지 판단하는 기능을 제공하는 클래스
class BlogSession(Base):
    __tablename__ = 'user_sessions'

    blog_page = {'A': 'blog_A.html', 'B': 'blog_B.html'}
    session_count = 0

    # session 정보를 저장하기 위한 column
    session_ip = Column(String, primary_key=True)
    email = Column(String)
    pageName = Column(String)
    access_time = Column(DateTime)

    def __init__ ( self, session_ip, user_email, webpage_name, access_time ):
        self.session_ip = session_ip
        self.email = user_email
        self.pageName = webpage_name
        self.access_time = access_time

    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        now_time = now.strftime("%d/%m/%Y %H:%M:%S")
        #db 에 blog session 정보를 넣는 동작 실시
        session.add( BlogSession( session_ip=session_ip, user_email=user_email,webpage_name=webpage_name, access_time=now_time) )
        

    @staticmethod
    def get_blog_page(blog_id=None):
        if blog_id == None:
            if BlogSession.session_count == 0:
                BlogSession.session_count = 1
                return BlogSession.blog_page['A']
            else:
                BlogSession.session_count = 0
                return BlogSession.blog_page['B']
        else:
            return BlogSession.blog_page[blog_id]
