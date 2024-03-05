"""
Functions and testing lab. This file will contain the tests for all of the
functions in the other file to make sure those functions are working properly.

TEAMMATE NAMES: 
"""

# Necessary imports for testing
import unittest


# This imports the "functions" module (your other file)
# All of the functions in that file can be accessed by doing something like:
#   functions.fahrenheit_to_celsius(32)
import functions


class Tester(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(0, functions.fahrenheit_to_celsius(32))  # freezing
        self.assertEqual(100, functions.fahrenheit_to_celsius(212))  # boiling
        self.assertEqual(-40, functions.fahrenheit_to_celsius(-40))  # crossover
        self.assertEqual(37, functions.fahrenheit_to_celsius(98.6))  # body temperature
        self.assertAlmostEqual(21.111, functions.fahrenheit_to_celsius(70), places=3)  # room temperature

    def test_celsius_to_fahrenheit(self):
        # TODO: Write the tests for the celsius_to_fahrenheit() function here (and remove the 'pass')
        pass

    # TODO: add additional tests here as new functions
    # The function names must start with test_
    # They must be indented like the above function
    # Make sure that tests are actually running

    

if __name__ == "__main__":
    unittest.main()
