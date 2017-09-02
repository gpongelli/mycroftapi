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
    def test_ws_connection(self, mock_create_conn):
        # Create simple replacement websocket object and return it
        # when creating sockets
        mock_ws = MockWS()
        mock_create_conn.return_value = mock_ws

        # Test that init calls create_connection with correct param
        m = MycroftAPI('127.0.0.1')
        mock_create_conn.assert_called_with(
            "ws://" + '127.0.0.1' + ":8181/core")

        # Check that message bus message looks like what we expect
        text = 'hello brian'
        # Expected data to websocket
        mycroft_speak = ('"{}"'.format(text))
        mycroft_type = '"speak"'
        mycroft_data = '{"expect_response": false, "utterance": %s}, ' \
                       '"context": null' % mycroft_speak
        message = '{"type": ' + mycroft_type + \
                  ', "data": ' + mycroft_data + '}'
        m.speak_text(text)
        self.assertEqual(message, mock_ws.message)

    def test_os_error(self):
        self.assertRaises(OSError, MycroftAPI.__init__(self, mycroft_ip='1.1'))


if __name__ == '__main__':
    unittest.main()
