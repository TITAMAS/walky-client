from http.client import HTTPSConnection
import json
import os
import sys
import time
from urllib.parse import urlencode
import uuid

from lib.acceleration import Acceleration
from lib.camera import snapshot
from lib.ir_sensor import read_distance
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
    while True:
        # Capture snapshot when acceleration is minimum
        if accel.permit_snapshot():
            token = uuid.uuid4()
            filename = '%s.jpg' % token
            snapshot(filename)

            headers = {
                'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': settings.SUBSCRIPTION_KEY,
            }

            # request params
            params = urlencode({'visualFeatures': 'Tags'})

            # connection
            conn = HTTPSConnection('westus.api.cognitive.microsoft.com')

            filepath = os.path.join('images', filename)
            img = open(filepath, 'rb').read()
            conn.request("POST", "/vision/v1.0/analyze?%s" % params, img, headers)

            response = conn.getresponse()
            data = response.read().decode('utf-8')

            # Read distance from ir sensor
            dist = read_distance()
            print('Dist:', dist)

            json = pretty_print_json(data)

            conn.close()

            time.sleep(5.0)
