"""
PURPOSE: Tests functions
AUTHOR: Amber Morgan
"""

import unittest

import project


class Tester(unittest.TestCase):
    def test_get_field_data(self):
        dictionary = {0: [6, 4, 2, 55, 346, 36, 3, 60, 45, 67, 40, 4, 7, 23],
                      1: [12, 3, 0, 55, 67, 3, 67, 54, 8, 94, 43, 9.4, 23, 6],
                      2: [9, 7, 14, 44, 23, 45, 7, 67, 8, 4, 34, 56, 5.6, 3]}
        dict_index = ["coins", "marbles", "cookies"]
        self.assertEqual({(34.0, 56.0): 9.0, (40.0, 4.0): 6.0, (43.0, 9.4): 12.0}, project.get_field_data("coins",
                                                                                                          dictionary,
                                                                                                          dict_index))
        self.assertEqual({(34.0, 56.0): 7.0, (40.0, 4.0): 4.0, (43.0, 9.4): 3.0}, project.get_field_data("marbles",
                                                                                                         dictionary,
                                                                                                         dict_index))
        self.assertEqual({(34.0, 56.0): 14.0, (40.0, 4.0): 2.0, (43.0, 9.4): 0.0}, project.get_field_data("cookies",
                                                                                                          dictionary,
                                                                                                          dict_index))


if __name__ == "__main__":
    unittest.main()
