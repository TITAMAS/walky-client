#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def read_distance():
    """加速度センサから距離を読み取る"""

    # 必要なライブラリのインポート・設定
    import RPi.GPIO as GPIO

    try:
        GPIO.setwarnings(False)

        # 使用するピンの設定
        GPIO.setmode(GPIO.BCM)
        TRIG = 17 # ボード上の11番ピン(GPIO17)
        ECHO = 27 # ボード上の13番ピン(GPIO27)

        # ピンのモードをそれぞれ出力用と入力用に設定
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.output(TRIG, GPIO.LOW)

        # TRIGに短いパルスを送る
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        # ECHO ピンがHIGHになるのを待つ
        signaloff = time.time()
        while GPIO.input(ECHO) == GPIO.LOW:
            signaloff = time.time()

        # ECHO ピンがLOWになるのを待つ
        signalon = signaloff
        while time.time() < signaloff + 0.1:
            if GPIO.input(ECHO) == GPIO.LOW:
                signalon = time.time()
                break

        # 時刻の差から、物体までの往復の時間を求め、距離を計算する
        timepassed = signalon - signaloff
        distance = timepassed * 170

        return distance

    except Exception as e:
        print(e)
        return 0.0
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    dist = read_distance()
    print('Dist:', dist)
