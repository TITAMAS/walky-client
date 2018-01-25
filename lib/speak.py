#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from lib.talk import talk

TAG_GROUP = {
    'cab': 'car',
    'streetcar': 'car',
    'moving_van': 'car',
    'passenger_car': 'car',
    'beach_wagon': 'car',
    'sports_car': 'car',
    'trolleybus': 'car',
    'minibus': 'car',
    'school_bus': 'car',
    'tow_truck': 'truck',
    'trailer_truck': 'truck',
    'garbage_truck': 'truck',
    'bicycle-built-for-two': 'bike',
    'tricycle': 'bike',
    'unicycle': 'bike',
    'mountain_bike': 'bike',
    'motor_scooter': 'scooter',
}

bike_group = [
    'bicycle-built-for-two',
    'unicycle',
    'tricycle',
    'mountain_bike',
    'motor_scooter',
]


def speak(tags, dist):
    tag_len = len(tags)
    tag = tags[0]

    if tag_len >= 1:
        if dist is 0.0 and tag not in bike_group:
            return
        elif dist < 0.5:
            filename = '%s_%s.wav' % ('close', TAG_GROUP[tag])
        elif dist > 5.0:
            filename = '%s_%s.wav' % ('far', TAG_GROUP[tag])
        else:
            round_dist = round(dist * 2) / 2.0
            filename = '%s_%s.wav' % (round_dist, TAG_GROUP[tag])
    else:
        return
    speak_with_talk(filename)


def speak_with_talk(filename):
    talk(filename)
