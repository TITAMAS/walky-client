#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.filtering import JP_TRANS
from lib.jtalk import jtalk


def speak(tags, dist, lang):
    tag_len = len(tags)

    # Switch language
    if lang == 'en-US':
        tags_str = str.join(' and ', tags)
        # Use be-verb properly and return if tags are empty
        if tag_len >= 2:
            text = 'There are %s in %.1f meters' % (tags_str, dist)
        elif tag_len == 1:
            text = 'There is %s in %.1f meters' % (tags_str, dist)
        else:
            return
        speak_with_jtalk(text, lang)
    elif lang == 'ja-JP':
        tags_jp = map(lambda word: JP_TRANS[word], tags)
        tags_str = str.join('と', tags_jp)
        if tag_len >= 1:
            text = '%.1fメートル先に%sがあります' % (dist, tags_str)
        else:
            return
        speak_with_jtalk(text, lang)


def speak_raw(text, lang):
    speak_with_jtalk(text, lang)


def speak_with_jtalk(text, lang='en-US'):
    jtalk(text)
