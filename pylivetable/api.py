# -*- coding: utf-8 -*-


from .models import Categories


def categories(site='all'):
    '''
    TODO
    :param site:
    :return:
    '''
    cate = Categories()
    return cate.get(site)

