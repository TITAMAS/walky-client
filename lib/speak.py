#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by Keisuke Okumura

# == Kei18 PC ==
# sudo open_jtalk -x /usr/local/Cellar/open-jtalk/1.09/dic
# -m /usr/local/Cellar/open-jtalk/1.09/voice/mei/mei_normal.htsvoice
# -ow out.wav sample.txt
#
# afplay out.wav

import subprocess
from lib.bing_tts import speak_with_bing

def speak(tags, dist, lang):
    tags_str = str.join(', ', tags)
    tag_len = len(tags)

    # Switch language
    if lang == 'en':
        # Use be-verb properly and return if tags are empty
        if tag_len >= 2:
            word = 'There are %s in %s meter' % (tags_str, dist)
        elif tag_len == 1:
            word = 'There is %s' % (tags_str, dist)
        else:
            return
        speak_with_bing(word)
    elif lang == 'ja':
        if tag_len >= 1:
            word = '%sメートル先に%sがあります' % (dist, tags_str)
        else:
            return
        script = os.path.join(os.getcwd(), 'jtalk.sh')
        cmd = ['sh', script, word]
        subprocess.call(cmd)
