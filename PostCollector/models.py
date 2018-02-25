from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, TIMESTAMP, DateTime

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, Sequence('posts_id_seq'), primary_key=True)
    source = Column(String(256))
    title = Column(String(256))
    author = Column(String(64))
    url = Column(String(2000))
    url_hash = Column(Integer)
    hit = Column(Integer)
    time = Column(TIMESTAMP)

    def __init__(self, params):
        self.source = params['source']
        self.title = params['title']
        self.author = params['author']
        self.url = params['url']
        self.url_hash = params['url_hash']
        self.hit = params['hit']
        self.time = params['time']

