#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import picamera
import sys
import tempfile
import time

from lib.acceleration import Acceleration
from lib.camera import snapshot
from lib.dip import read_switch
from lib.filtering import filter_tags
from lib.sonic_sensor import read_distance
from lib.recognition import recognize_image
from lib import settings
from lib.speak import speak, speak_raw

DEBUG_PIN = 26
LANG_PIN = 19

DEBUG = False
LANG = 'en-US'

if __name__ == '__main__':

    if read_switch(LANG_PIN):
        LANG = 'ja-JP'

    if read_switch(DEBUG_PIN):
        DEBUG = True

    print('LANG:', LANG)
    print('DEBUG:', DEBUG)

    # Initialize accelerometer
    accel = Acceleration()

    with picamera.PiCamera() as camera:
        # Set camera settings
        print('Initializing...')
        camera.hflip = True
        camera.vflip = True
        camera.framerate = 80
        camera.resolution = (320, 240)
        camera.shutter_speed = 5000
        camera.iso = 800
        camera.start_preview()

        time.sleep(2)
        print('Initialized...')

        while True:
            # Capture snapshot when acceleration is minimum
            if not DEBUG:
                if accel.permit_snapshot():
                    start = time.time()
                    print("start_time:", start)

                    with tempfile.TemporaryDirectory() as temp_path:
                        filepath = os.path.join(temp_path, 'image.jpg')
                        snapshot(camera, filepath)

                        elapsed_time_snapshot = time.time() - start
                        print ("elapsed_time_snapshot:{0}".format(elapsed_time_snapshot) + "[sec]")

                        data = json.loads(recognize_image(filepath))

                    tags = data.get('tags', [])

                    # Filter tags with whitelist
                    filtered_tags = filter_tags(tags)

                    # Read distance from ir sensor
                    dist = read_distance()
                    print('Dist:', dist)

                    speak(filtered_tags, dist, LANG)

                    elapsed_time = time.time() - start
                    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

                    end = time.time()
                    print("end:", end)
            else:
                import boto3
                from datetime import datetime

                s3 = boto3.resource('s3')
                BUCKET_NAME = 'walky-debug'

                with tempfile.TemporaryDirectory() as temp_path:
                    filepath = os.path.join(temp_path, 'image.jpg')

                    speak_raw('will take a picture', LANG)
                    snapshot(camera, filepath)
                    speak_raw('finish taking a picture', LANG)

                    data = open(filepath, 'rb')
                    key = datetime.now().strftime("%Y/%m/%d/%H_%M_%S")
                    bucket = s3.Bucket(BUCKET_NAME)
                    bucket.put_object(Key=key, Body=data)

                speak_raw('Uploaded', LANG)

                time.sleep(3)

        camera.stop_preview()
