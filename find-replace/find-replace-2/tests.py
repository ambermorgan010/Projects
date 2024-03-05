"""
PURPOSE: Test functions.
AUTHOR: Amber Morgan
"""

import unittest

import replace

class Tester(unittest.TestCase):
    def test_replace(self):
        self.assertEqual(replace.replace('Hello World', 'o', 'x'), 'Hellx Wxrld')
        self.assertEqual(replace.replace('aaaaaa', 'a', 'o'), 'oooooo')
        self.assertEqual(replace.replace('spaghetti', 'd', 'x'), 'spaghetti')
        self.assertEqual(replace.replace('Pepper', 'p', 'b'), 'Pebber')
        self.assertEqual(replace.replace('Mississippi', 's', 'p'), 'Mippippippi')

if __name__ == "__main__":
    unittest.main()
