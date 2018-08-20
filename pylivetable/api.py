# -*- coding: utf-8 -*-

'''
pylivetable.api
~~~~~~~~~~~~~~~

This module implements the pylivetable API.
'''

from .models import Categories


def categories(site='all', top=None):
    '''
    Get categories from Live website
    :param site: Live website name
    :return: categories table which type is pandas.DataFrame
    '''
    cate = Categories()
    return cate.get(site, top)

