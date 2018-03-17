import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import drop_database
from sqlalchemy_utils.functions import database_exists, create_database

from models import Post, Base

print(sqlalchemy.__version__)


engine = create_engine('postgresql+psycopg2://postgres@localhost/posts', echo=True)

# init
if database_exists(engine.url):
    drop_database(engine.url)

if not database_exists(engine.url):
    create_database(engine.url)

metadata = MetaData()
Base.metadata.create_all(engine)


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
