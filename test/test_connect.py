import unittest
from unittest.mock import patch, MagicMock
from mycroftapi import MycroftAPI


class ConTest(unittest.TestCase):
    def __init__(self):
        m = MycroftAPI(mycroft_ip='127.0.0.1')
        m.__init__ = MagicMock(name='connection')
        m.speak_text('hello brian')
        self.assertEqual(ws.mycroft_ip, ('127.0.0.1'))
        self.assertEqual(ws.text, ('brian'))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ConTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
