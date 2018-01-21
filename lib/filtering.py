#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

FILTER_LISTS = ['car', 'track', 'person', 'indoor', 'Library']
JP_TRANS = {'car': '車', 'person': '人', 'indoor': '屋内', 'Library': '図書館'}


def filter_tags(categories):
    return [JP_TRANS[category] for category in categories if category in FILTER_LISTS]
