import post_collector

from models import Post
import db_manager


def main():
    print("main")

    posts = post_collector.read_posts()

    # new_post = Post("title", "author", "url", 0)
    db_manager.add(posts)
    db_manager.read()
    db_manager.close()


if __name__ == "__main__":
    main()


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