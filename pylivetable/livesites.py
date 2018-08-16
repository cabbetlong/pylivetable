# -*- coding: utf-8 -*-

'''
pylivetable.livesites
~~~~~~~~~~~~~~~~~~~~~

This module contains the models devided by different Live website.
Each model provides parse method to get data we focus on from http response of it's corresponding site.
'''

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
        # TODO add comment & parse rule extraction
        cate_names = []
        cate_gameid = []
        cate_href = []

        soup = BeautifulSoup(content, 'lxml')
        obj_nodes = soup.select('.unit a')
        for a in obj_nodes:
            cate_names.append(a.p.get_text())
            cate_gameid.append(a['data-tid'])
            cate_href.append(a['href'])

        site_index = ['douyu' for _ in range(len(obj_nodes))]
        return site_index, cate_names, cate_gameid, cate_href


class Huya(object):
    # TODO add comment &
    CATEGORIES_URL = 'https://www.huya.com/g'

    def get_categories(self):
        # TODO add comment
        # get html of http response
        content = get_content(Huya.CATEGORIES_URL)
        return self._parse_catecontent(content)

    def _parse_catecontent(self, content):
        # TODO add comment & parse rule extraction
        cate_names = []
        cate_gameid = []
        cate_href = []

        soup = BeautifulSoup(content, 'lxml')
        obj_nodes = soup.select('.game-list-item')
        for li in obj_nodes:
            cate_names.append(li.a.h3.get_text())
            cate_gameid.append(li['gid'])
            cate_href.append(li.a['href'])

        site_index = ['huya' for _ in range(len(obj_nodes))]
        return site_index, cate_names, cate_gameid, cate_href
