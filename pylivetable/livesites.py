# -*- coding: utf-8 -*-
# TODO add comment

from bs4 import BeautifulSoup
from .http import get_content


class Douyu(object):
    # TODO add comment
    CATEGORIES_URL = 'https://www.douyu.com/directory'

    def get_categories(self):
        # TODO add comment
        # get html of http response
        content = get_content(Douyu.CATEGORIES_URL)
        return self._parse_catecontent(content)

    def _parse_catecontent(self, content):
        # TODO add comment &
        cate_names = []
        cate_gameid = []
        cate_href = []

        soup = BeautifulSoup(content, 'lxml')
        for a in soup.select('.unit a'):
            cate_names.append(a.p.get_text())
            cate_gameid.append(a['data-tid'])
            cate_href.append(a['href'])

        return cate_names, cate_gameid, cate_href


class Huya(object):
    # TODO add comment &
    CATEGORIES_URL = 'https://www.huya.com/g'

    def get_categories(self):
        # TODO add comment
        # get html of http response
        content = get_content(Huya.CATEGORIES_URL)
        return self._parse_catecontent(content)

    def _parse_catecontent(self, content):
        # TODO add comment
        cate_names = []
        cate_gameid = []
        cate_href = []

        soup = BeautifulSoup(content, 'lxml')
        for li in soup.select('.game-list-item'):
            cate_names.append(li.a.h3.get_text())
            cate_gameid.append(li['gid'])
            cate_href.append(li.a['href'])

        return cate_names, cate_gameid, cate_href
