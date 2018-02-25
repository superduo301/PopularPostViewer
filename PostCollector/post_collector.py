# -*- coding: utf-8 -*-
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def read_posts():
    source = "Clien"

    # req = requests.get('http://www.ppomppu.co.kr/hot.php?category=1')
    req = requests.get('https://www.clien.net/service/group/community')

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')

    post_tags = soup.select(
        '#div_content > div.list_item'
    )

    posts = []

    for post_tag in post_tags:
        post = {'source': source}

        title = post_tag.select_one(
            'div.list_title > a.list_subject > span[data-role]'
        )
        if title is None:
            continue

        post['title'] = title.text

        url = post_tag.select_one('div.list_title > a.list_subject')
        post['url'] = url.attrs['href']
        post['url_hash'] = hash(url)

        author = post_tag.select_one('div.list_author > span.nickname > span')
        if author:
            post['author'] = author.text
        else:
            author = post_tag.select_one('div.list_author > span.nickname > img')
            post['author'] = author.attrs['alt']

        hit = post_tag.select_one('div.list_hit > span.hit')
        post['hit'] = hit.text

        time = post_tag.select_one('div.list_time > span > span.timestamp')
        post['time'] = datetime.strptime(time.text, "%Y-%m-%d %H:%M:%S")

        print(post)

        posts.append(post)

    return posts
