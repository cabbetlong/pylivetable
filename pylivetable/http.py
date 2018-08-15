# -*- coding: utf-8 -*-


import requests as rq


def get_content(url):
    '''
    TODO
    :param url:
    :return:
    '''
    try:
        return rq.get('https://www.douyu.com/directory').text
    except Exception as e:
        print(e)
        return None
