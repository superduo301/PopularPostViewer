# -*- coding: utf-8 -*-
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def read_posts():
    clien_post_collector = ClienPostCollector()

    # req = requests.get('http://www.ppomppu.co.kr/hot.php?category=1')
    req = requests.get(clien_post_collector.get_request_url())
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')

    posts = clien_post_collector.get_posts(soup)

    return posts


class PostCollector:
    def __init__(self, source, base_url, request_url):
        self.source = source
        self.base_url = base_url
        self.request_url = request_url

    def get_request_url(self):
        return self.request_url

    def get_base_url(self):
        return self.base_url

    def get_post_tags(self, soup):
        pass

    def get_posts(self, soup):

        post_tags = self.get_post_tags(soup)
        if not post_tags:
            return

        posts = []

        for post_tag in post_tags:
            post = self.get_post(post_tag)
            if post:
                posts.append(post)

        return posts

    def get_post(self, post_tag):
        post = {
            'source': self.get_source(),
            'title': self.get_title(post_tag),
            'url': self.get_url(post_tag),
            'url_hash': self.get_url_hash(post_tag),
            'author': self.get_author(post_tag),
            'hit': self.get_hit(post_tag),
            'time': self.get_time(post_tag)
        }

        if not self.is_valid(post):
            return

        print(post)

        return post

    @staticmethod
    def is_valid(post):
        mandatory_elements = {'title', 'url'}

        for element in mandatory_elements:
            if not post[element]:
                return False

        return True

    def get_source(self):
        return self.source

    def get_title(self, post_tag):
        pass

    def get_url(self, post_tag):
        pass

    def get_url_hash(self, post_tag):
        return hash(self.get_url(post_tag))

    def get_author(self, post_tag):
        pass

    def get_hit(self, post_tag):
        pass

    def get_time(self, post_tag):
        pass


class ClienPostCollector(PostCollector):
    source = 'Clien'
    base_url = 'https://www.clien.net/'
    request_url = 'https://www.clien.net/service/group/community'

    def __init__(self):
        super().__init__(self.source, self.base_url, self.request_url)

    def get_post_tags(self, soup):
        post_tags = soup.select(
            '#div_content > div.list_item'
        )
        return post_tags

    def get_title(self, post_tag):
        title = post_tag.select_one(
            'div.list_title > a.list_subject > span[data-role]'
        )
        if title is None:
            return

        return title.text

    def get_url(self, post_tag):
        url = post_tag.select_one(
            'div.list_title > a.list_subject'
        )
        if not url:
            return

        return self.get_base_url() + url.attrs['href']

    def get_author(self, post_tag):
        author_tag = post_tag.select_one('div.list_author > span.nickname > span')
        if author_tag:
            author = author_tag.text
        else:
            author_tag = post_tag.select_one('div.list_author > span.nickname > img')
            if not author_tag:
                return

            author = author_tag.attrs['alt']

        return author

    def get_hit(self, post_tag):
        hit = post_tag.select_one('div.list_hit > span.hit')
        if not hit:
            return

        return hit.text

    def get_time(self, post_tag):
        time = post_tag.select_one('div.list_time > span > span.timestamp')
        if not time:
            return

        return datetime.strptime(time.text, "%Y-%m-%d %H:%M:%S")

#
# def parse_post(source, base_url, post_tag):
#     post = {'source': source}
#
#     title = post_tag.select_one(
#         'div.list_title > a.list_subject > span[data-role]'
#     )
#     if title is None:
#         return
#
#     post['title'] = title.text
#
#     url = post_tag.select_one('div.list_title > a.list_subject')
#     post['url'] = base_url + url.attrs['href']
#     post['url_hash'] = hash(url)
#
#     author = post_tag.select_one('div.list_author > span.nickname > span')
#     if author:
#         post['author'] = author.text
#     else:
#         author = post_tag.select_one('div.list_author > span.nickname > img')
#         post['author'] = author.attrs['alt']
#
#     hit = post_tag.select_one('div.list_hit > span.hit')
#     post['hit'] = hit.text
#
#     time = post_tag.select_one('div.list_time > span > span.timestamp')
#     post['time'] = datetime.strptime(time.text, "%Y-%m-%d %H:%M:%S")
#
#     print(post)
#
#     return post
