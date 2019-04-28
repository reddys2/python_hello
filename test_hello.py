import unittest
from hello import *


class HelloTest(unittest.TestCase):
    def test_hello(self):
        response = print_hello()
        self.assertEqual(response, "Hello World")


if __name__ == '__main__':
    unittest.main()
