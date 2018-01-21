#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# WebCam Setting
#
# created by Keisuke Okumura

from __future__ import absolute_import

import time

import picamera
from picamera import PiCameraError


def snapshot(camera, filepath):
    """スナップショットを撮影"""
    try:
        camera.capture(filepath, format='jpeg')
        print('Capture successfuly')
    except PiCameraError:
        print('Something went wrong with the camera')
        time.sleep(3)


if __name__ == '__main__':
    with picamera.PiCamera() as camera:
        snapshot(camera, 'test.jpg')
