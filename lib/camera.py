#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# WebCam Setting
#
# created by Keisuke Okumura

import os
import time

import picamera
from picamera import PiCameraError


def snapshot(name):
    """スナップショットを撮影"""
    with picamera.PiCamera() as camera:
        filepath = os.path.join(os.getcwd(), 'images', name)
        camera.hflip = True
        camera.vflip = True
        camera.resolution = (640, 480)
        camera.shutter_speed = 5000
        camera.iso = 800
        try:
            camera.capture(filepath, format='jpeg')
            print('Capture successfuly')
        except PiCameraError:
            print('Something went wrong with the camera')
            time.sleep(3)


if __name__ == '__main__':
    snapshot('test.jpg')
