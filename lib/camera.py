#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# WebCam Setting
#
# created by Keisuke Okumura

import cv2


class Camera:
    """WEBカメラの設定
    """

    def __init__(self):
        self.img_path = "./images/"
        print 'finish setting camera'

    def snapshot(self, name):
        """スナップショットを撮影"""
        ret, image = cv2.VideoCapture(0).read()
        if not ret:
            raise IOError("Cannnot shot")
        cv2.imwrite(self.img_path+name, image)
