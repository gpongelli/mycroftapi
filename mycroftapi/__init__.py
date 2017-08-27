from websocket import create_connection, WebSocket
import ssl


class MycroftAPI(object):
    def __init__(self, mycroft_ip, text):
        self.mycroft_ip = mycroft_ip
        self.text = text
        self.url = "(ws://" + self.mycroft_ip + "/core)"
        #self._ws = create_connection(self.url)
        print(self.url)


