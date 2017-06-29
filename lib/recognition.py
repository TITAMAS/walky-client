#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from http.client import HTTPSConnection
from lib import settings
from urllib.parse import urlencode

def recognize_image(filepath):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': settings.SUBSCRIPTION_KEY,
    }

    # request params
    params = urlencode({'visualFeatures': 'Tags'})

    # connection
    conn = HTTPSConnection('westus.api.cognitive.microsoft.com')

    img = open(filepath, 'rb').read()
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, img, headers)

    response = conn.getresponse()
    data = response.read().decode('utf-8')

    os.remove(filepath)

    conn.close()

    return data
