"""
PURPOSE: Tests functions.
AUTHOR(S): Amber Morgan
"""

import unittest

import collatz

class Tester(unittest.TestCase):
    def test_collatz(self):
        self.assertEqual([1], collatz.Collatz(1))
        self.assertEqual([5, 16, 8, 4, 2, 1], collatz.Collatz(5))
        self.assertEqual([6, 3, 10, 5, 16, 8, 4, 2, 1], collatz.Collatz(6))
        self.assertEqual([10, 5, 16, 8, 4, 2, 1], collatz.Collatz(10))
        self.assertEqual([2, 1], collatz.Collatz(2))
        
    def test_list_to_str(self):
        self.assertEqual('1 2 3', collatz.list_to_str([1, 2, 3]))
        self.assertEqual('1', collatz.list_to_str([1]))
        self.assertEqual('word -1 string', collatz.list_to_str(['word', -1, 'string']))
        self.assertEqual('', collatz.list_to_str([]))
        self.assertEqual('6 3 10 5 16 8 4 2 1', collatz.list_to_str([6, 3, 10, 5, 16, 8, 4, 2, 1]))
        self.assertEqual('2 1', collatz.list_to_str([2, 1]))


if __name__ == "__main__":
    unittest.main()
