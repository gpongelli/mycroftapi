from unittest import TestLoader

if __name == "__main__":
    tests = TestLoader().discover(dirname(__file__), "*.py")
