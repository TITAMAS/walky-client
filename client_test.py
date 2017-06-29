from urllib.parse import urlencode
from http.client import HTTPSConnection
import sys
import json

from lib import settings

def pretty_print_json(json_str):
    parsed = json.loads(json_str)
    print(json.dumps(parsed, indent=4, sort_keys=True))

if __name__ == '__main__':

    # request header
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': settings.SUBSCRIPTION_KEY,
    }

    # request params
    params = urlencode({'visualFeatures': 'Tags'})

    # connection
    conn = HTTPSConnection('westus.api.cognitive.microsoft.com')

    file_name = 'sample.jpg'
    img = open(file_name, 'rb').read()
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, img, headers)

    response = conn.getresponse()
    data = response.read().decode('utf-8')
    pretty_print_json(data)
    conn.close()
