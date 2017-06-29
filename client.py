import json
import os
import picamera
import sys
import time
import uuid

from lib.acceleration import Acceleration
from lib.camera import snapshot
from lib.ir_sensor import read_distance
from lib.recognition import recognize_image
import settings

def pretty_print_json(json_str):
    parsed = json.loads(json_str)
    print(json.dumps(parsed, indent=4, sort_keys=True))
    return json

if __name__ == '__main__':
    # Create a directory to store images if it does not exist.
    directory = 'images'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Initialize accelerometer
    accel = Acceleration()
    with picamera.PiCamera() as camera:
        # Set camera settings
        print('Initializing...')
        camera.hflip = True
        camera.vflip = True
        camera.framerate = 80
        camera.resolution = (160, 120)
        camera.shutter_speed = 5000
        camera.iso = 800
        camera.color_effects = (128,128)
        camera.start_preview()

        time.sleep(2)
        print('Initialized...')

        while True:
            # Capture snapshot when acceleration is minimum
            if accel.permit_snapshot():
                start = time.time()
                print("start_time:", start)

                token = uuid.uuid4()
                filename = '%s.jpg' % token
                snapshot(camera, filename)

                elapsed_time_snapshot = time.time() - start
                print ("elapsed_time_snapshot:{0}".format(elapsed_time_snapshot) + "[sec]")

                filepath = os.path.join(os.getcwd(), 'images', filename)
                data = recognize_image(filepath)

                # Read distance from ir sensor
                dist = read_distance()
                print('Dist:', dist)

                json = pretty_print_json(data)

                conn.close()

                elapsed_time = time.time() - start
                print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

                end = time.time()
                print("end:", end)

                time.sleep(5.0)

        camera.stop_preview()
