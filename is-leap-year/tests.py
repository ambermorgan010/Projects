"""
Tests for the leap_year program.

AUTHOR: Amber Morgan
"""

import unittest
import leap_year

class Tester(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(True, leap_year.is_leap_year(2020))
        self.assertEqual(False, leap_year.is_leap_year(1900))
        self.assertEqual(True, leap_year.is_leap_year(1996))
        self.assertEqual(True, leap_year.is_leap_year(2000))
        self.assertEqual(False, leap_year.is_leap_year(1857))


if __name__ == "__main__":
    unittest.main()
