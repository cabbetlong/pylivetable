# -*- coding: utf-8 -*-


import sys
sys.path.append(r'../pylivetable')


import pylivetable


class TestRequests:

    def test_categories(self):
        assert pylivetable.categories()


if __name__ == '__main__':
    print(pylivetable.categories())