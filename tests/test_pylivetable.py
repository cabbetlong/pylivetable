# -*- coding: utf-8 -*-


import sys
sys.path.append(r'../pylivetable')

import pandas as pd

import pylivetable


class TestRequests:

    def test_categories(self):
        categories = pylivetable.categories()
        assert isinstance(categories, pd.DataFrame)
        assert len(categories) > 0
