# -*- coding: utf-8 -*-
# TODO add comment

from .models import Categories


def categories(site='all'):
    # TODO add comment
    cate = Categories()
    return cate.get(site)

