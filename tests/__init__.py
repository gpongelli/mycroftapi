import unittest
from unittest.mock import patch, MagicMock
from mycroftapi import MycroftAPI


class TestSet(unittest.TestCase):
    def test_ws_connection(self):
        m = MycroftAPI(mycroft_ip='127.0.0.1', text='hello brian')
        m.open_ws_connection = MagicMock(name='connection')
        ws = MycroftAPI(m.mycroft_ip, m.text)
        self.assertEqual(ws.mycroft_ip, ('127.0.0.1'))
        self.assertEqual(ws.text, ('hello brian'))


if __name__ == '__main__':
    unittest.main()