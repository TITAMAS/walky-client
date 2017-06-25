#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# WebCam Setting
#
# created by Keisuke Okumura

import os
import picamera


def snapshot(name):
    """スナップショットを撮影"""
    camera = picamera.PiCamera()
    filepath = os.path.join(os.getcwd(), 'images', name)
    camera.hflip = True
    camera.vflip = True
    camera.resolution = (640, 480)
    camera.shutter_speed = 5000
    camera.iso = 800
    status = camera.capture(filepath, format='jpeg')
    print(status)
    if status != None:
        snapshot(name)
    else:
        print('Shot successfuly')


if __name__ == '__main__':
    snapshot('test.jpg')
