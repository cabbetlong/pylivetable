# -*- coding: utf-8 -*-

'''
pylivetable.models
~~~~~~~~~~~~~~~~~~

This module contains the base models which integrate the data from Live website to pandas.DataFrame.
'''

from functools import reduce

import pandas as pd
from .livesites import Douyu, Huya
from collections import defaultdict


SITES = {
    'douyu': Douyu,
    'huya': Huya,
}


def _gen_idx(site_idx):
    '''
    Integrate integer index and site index.
    :param site_idx: site index genrated by model of livesites.
    :return: index for pandas.DataFrame
    '''
    return [site_idx, [i for i in range(len(site_idx))]]


def _gendata_forall(last, pre):
    '''
    Function called by reduce() to add each site's data which type is list.
    eg:
    >>> lst = [([1, 2], [3, 4]), ([1, 2], [3, 4]), ([1, 2], [3, 4])]
    >>> reduce(_gendata_forall, lst)
    >>> ([1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4])
    :param last: last element in the iterable object
    :param pre: previous element in the iterable object
    :return:
    '''
    if not last: return pre
    ret = []
    for i in range(len(pre)):
        ret.append(last[i] + pre[i])
    return tuple(ret)


class Categories(object):
    # TODO add comment
    COLUMNS = ['name', 'game_id', 'href']

    def get(self, site):
        # TODO add comment
        if site is 'all':
            all_data = [SITES[_site]().get_categories()
                        for _site in SITES]
            site_idx, *data = reduce(_gendata_forall, all_data)
        else:
            site_idx, *data = SITES[site]().get_categories()

        return self._gen_dataframe(
            dict(zip(Categories.COLUMNS, data)),  # integrate data as a dict used for pandas.DataFrame
            _gen_idx(site_idx))

    def _gen_dataframe(self, data, index):
        # TODO add comment
        cate_df = pd.DataFrame(data, index=index)
        return cate_df
