#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wiringpi
import time


def read_switch():
    # ボタンを繋いだGPIOの端子番号
    button_pin = 10

    # GPIO初期化
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode( button_pin, 0 )
    wiringpi.pullUpDnControl( button_pin, 2 )
    return wiringpi.digitalRead(button_pin)

if __name__ == '__main__':
    # whileの処理は字下げをするとループの範囲になる（らしい）
    switch1 = read_switch()
    while True:
        if( switch1 == 0 ):
            # 0V(0)の場合に表示
            print ("Switch ON")
        else:
            # 3.3V(1)の場合に表示
            print ("Switch OFF")

        time.sleep(1)
