# -*- coding: utf-8 -*-

'''
pylivetable.livesites
~~~~~~~~~~~~~~~~~~~~~

This module contains the models devided by different Live website.
Each model provides parse method to get data we focus on from http response of it's corresponding site.
'''

from lxml import etree
from .http import get_content


class Douyu(object):
    # TODO add comment
    SITE_NAME = 'douyu'
    CATEGORIES_URL = 'https://www.douyu.com/directory'
    CATES_PARSE_RULES = ['//*[@id="live-list-contentbox"]/li/a/p/text()',
                        '//*[@id="live-list-contentbox"]/li/a/@data-tid',
                        '//*[@id="live-list-contentbox"]/li/a/@href']


class Huya(object):
    # TODO add comment &
    SITE_NAME = 'huya'
    CATEGORIES_URL = 'https://www.huya.com/g'
    CATES_PARSE_RULES = ['//*[@id="js-game-list"]/li/a/h3/text()',
                         '//*[@id="js-game-list"]/li/@gid',
                         '//*[@id="js-game-list"]/li/a/@href']


SITES = {
    'douyu': Douyu,
    'huya': Huya,
}


def get_data(site):
    site_cls = SITES[site]
    content = get_content(site_cls.CATEGORIES_URL)
    tree = etree.HTML(content)
    for parse_rule in site_cls.CATES_PARSE_RULES:
        print(len(tree.xpath(parse_rule)))
        yield tree.xpath(parse_rule)

    yield [site for _ in range(len(tree.xpath(parse_rule)))]


def iter_sites():
    for site in SITES: yield site
