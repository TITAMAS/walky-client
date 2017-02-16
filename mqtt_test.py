#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MQTT Test Client
#
# created by Shun Iwase

import base64
import os
import time

import paho.mqtt.client as mqtt

host = 'std1.mqtt.shiguredo.jp'
user_name = 'sh8@github'
password = os.environ['SANGO_PASSWORD']
port = 1883
topic = '%s/jphacks' % user_name
sub_topic = topic + '/result'
pub_topic = topic + '/image'


def on_connect(client, userdata, flags, respons_code):
    client.subscribe(sub_topic)


def on_publish(client, userdata, mid):
    print("publish: {0}".format(mid))


if __name__ == "__main__":
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.username_pw_set(user_name, password)
    client.connect(host, port=port, keepalive=60)
    client.loop_start()

    while True:
        file = open('lib/images/demo-image.jpg', "rb").read()
        file_data = base64.b64encode(file)
        client.publish(pub_topic, file_data, 0)
        time.sleep(10.0)
