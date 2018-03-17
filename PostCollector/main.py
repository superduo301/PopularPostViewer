import db_manager
import post_collector


def main():
    print("main")

    posts = post_collector.read_posts()

    # new_post = Post("title", "author", "url", 0)
    db_manager.add(posts)
    db_manager.read()
    db_manager.close()


if __name__ == "__main__":
    main()

