# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from .http import get_content


class Douyu(object):
    CATEGORIES_URL = 'https://www.douyu.com/directory'

    def get_categories(self):
        '''
        TODO
        :return:
        '''
        # get http text of response
        content = get_content(Douyu.CATEGORIES_URL)
        return self._parse_catecontent(content)

    def _parse_catecontent(self, content):
        '''
        TODO
        :param content:
        :return:
        '''
        cate_names = []
        cate_gameid = []
        cate_href = []

        soup = BeautifulSoup(content, 'lxml')
        for a in soup.select('.unit a'):
            cate_names.append(a.p.get_text())
            cate_gameid.append(a['data-tid'])
            cate_href.append(a['href'])

        return cate_names, cate_gameid, cate_href