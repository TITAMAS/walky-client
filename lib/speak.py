#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from lib.jtalk import jtalk

JP_TRANS = {
    'cab': 'くるま',
    'streetcar': 'くるま',
    'moving_van': 'くるま',
    'passenger_car': 'くるま',
    'beach_wagon': 'くるま',
    'sports_car': 'くるま',
    'trolleybus': 'くるま',
    'minibus': 'くるま',
    'school_bus': 'くるま',
    'tow_truck': 'とらっく',
    'trailer_truck': 'とらっく',
    'garbage_truck': 'とらっく',
    'bicycle-built-for-two': 'じてんしゃ',
    'tricycle': 'じてんしゃ',
    'unicycle': 'じてんしゃ',
    'mountain_bike': 'じてんしゃ',
    'motor_scooter': 'ばいく',
}

bicycle_group = [
    'bicycle-built-for-two',
    'unicycle',
    'tricycle',
    'mountain_bike',
    'motor_scooter',
]


def speak(tags, dist, lang):
    tag_len = len(tags)
    tag = tags[0]
    tag_jp = JP_TRANS[tag]

    if tag_len >= 1:
        if dist is 0.0 and tag in bicycle_group:
            text = '近くに%s' % (tag_jp)
        elif dist < 0.5:
            text = '近くに%s' % (tag_jp)
        else:
            text = '%.1fメートル先に%s' % (dist, tag_jp)
    else:
        return
    speak_with_jtalk(text, lang)


def speak_raw(text, lang):
    speak_with_jtalk(text, lang)


def speak_with_jtalk(text, lang='en-US'):
    jtalk(text)
