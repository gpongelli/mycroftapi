# Mycroft API [![Build Status](https://travis-ci.org/Geeked-Out-Solutions/mycroftapi.svg?branch=master)](https://travis-ci.org/Geeked-Out-Solutions/mycroftapi) [![Stories in Ready](https://badge.waffle.io/Geeked-Out-Solutions/mycroftapi.svg?label=ready&title=Ready)](http://waffle.io/Geeked-Out-Solutions/mycroftapi) [![Coverage Status](https://coveralls.io/repos/github/Geeked-Out-Solutions/mycroftapi/badge.svg?branch=master)](https://coveralls.io/github/Geeked-Out-Solutions/mycroftapi?branch=master) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

To be used to interact with a mycroft instance https://mycroft.ai.  Right now only feature supported is speaking text but more coming soon.

## Installing
`pip install mycroftapi`

## How to Use
Below is a python code sample to show how to use the API, currently has a lot of things supported from changing eye color and more.


This example shows how to have Hello Brian scrolled across the display until I send it a reset.
```
from mycroftapi import MycroftAPI

mycroft_ip = '10.0.0.7'
text = 'hello Brian'
mycroft = MycroftAPI(mycroft_ip)
mycroft.speak_text(text)
```

# Features
- scroll text
- change eye colors
- blink eyes
- eyes off/on
- mute speaker
- change eye brightness
- control mouth visuals like smiling, etc
- speak text to mycroft to have it speak it
