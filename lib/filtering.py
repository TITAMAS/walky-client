#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

FILTER_LISTS = [
    'streetcar',
    'moving_van',
    'car_mirror',
    'car_wheel',
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

JP_TRANS = {
    'streetcar': 'くるま',
    'moving_van': 'くるま',
    'car_mirror': 'くるま',
    'car_wheel': 'くるま',
    'passenger_car': 'くるま',
    'beach_wagon': 'くるま',
    'sports_car': 'くるま',
    'trolleybus': 'ばす',
    'minibus': 'ばす',
    'school_bus': 'ばす',
    'tow_truck': 'とらっく',
    'trailer_truck': 'とらっく',
    'garbage_truck': 'とらっく',
    'bicycle-built-for-two': 'じてんしゃ',
    'tricycle': 'じてんしゃ',
    'unicycle': 'じてんしゃ',
    'mountain_bike': 'じてんしゃ',
    'motor_scooter': 'ばいく',
}


def filter_categories(categories):
    filtered_categories = [JP_TRANS[category] for category in categories if category in FILTER_LISTS]
    return list(set(filtered_categories))
