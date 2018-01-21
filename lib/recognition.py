#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import datetime

import cv2
from keras.applications.imagenet_utils import decode_predictions
import numpy as np


def recognize_image(filepath, graph):
    image = cv2.imread(filepath)
    image = cv2.resize(image, (299, 299))
    image = np.array(image) / 255.0
    image -= 0.5
    image *= 2.

    print(str(datetime.now()))
    if (graph.LoadTensor(image.astype(np.float16), 'user object')):
        output, _ = graph.GetResult()
        output = np.delete(output, 0, axis=1)
        data = decode_predictions(output)
        print(data)
    print(str(datetime.now()))

    return data
