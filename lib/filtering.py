#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

FILTER_LISTS = [
    'cab',
    'streetcar',
    'moving_van',
    'passenger_car',
    'beach_wagon',
    'sports_car',
    'trolleybus',
    'minibus',
    'school_bus',
    'tow_truck',
    'trailer_truck',
    'garbage_truck',
    'bicycle-built-for-two',
    'tricycle',
    'unicycle',
    'mountain_bike',
    'motor_scooter',
]


def filter_categories(categories):
    filtered_categories = [category for category in categories if category in FILTER_LISTS]
    return list(set(filtered_categories))
