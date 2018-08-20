# -*- coding: utf-8 -*-

'''
pylivetable.livesites
~~~~~~~~~~~~~~~~~~~~~

This module contains the models devided by different Live website.
Each model provides parse method to get data we focus on from http response of it's corresponding site.
'''

from collections import Iterable
from lxml import etree
from pandas import DataFrame
from .http import get_content


class Douyu(object):
    '''
    Config of douyu site
    '''
    DOMAIN = 'https://www.douyu.com'
    SITE_NAME = 'douyu'
    CATEGORIES_URL = 'https://www.douyu.com/directory'

    CATES_PARSE_RULES = ['//*[@id="live-list-contentbox"]/li/a/p/text()',
                        '//*[@id="live-list-contentbox"]/li/a/@data-tid',
                        '//*[@id="live-list-contentbox"]/li/a/@href']

    ROOMSINCATE_URL = 'https://www.douyu.com/gapi/rkc/directory/{0}/1'

    def get_olusers_incates(self, cates):
        if not isinstance(cates, DataFrame): raise ValueError('cates must be pandas.DataFrame')
        if len(cates) == 1:
            return self._get_olusers_incate(cates)
        else:
            return (self._get_olusers_incate(cate)
                            for cate in cates)

    def _get_olusers_incate(self, cate):
        # get page count

        # get all roominfo

        #
        pass


class Huya(object):
    '''
    Config of huya site
    '''
    DOMAIN = 'https://www.huya.com'
    SITE_NAME = 'huya'
    CATEGORIES_URL = 'https://www.huya.com/g'
    CATES_PARSE_RULES = ['//*[@id="js-game-list"]/li/a/h3/text()',
                         '//*[@id="js-game-list"]/li/@gid',
                         '//*[@id="js-game-list"]/li/a/@href']


_SITES = {
    'douyu': Douyu,
    'huya': Huya,
}


def get_cates_data(site):
    '''
    Get categories data.
    :param site: Live Website
    :return: each column data as a list
    '''
    site_cls = _SITES[site]
    content = get_content(site_cls.CATEGORIES_URL)
    tree = etree.HTML(content)
    for parse_rule in site_cls.CATES_PARSE_RULES:
        yield tree.xpath(parse_rule)

    yield [site for _ in range(len(tree.xpath(parse_rule)))]


def iter_sites():
    '''
    Iterate SITES
    :return: generator of SITES
    '''
    for site in _SITES: yield site
