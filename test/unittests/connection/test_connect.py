import unittest
from unittest.mock import patch, MagicMock
from mycroftapi import MycroftAPI


class TestSet(unittest.TestCase):

    def __init__(self):
        self.ws = MycroftAPI()

    def test_ws_connection(self):
        m = MycroftAPI(mycroft_ip='127.0.0.1')
        m.__init__ = MagicMock(name='connection')
        ws = m.__init__(mycroft_ip='127.0.0.1')
        self.assertEqual(ws.mycroft_ip, ('127.0.0.1'))
        self.assertEqual(ws.text, ('hello brian'))


if __name__ == '__main__':
    unittest.main()
