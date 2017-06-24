from urllib.parse import urlencode
from http.client import HTTPSConnection
import os
import sys
import json

from lib import Acceralation
from lib.camera import snapshot
import settings

def pretty_print_json(json_str):
    parsed = json.loads(json_str)
    print(json.dumps(parsed, indent=4, sort_keys=True))

if __name__ == '__main__':

    accel = Acceralation()
    while True:
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
            pretty_print_json(data)
            conn.close()

            time.sleep(5.0)
