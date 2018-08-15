# -*- coding: utf-8 -*-


import sys
sys.path.append(r'../pylivetable')

import pandas as pd

import pylivetable


class TestRequests:

    def test_categories(self, site):
        categories = pylivetable.categories(site)
        assert isinstance(categories, pd.DataFrame)
        assert len(categories) > 0
        return True

    def test_categories_all(self):
        assert self.test_categories('all')

    def test_categories_douyu(self):
        assert self.test_categories('douyu')

    def test_categories_huya(self):
        assert self.test_categories('huya')
