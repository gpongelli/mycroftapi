import unittest
from unittest.mock import patch, MagicMock
from mycroftapi import MycroftAPI


class TestSet(unittest.TestCase):
    def __init__(self):
        m = MycroftAPI(mycroft_ip='127.0.0.1')
        m.__init__ = MagicMock(name='connection')
        m.speak_text('hello brian')
        self.assertEqual(ws.mycroft_ip, ('127.0.0.1'))
        self.assertEqual(ws.text, ('brian'))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    unittest.TextTestRunner(verbosity=2).run(suite)
