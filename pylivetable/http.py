# -*- coding: utf-8 -*-
# TODO add comment

import requests as rq


def get_content(url):
    # TODO add comment
    try:
        return rq.get(url).text
    except Exception as e:
        print(e)
        return None
