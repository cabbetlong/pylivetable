# -*- coding: utf-8 -*-

'''
pylivetable.models
~~~~~~~~~~~~~~~~~~

This module contains the base models which integrate the data from Live website to pandas.DataFrame.
'''

import pandas as pd
from .livesites import Douyu, Huya
from collections import defaultdict


SITES = {
    'douyu': Douyu,
    'huya': Huya,
}


class Categories(object):
    # TODO add comment
    COLUMNS = ['name', 'game_id', 'href']

    def __init__(self):
        pass

    def get(self, site):
        # TODO add comment
        # choose site
        data = defaultdict(list)
        index = [[], []]
        if site is 'all':
            index_len = 0
            for _site in SITES:
                lenth, dataofsite = self._get_data(_site)
                for key, value in zip(Categories.COLUMNS, dataofsite):
                    data[key].extend(value)
                index[0].extend([_site for _ in range(lenth)])
                index[1].extend([i for i in range(index_len, index_len + lenth)])
                index_len += lenth
            return self._gen_dataframe(data, index)
        else:
            lenth, data = self._get_data(site)
            index[0].extend([site for _ in range(lenth)])
            index[1].extend([i for i in range(lenth)])
            return self._gen_dataframe(dict(zip(Categories.COLUMNS, data)), index)

    def _get_data(self, site):
        # TODO add comment
        if site not in SITES: raise Exception
        site_class = SITES[site]

        data = site_class().get_categories()
        lenth = len(data[0])
        return lenth, data

    def _gen_dataframe(self, data, index):
        # TODO add comment
        cate_df = pd.DataFrame(data, index=index)
        return cate_df
