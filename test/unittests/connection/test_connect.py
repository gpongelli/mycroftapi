import unittest
from unittest.mock import MagicMock
from mycroftapi import MycroftAPI


class ConTest(unittest.TestCase):
    def connection_test(self):
        m = MycroftAPI(mycroft_ip='127.0.0.1')
        m.__init__ = MagicMock(name='connection')
        m.speak_text('hello brian')
        self.assertEqual(m.mycroft_ip, '127.0.0.1')
        self.assertEqual(m.text, 'hello brian')
