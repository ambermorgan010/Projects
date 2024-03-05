"""
PURPOSE: Test functions in this lab
CSCI 120 - Computer Science 1 - Lab 7
INSTRUCTOR: Jeff Bush
"""

import unittest

import number_guess

class Tester(unittest.TestCase):
    def test_get_guess_outcome(self):
        self.assertEqual('Your guess was correct!', number_guess.get_guess_outcome(50, 50))
        self.assertEqual('Your guess was correct!', number_guess.get_guess_outcome(1, 1))
        self.assertEqual('Your guess was too low.', number_guess.get_guess_outcome(1, 2))
        self.assertEqual('Your guess was too low.', number_guess.get_guess_outcome(1, 21))
        self.assertEqual('Your guess was too low (not even close)!', number_guess.get_guess_outcome(1, 22))
        self.assertEqual('Your guess was too high (not even close)!', number_guess.get_guess_outcome(22, 1))
        self.assertEqual('Your guess was too high.', number_guess.get_guess_outcome(21, 1))
        self.assertEqual('Your guess was too high.', number_guess.get_guess_outcome(2, 1))


if __name__ == "__main__":
    unittest.main()
