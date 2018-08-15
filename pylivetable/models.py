# -*- coding: utf-8 -*-


import pandas as pd
from .livesites import Douyu


SITES = {
    'douyu': Douyu
}


class Categories(object):

    COLUMNS = ['name', 'game_id', 'href']

    def __init__(self):
        pass

    def get(self, site):
        '''
        TODO
        :param site:
        :return:
        '''
        # choose site
        if site is 'all':
            columns = ([], [], [])
            names, game_ids, hrefs = columns
            for _site in SITES:
                name, game_id, href = self._get_columns(_site)
                names.append(name)
                game_ids.append(game_id)
                hrefs.append(href)
                return self._gen_dataframe(columns)
        else:
            columns = self._get_columns(site)
            return self._gen_dataframe(columns)

    def _get_columns(self, site):
        '''
        TODO
        :param site:
        :return:
        '''
        if site not in SITES: raise Exception
        site_class = SITES[site.lower()]

        columns = site_class().get_categories()
        return columns

    def _gen_dataframe(self, columns):
        '''
        TODO
        :return:
        '''
        datas = dict(zip(Categories.COLUMNS, columns))
        cate_df = pd.DataFrame(datas)

        return cate_df