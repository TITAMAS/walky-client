#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from datetime import datetime

from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
import numpy as np


def recognize_image(filepath, graph):
    img = image.load_img(filepath, target_size=(299, 299))
    img = image.img_to_array(img) / 255.0
    img -= 0.5
    img *= 2.

    print(str(datetime.now()))
    if (graph.LoadTensor(img.astype(np.float16), 'user object')):
        output, _ = graph.GetResult()
        output = np.expand_dims(output, axis=0)
        output = np.delete(output, 0, axis=1)
        data = decode_predictions(output)
    print(str(datetime.now()))

    data = map(lambda x: x[1], data[0])

    return data
