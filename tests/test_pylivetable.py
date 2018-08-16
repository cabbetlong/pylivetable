# -*- coding: utf-8 -*-
# TODO add comment

import sys
sys.path.append(r'../pylivetable')

import pandas as pd

import pylivetable


class TestRequests:
    # TODO add comment

    def test_categories_douyu(self):
        # TODO add comment
        categories = pylivetable.categories('douyu')
        assert isinstance(categories, pd.DataFrame)
        assert len(categories) > 0

    def test_categories_huya(self):
        # TODO add comment
        categories = pylivetable.categories('huya')
        assert isinstance(categories, pd.DataFrame)
        assert len(categories) > 0

    def test_categories_all(self):
        # TODO add comment
        res = pylivetable.categories()
        print(res)
        assert len(res.loc['douyu']) == len(pylivetable.categories('douyu'))
        assert len(res.loc['huya']) == len(pylivetable.categories('huya'))
