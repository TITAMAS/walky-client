#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import time
import RPi.GPIO as GPIO


def read_switch(button_pin):
    # ボタンを繋いだGPIOの端子番号

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_pin, GPIO.IN)

    if GPIO.input(button_pin) == 0:
        state = True
    else:
        state = False

    return state


if __name__ == '__main__':
    button_pin = 26
    try:
        while True:
            state = read_switch(button_pin)
            print(state)
            if(state):
                # 0V(0)の場合に表示
                print("Switch ON")
            else:
                # 3.3V(1)の場合に表示
                print("Switch OFF")

            time.sleep(1)
    finally:
        GPIO.cleanup()
