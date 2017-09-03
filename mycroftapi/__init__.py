from websocket import create_connection, WebSocket


class MycroftAPI(object):
    def __init__(self, mycroft_ip):
        self.mycroft_ip = mycroft_ip
        self.url = "ws://" + self.mycroft_ip + ":8181/core"
        try:
            self._ws = create_connection(self.url)
        except OSError:
            print("Could not connect, verify ip.")
            return None

    def speak_text(self, text):
        mycroft_speak = ('"{}"'.format(text))
        mycroft_type = '"speak"'
        mycroft_data = '{"expect_response": false, "utterance": %s}, ' \
                       '"context": null' % mycroft_speak
        message = '{"type": ' + mycroft_type + \
                  ', "data": ' + mycroft_data + '}'
        self._ws.send(message)
        response = "Message Sent to Mycroft Instance: {}"\
            .format(self.mycroft_ip)
        return response

    def blink_eyes(self, side):
        """
        Used to blink eyes on a mark1 device, side can be values of:

        Args:
            side (str): 'r', 'l', or 'b' for 'right', 'left' or 'both'

        """
        side = '""'
        mycroft_type = '"enclosure.eyes.blink"'
        mycroft_data = '{"side": %s}, ' \
                       '"context": null' % side
        message = '{"type": ' + mycroft_type + \
                  ', "data": ' + mycroft_data + '}'
        print(message)
        self._ws.send(message)
        response = "Sent command to mycroft to blink eye on side %s" % side
        return response

    def eyes_off(self):
        """
        Used to turn off eyes on mark1 device
        """
        mycroft_type = '"enclosure.eyes.off"'
        message = '{"type": ' + mycroft_type + '}'
        print(message)
        self._ws.send(message)
        response = "Sent command to mycroft to turn off  mark1 eyes"
        return response

    def eyes_on(self):
        """
        Used to turn on eyes on mark1 device.
        """
        mycroft_type = '"enclosure.eyes.on"'
        message = '{"type": ' + mycroft_type + '}'
        self._ws.send(message)
        response = "Sent command to mycroft to turn on mark1 eyes"
        return response

    def reset_display(self):
        """
        Used to reset display of mark1 back to started state
        """
        mycroft_type = '"enclosure.reset"'
        message = '{"type": ' + mycroft_type + '}'
        self._ws.send(message)
        response = "Sent command to mycroft to reset mark1 screen"
        return response

    def mute_speaker(self, mute):
        """
        Used to mute speaker on enclosure

        Args:
            mute (boolean): True or False - True to mute, False to unmute

        """
        if mute is True:
            mycroft_type = '"enclosure.system.mute"'
            mute_speaker = 'mute'
        else:
            mycroft_type = '"enclosure.system.unmute"'
            mute_speaker = 'unmute'
        message = '{"type": ' + mycroft_type + '}'
        self._ws.send(message)
        response = "Sent command to mycroft to %s speaker" % mute_speaker
        return response


