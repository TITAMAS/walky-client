#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# WebCam Setting
#
# created by Keisuke Okumura

import os


def snapshot(self, name):
    """スナップショットを撮影"""
    filepath = os.path.join(os.getcwd(), '../../images')
    status = os.system('fswebcam -F 1 -S 10 --no-banner -r 320x240 %s.jpg' % name)
    if status == 0:
        self.snapshot(name)
    else:
        print('Shot successfuly')


if __name__ == '__main__':
    snapshot('../test.jpg')
