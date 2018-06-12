# Mycroft API [![Build Status](https://travis-ci.org/Geeked-Out-Solutions/mycroftapi.svg?branch=dev)](https://travis-ci.org/Geeked-Out-Solutions/mycroftapi) [![Stories in Ready](https://badge.waffle.io/Geeked-Out-Solutions/mycroftapi.svg?label=ready&title=Ready)](http://waffle.io/Geeked-Out-Solutions/mycroftapi) [![Coverage Status](https://coveralls.io/repos/github/Geeked-Out-Solutions/mycroftapi/badge.svg?branch=dev)](https://coveralls.io/github/Geeked-Out-Solutions/mycroftapi?branch=dev) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

This library enables the management of some of the facilites provided by a Mycroft (https://mycroft.ai) instance 

# Installing
`pip install mycroftapi`

# Using

The following examples are in-line python and can be run on the Mycroft. Using a remote IP address, the code can be executed from elsewhere.

Each function should be proceeded with the Python interpreter, import and API code:
```
python
from mycroftapi import MycroftAPI
mycroft = MycroftAPI('127.0.0.1')
```
Following this, paste any of the following examples (press ctrl-d to exit the Python command line):

## Sound

### Speak

```
mycroft.speak_text('Hello world')
```

### Mute the speaker

Parameters: mute (boolean): True or False - True to mute, False to unmute

```mycroft.mute_speaker(true)```

## Eyes
### Blink eyes

Parameters: left,righ,both (or l,r,b)

```mycroft.blink_eyes('b')```

### Eyes off

```mycroft.eyes_off()```

### Eyes on

```mycroft.eyes_on()```

### Squint

```mycroft.squint_eyes()```

### Eyes look

Parameters  'r', 'l', 'u', 'd', or 'c' for 'right', 'left' 'up', 'down' or 'crossed'

```mycroft.eyes_look('l')```

### Set eye colour

Parameters: r,g,b

```mycroft.eyes_color(255,100,0)```

### Set eye brightness

Parameters: 1-30 (bigger number is brighter)

```mycroft.eyes_brightness(10)```

### Reset eyes

```mycroft.eyes_reset()```
- Note: :x: not working

## Mouth animations

### Talking

```mycroft.mouth_talk()```

### Thinking 

```mycroft.mouth_think()```

### Listen

```mycroft.mouth_listen()```

### Smile

```mycroft.mouth_smile()```
- Note: :x: not working

### Display text

```mycroft.mouth_text('hello world')```
- Note: :x: not working

### Reset the display
```mycroft.reset_display()```
