# -*- coding: utf-8 -*-
# TODO add comment

import sys
sys.path.append(r'../pylivetable')

import pandas as pd

import pylivetable


class TestRequests:
    # TODO add comment
    def test_categories(self, site):
        # TODO add comment
        categories = pylivetable.categories(site)
        assert isinstance(categories, pd.DataFrame)
        assert len(categories) > 0
        return True

    def test_categories_douyu(self):
        # TODO add comment
        assert self.test_categories('douyu')

    def test_categories_huya(self):
        # TODO add comment
        assert self.test_categories('huya')

    def test_categories_all(self):
        # TODO add comment
        res = pylivetable.categories()
        print(res)
        assert len(res.loc['douyu']) == len(pylivetable.categories('douyu'))
        assert len(res.loc['huya']) == len(pylivetable.categories('huya'))
