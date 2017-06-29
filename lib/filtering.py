#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import settings

def filter_tags(tags, debug=False):
    filter_lists = settings.FILTER_LISTS

    if not debug:
        return [tag['name'] for tag in tags if tag['name'] in filter_lists]
    else:
        return [tag['name'] for tag in tags]
