# -*- coding: utf-8 -*-

'''
pylivetable.http
~~~~~~~~~~~~~~~~

This module provides methods to get http response by requests lib.
'''

import requests as rq


def get_content(url):
    '''
    Get text of http response by requests lib.
    :param url: Specific url which can get data.
    :return: text of http response.
    '''
    try:
        return rq.get(url).text
    except Exception as e:
        print(e)
        return None
