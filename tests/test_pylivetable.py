# -*- coding: utf-8 -*-


import sys
sys.path.append(r'../pylivetable')

import pandas as pd

from pylivetable import categories
from pylivetable.livesites import iter_sites


class TestPylivetable:
    '''
    Test class for pylivetable
    '''

    def test_categories_single_site(self):
        '''
        Test pylivetable.categories when param :site is single site
        '''
        for site in iter_sites():
            res = categories(site)
            assert isinstance(res, pd.DataFrame)
            assert len(res) > 0

    def test_categories_all(self):
        '''
        Test pylivetable.categories when param :site 'all'
        '''
        res = categories()
        for site in iter_sites():
            assert len(res.loc[site]) == len(categories(site))
