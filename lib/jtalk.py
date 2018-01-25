# -*- coding:utf-8 -*-

from __future__ import absolute_import

import os
import subprocess


def jtalk(t, filename='open_jtalk.wav'):
    open_jtalk = ['open_jtalk']
    mech = ['-x', '/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice = ['-m', '/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed = ['-r', '1.0']
    outwav = ['-ow', 'open_jtalk.wav']
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay', '-q', filename]
    subprocess.Popen(aplay)


if __name__ == '__main__':
    dist = {
        'close': '近くに',
        '0.5': '0.5メートル先に',
        '1.0': '1.0メートル先に',
        '1.5': '1.5メートル先に',
        '2.0': '2.0メートル先に',
        '2.5': '2.5メートル先に',
        '3.0': '3.0メートル先に',
        '3.5': '3.5メートル先に',
        '4.0': '4.0メートル先に',
        '4.5': '4.5メートル先に',
        '5.0': '5.0メートル先に',
        'far': '5メートル以上先に',
    }

    objects = {
        'car': 'くるまがあります',
        'truck': 'とらっくがあります',
        'bike': 'じてんしゃがあります',
        'scooter': 'ばいくがあります',
    }

    for d_key, d in dist.iteritems():
        for o_key, o in objects.iteritems():
            filename = '%s_%s' % (d_key, o_key)
            text = '%s%s' % (d, o)
            jtalk(text, os.path.join('voices', filename))
