# -*- coding: utf-8 -*-

'''
pylivetable.api
~~~~~~~~~~~~~~~

This module implements the pylivetable API.
'''

from .models import Categories


def categories(site='all'):
    # TODO add comment
    cate = Categories()
    return cate.get(site)

