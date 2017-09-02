from unittest import TestLoader, TextTestRunner
from os.path import dirname

if __name__ == "__main__":
    tests = TestLoader().discover(dirname(__file__), "*.py")
    results = TextTestRunner(verbosity=1).run(tests)
    if results.errors or results.failures:
        exit(1)
    else:
        exit(0)
