import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Post

print(sqlalchemy.__version__)

engine = create_engine('postgresql+psycopg2://postgres:outback15@localhost/posts_db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


def add(post):
    session.add(post)
    print(session.new)
    session.commit()


def add(posts):
    for post in posts:
        session.add(Post(post))
    print(session.new)
    session.commit()


def read():
    queries = session.query(Post)
    entries = [dict(id=q.id) for q in queries]
    print(entries)


def close():
    session.close()
