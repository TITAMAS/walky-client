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


def snapshot(camera, name):
    """スナップショットを撮影"""
    filepath = os.path.join(os.getcwd(), 'images', name)
    try:
        camera.capture(filepath, format='jpeg')
        print('Capture successfuly')
    except PiCameraError:
        print('Something went wrong with the camera')
        time.sleep(3)


if __name__ == '__main__':
    with picamera.PiCamera() as camera:
        snapshot(camera, 'test.jpg')
