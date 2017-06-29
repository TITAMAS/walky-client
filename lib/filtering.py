#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import settings

FILTER_LISTS = ['car', 'track', 'person', 'indoor']
JP_TRANS = {'car': '車', 'person': '人', 'indoor': '屋内'}

def filter_tags(tags, debug=False):

    if not debug:
        return [tag['name'] for tag in tags if tag['name'] in FILTER_LISTS]
    else:
        return [tag['name'] for tag in tags]
