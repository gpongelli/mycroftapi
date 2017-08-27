# Mycroft API
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
