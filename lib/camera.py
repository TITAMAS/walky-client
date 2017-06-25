#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# WebCam Setting
#
# created by Keisuke Okumura

import os


def snapshot(name):
    """スナップショットを撮影"""
    filepath = os.path.join(os.getcwd(), 'images', name)
    status = os.system('raspistill -t 1 -o %s -vf -hf -w 640 -h 480' % filepath)
    if status == 0:
        snapshot(name)
    else:
        print('Shot successfuly')


if __name__ == '__main__':
    snapshot('test.jpg')
