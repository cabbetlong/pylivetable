# -*- coding: utf-8 -*-
# TODO add comment

import pandas as pd
from .livesites import Douyu, Huya


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
        if site is 'all':
            data = dict()
            for _site in SITES:
                data.update(self._get_data(_site))
            return self._gen_dataframe(data)
        else:
            columns = self._get_data(site)
            return self._gen_dataframe(columns)

    def _get_data(self, site):
        # TODO add comment
        if site not in SITES: raise Exception
        site_class = SITES[site.lower()]

        columns = site_class().get_categories()
        data = {site.lower(): dict(zip(Categories.COLUMNS, columns))}
        return data

    def _gen_dataframe(self, data):
        # TODO add comment
        cate_df = pd.DataFrame(data)
        return cate_df
