#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# == Kei18 PC ==
# sudo open_jtalk -x /usr/local/Cellar/open-jtalk/1.09/dic
# -m /usr/local/Cellar/open-jtalk/1.09/voice/mei/mei_normal.htsvoice
# -ow out.wav sample.txt
#
# afplay out.wav

import os
import subprocess
import tempfile

from bingtts import Translator
from lib import settings
from lib.filtering import JP_TRANS

def speak(tags, dist, lang):
    tag_len = len(tags)

    # Switch language
    if lang == 'en-US':
        tags_str = str.join(' and ', tags)
        # Use be-verb properly and return if tags are empty
        if tag_len >= 2:
            word = 'There are %s in %.1f meters' % (tags_str, dist)
        elif tag_len == 1:
            word = 'There is %s in %.1f meters' % (tags_str, dist)
        else:
            return
        speak_with_bing(word, lang)
    elif lang == 'ja-JP':
        tags_jp = map(lambda word: JP_TRANS[word], tags)
        tags_str = str.join('と', tags_jp)
        if tag_len >= 1:
            word = '%.1fメートル先に%sがあります' % (dist, tags_str)
        else:
            return
        speak_with_bing(word, lang)

def speak_with_bing(text, lang='en-US'):
    translator = Translator(settings.TTS_API_KEY)
    output = translator.speak(text, lang, 'Female', 'riff-16khz-16bit-mono-pcm')

    with tempfile.TemporaryDirectory() as temp_path:
        filepath = os.path.join(temp_path, 'speech.wav')
        with open(filepath, 'wb') as f:
            f.write(output)
        cmd = ['aplay', filepath]
        subprocess.call(cmd)
