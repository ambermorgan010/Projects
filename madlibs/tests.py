"""
Tests for mablibs program

AUTHOR: Amber Morgan
"""

import unittest

import madlibs


class Tester(unittest.TestCase):
    def test_is_blank(self):
        self.assertEqual(True, madlibs.is_blank("__noun__"))
        self.assertEqual(True, madlibs.is_blank("__verb_ending_in_'-ing'__"))
        self.assertEqual(False, madlibs.is_blank(""))
        self.assertEqual(False, madlibs.is_blank("catapult"))
        self.assertEqual(True, madlibs.is_blank("__verb__(previous_verb)__"))

    def test_get_description_from_blank(self):
        self.assertEqual("verb (not one from before)", madlibs.get_description_from_blank("__verb_(not_one_from_before)__"))
        self.assertEqual("verb ending in -ing", madlibs.get_description_from_blank("__verb_ending_in_-ing__"))
        self.assertEqual("verb ending in '-ed'", madlibs.get_description_from_blank("__verb_ending_in_'-ed'__"))
        self.assertEqual("noun", madlibs.get_description_from_blank("__noun__"))
        

if __name__ == "__main__":
    unittest.main()
