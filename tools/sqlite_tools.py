from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String, JSON
from sqlalchemy.orm import DeclarativeBase
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db.sqlite3")

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, primary_key=False)
    post_text = Column(String, primary_key=False)
    post_photo = Column(String, primary_key=False)
    telegram_message_id = Column(Integer, primary_key=False)

class SqliteTools:
    session = sessionmaker(autoflush=False, bind=engine)

    @classmethod
    def check_exists_db(cls):
        if not os.path.exists('db.sqlite3'):
            Base.metadata.create_all(bind=engine)

    @classmethod
    def add_post(cls, post_id, post_text, post_photo, telegram_message_id):
        post = Post(post_id=post_id, post_text=post_text, post_photo=post_photo, telegram_message_id=telegram_message_id)
        with cls.session(autoflush=False, bind=engine) as db:
            db.add(post)
            db.commit()

    @classmethod
    def get_post(cls, post_id):
        with cls.session(autoflush=False, bind=engine) as db:
            post = db.query(Post).filter(Post.post_id == post_id).first()
            return post
    
    @classmethod
    def check_exists_post(cls, post_id):
        with cls.session(autoflush=False, bind=engine) as db:
            post = db.query(Post).filter(Post.post_id == post_id).first()
            if not post:
                return False
            return True
        
    @classmethod
    def update_post(cls, post_id, text, photo):
        with cls.session(autoflush=False, bind=engine) as db:
            post = db.query(Post).filter(Post.post_id == post_id).first()
            post.post_text = text
            post.post_photo = photo
            db.commit()
            return post