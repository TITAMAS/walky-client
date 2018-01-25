# -*- coding:utf-8 -*-

from __future__ import absolute_import

import os
import subprocess


def talk(filename='close_car.wav'):
    path = os.path.join('voices', filename)
    aplay = ['aplay', '-q', path]
    subprocess.Popen(aplay)


if __name__ == '__main__':
    talk()
