#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tempfile
import os

from bingtts import Translator
from lib import settings

def speak_with_bing(text):
    translator = Translator(settings.TTS_API_KEY)
    output = translator.speak(text, "en-US", "Female", "riff-16khz-16bit-mono-pcm")

    with tempfile.TemporaryDirectory() as temp_path:
        filepath = os.path.join(temp_path, 'speech.wav')
        with open(filepath, 'wb') as f:
            f.write(output)
        cmd = ['aplay', filepath]
        subprocess.call(cmd)
