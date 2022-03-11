# user 를 객체로 정의
from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BlogSession(Base):
    __tablename__ = 'user_sessions'

    blog_page = {'A': 'blog_A.html', 'B': 'blog_B.html'}
    session_count = 0

    # session 정보를 저장하기 위한 column
    session_ip = Column(String)
    email = Column(String)
    pageName = Column(String)
    access_time = Column(DateTime)

    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        now_time = now.strftime("%d/%m/%Y %H:%M:%S")
        #db 에 blog session 정보를 넣는 동작 실시

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
