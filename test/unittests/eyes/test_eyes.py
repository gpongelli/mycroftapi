import unittest
from unittest.mock import patch
from mycroftapi import MycroftAPI


class MockWS(object):
    def __init__(self):
        pass

    def send(self, message):
        self.message = message


class TestSet(unittest.TestCase):
    @patch('mycroftapi.create_connection')
    def test_eyes_blink(self, mock_create_conn):
        # Create simple replacement websocket object and return it
        # when creating sockets
        mock_ws = MockWS()
        mock_create_conn.return_value = mock_ws
        # Test that init calls create_connection with correct param
        m = MycroftAPI('127.0.0.1')
        mock_create_conn.assert_called_with(
            "ws://" + '127.0.0.1' + ":8181/core")
        # Check that message bus message looks like what we expect
        # Expected data to websocket
        side = "b"
        mycroft_type = '"enclosure.eyes.blink"'
        mycroft_data = '{"side": "%s"}, ' \
                       '"context": null' % side
        message = '{"type": ' + mycroft_type + \
                  ', "data": ' + mycroft_data + '}'
        m.blink_eyes(side)
        self.assertEqual(message, mock_ws.message)

    @patch('mycroftapi.create_connection')
    def test_eyes_off(self, mock_create_conn):
        # Create simple replacement websocket object and return it
        # when creating sockets
        mock_ws = MockWS()
        mock_create_conn.return_value = mock_ws
        # Test that init calls create_connection with correct param
        m = MycroftAPI('127.0.0.1')
        mock_create_conn.assert_called_with(
            "ws://" + '127.0.0.1' + ":8181/core")
        # Check that message bus message looks like what we expect
        # Expected data to websocket
        mycroft_type = '"enclosure.eyes.off"'
        message = '{"type": ' + mycroft_type + '}'
        m.eyes_off()
        self.assertEqual(message, mock_ws.message)

    @patch('mycroftapi.create_connection')
    def test_eyes_on(self, mock_create_conn):
        # Create simple replacement websocket object and return it
        # when creating sockets
        mock_ws = MockWS()
        mock_create_conn.return_value = mock_ws
        # Test that init calls create_connection with correct param
        m = MycroftAPI('127.0.0.1')
        mock_create_conn.assert_called_with(
            "ws://" + '127.0.0.1' + ":8181/core")
        # Check that message bus message looks like what we expect
        # Expected data to websocket
        mycroft_type = '"enclosure.eyes.on"'
        message = '{"type": ' + mycroft_type + '}'
        m.eyes_on()
        self.assertEqual(message, mock_ws.message)

    @patch('mycroftapi.create_connection')
    def test_squint_eyes(self, mock_create_conn):
        # Create simple replacement websocket object and return it
        # when creating sockets
        mock_ws = MockWS()
        mock_create_conn.return_value = mock_ws
        # Test that init calls create_connection with correct param
        m = MycroftAPI('127.0.0.1')
        mock_create_conn.assert_called_with(
            "ws://" + '127.0.0.1' + ":8181/core")
        # Check that message bus message looks like what we expect
        # Expected data to websocket
        mycroft_type = '"enclosure.eyes.narrow"'
        message = '{"type": ' + mycroft_type + '}'
        m.squint_eyes()
        self.assertEqual(message, mock_ws.message)

    @patch('mycroftapi.create_connection')
    def test_eyes_look(self, mock_create_conn):
        # Create simple replacement websocket object and return it
        # when creating sockets
        mock_ws = MockWS()
        mock_create_conn.return_value = mock_ws
        # Test that init calls create_connection with correct param
        m = MycroftAPI('127.0.0.1')
        mock_create_conn.assert_called_with(
            "ws://" + '127.0.0.1' + ":8181/core")
        # Check that message bus message looks like what we expect
        # Expected data to websocket
        side = "u"
        mycroft_type = '"enclosure.eyes.look"'
        mycroft_data = '{"side": "%s"}, ' \
                       '"context": null' % side
        message = '{"type": ' + mycroft_type + \
                  ', "data": ' + mycroft_data + '}'
        m.eyes_look(side)
        self.assertEqual(message, mock_ws.message)

    @patch('mycroftapi.create_connection')
    def test_eyes_color(self, mock_create_conn):
        # Create simple replacement websocket object and return it
        # when creating sockets
        mock_ws = MockWS()
        mock_create_conn.return_value = mock_ws
        # Test that init calls create_connection with correct param
        m = MycroftAPI('127.0.0.1')
        mock_create_conn.assert_called_with(
            "ws://" + '127.0.0.1' + ":8181/core")
        # Check that message bus message looks like what we expect
        # Expected data to websocket
        r = 0
        g = 255
        b = 0
        mycroft_type = '"enclosure.eyes.color"'
        mycroft_data = '{"r": %s, "g": %s, "b": %s}, ' \
                       '"context": null' % (r, g, b)
        message = '{"type": ' + mycroft_type + \
                  ', "data": ' + mycroft_data + '}'
        m.eyes_color(r, g, b)
        self.assertEqual(message, mock_ws.message)

    @patch('mycroftapi.create_connection')
    def test_eyes_bright(self, mock_create_conn):
        # Create simple replacement websocket object and return it
        # when creating sockets
        mock_ws = MockWS()
        mock_create_conn.return_value = mock_ws
        # Test that init calls create_connection with correct param
        m = MycroftAPI('127.0.0.1')
        mock_create_conn.assert_called_with(
            "ws://" + '127.0.0.1' + ":8181/core")
        # Check that message bus message looks like what we expect
        # Expected data to websocket
        level = 20
        mycroft_type = '"enclosure.eyes.level"'
        mycroft_data = '{"level": %s}, ' \
                       '"context": null' % level
        message = '{"type": ' + mycroft_type + \
                  ', "data": ' + mycroft_data + '}'
        m.eyes_brightness(level)
        self.assertEqual(message, mock_ws.message)

if __name__ == '__main__':
    unittest.main()
