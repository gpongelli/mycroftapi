# Mycroft API [![Build Status](https://travis-ci.org/Geeked-Out-Solutions/mycroftapi.svg?branch=master)](https://travis-ci.org/Geeked-Out-Solutions/mycroftapi) [![Stories in Ready](https://badge.waffle.io/Geeked-Out-Solutions/mycroftapi.svg?label=ready&title=Ready)](http://waffle.io/Geeked-Out-Solutions/mycroftapi) [![Coverage Status](https://coveralls.io/repos/github/Geeked-Out-Solutions/mycroftapi/badge.svg?branch=master)](https://coveralls.io/github/Geeked-Out-Solutions/mycroftapi?branch=master) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

To be used to interact with a mycroft instance.  Right now only feature supported is speaking text but more coming soon.

## Installing
`pip install mycroftapi`

## How to Use
Below is a python code sample to show how to use the API, currently it is only speaking text but more will be coming.

```
from mycroftapi import MycroftAPI

mycroft_ip = '10.0.0.7'
text = 'hello Brian'
mycroft = MycroftAPI(mycroft_ip)
mycroft.speak_text(text)
```

# Features
Currently only has the speak_text function available but more coming soon...
