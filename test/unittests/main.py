from unittest import TestLoader
from os.path import dirname

if __name__ == "__main__":
    tests = TestLoader().discover(dirname(__file__), "*.py")
