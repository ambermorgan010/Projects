"""
PURPOSE: Test functions.

AUTHOR(S): Amber Morgan
"""

import unittest

import read_ints


class Tester(unittest.TestCase):
    def test_is_int(self):
        self.assertEqual(True, read_ints.is_int('-256'))
        self.assertEqual(False, read_ints.is_int('purpose'))
        self.assertEqual(False, read_ints.is_int('1.698'))
        self.assertEqual(False, read_ints.is_int('-1.883'))
        self.assertEqual(True, read_ints.is_int('1000'))
        self.assertEqual(False, read_ints.is_int('-purpose'))
        self.assertEqual(False, read_ints.is_int(''))


if __name__ == "__main__":
    unittest.main()
