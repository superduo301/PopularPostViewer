import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import drop_database
from sqlalchemy_utils.functions import database_exists, create_database

from models import Post, Base

print(sqlalchemy.__version__)


engine = create_engine('postgresql+psycopg2://postgres@localhost/posts_db', echo=True)

# init
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



    # -- Table: public.posts
    #
    # -- DROP TABLE public.posts;
    #
    # CREATE TABLE public.posts
    # (
    #     id serial NOT NULL,
    # source character varying(64) COLLATE pg_catalog."default",
    #                                                 category character varying(64) COLLATE pg_catalog."default",
    #                                                                                                   title character varying(256) COLLATE pg_catalog."default" NOT NULL,
    #                                                                                                                                                                 author character varying(64) COLLATE pg_catalog."default",
    #                                                                                                                                                                                                                 hit integer,
    #                                                                                                                                                                                                                     url character varying(2000) COLLATE pg_catalog."default",
    #                                                                                                                                                                                                                                                                    "time" timestamp with time zone,
    # CONSTRAINT posts_pkey PRIMARY KEY (id)
    # )
    # WITH (
    #     OIDS = FALSE
    # )
    # TABLESPACE pg_default;
    #
    # ALTER TABLE public.posts
    # OWNER to postgres;