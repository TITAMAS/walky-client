#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from picamera import PiCamera
import sys
import time

from backports import tempfile
import mvnc.mvncapi as ncs

from lib.camera import snapshot
from lib.filtering import filter_categories
from lib.jtalk import jtalk
from lib.sonic_sensor import read_distance
from lib.recognition import recognize_image
from lib.speak import speak

DEBUG_PIN = 26
LANG_PIN = 19

DEBUG = False
LANG = 'ja-JP'

if __name__ == '__main__':

    print('LANG:', LANG)

    with PiCamera() as camera:
        # Set camera settings
        print('Initializing...')
        camera.vflip = True
        camera.hflip = True
        camera.resolution = (720, 720)
        camera.shutter_speed = 5000
        camera.iso = 800

        time.sleep(2)
        print('Initialized...')

        jtalk('起動しました')

        ncs_names = ncs.EnumerateDevices()
        if (len(ncs_names) < 1):
            print("Error - no NCS devices detected.")
            sys.exit(1)
        dev = ncs.Device(ncs_names[0])

        dev.OpenDevice()

        with open('inception_v3.graph', 'rb') as f:
            graph = dev.AllocateGraph(f.read())

        while True:
            start = time.time()
            print("start_time:", start)

            with tempfile.TemporaryDirectory() as temp_path:
                filepath = os.path.join(temp_path, 'image.jpg')
                snapshot(camera, filepath)

                elapsed_time_snapshot = time.time() - start
                print("elapsed_time_snapshot:{0}".format(elapsed_time_snapshot) + "[sec]")

                categories = recognize_image(filepath, graph)

            # Filter tags with whitelist
            categories = filter_categories(categories)

            # Read distance from ir sensor
            dist = read_distance()
            print('Dist:', dist)

            if len(categories) >= 1 and dist > 0.0:
                speak(categories, dist, LANG)
                time.sleep(2)

            elapsed_time = time.time() - start
            print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

            end = time.time()
            print("end:", end)

        graph.DeallocateGraph()
        dev.CloseDevice()
        camera.stop_preview()
