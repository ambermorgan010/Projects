"""
Tests for Twilio lab.

AUTHOR: Amber Morgan
"""

import unittest

import texting


class Tester(unittest.TestCase):
    def test_format_phone_number(self):
        # These tests are already complete, run them to make sure your function is working
        self.assertEqual("(844) 387-6962", texting.format_phone_number("+18443876962"))
        self.assertEqual("(555) 867-5309", texting.format_phone_number("+15558675309"))

    def test_find_acronym_definition(self):
        self.assertEqual(("lol", "laughing out loud"), texting.find_acronym_definition("That made me Lol."))
        self.assertEqual(("lol", "laughing out loud"), texting.find_acronym_definition("lol haha"))
        self.assertEqual(("lol", "laughing out loud"), texting.find_acronym_definition("LOL"))
        self.assertEqual(("ttyl", "talk to you later"), texting.find_acronym_definition("I'll ttyl"))
        self.assertEqual(("ttyl", "talk to you later"), texting.find_acronym_definition("TTYL (:"))
        self.assertEqual(("jk", "just kidding"), texting.find_acronym_definition("Unless... jk"))
        self.assertEqual(("jk", "just kidding"), texting.find_acronym_definition("I'm JK"))
        self.assertEqual(("hru", "how are you"), texting.find_acronym_definition("hru man?"))
        self.assertEqual(("hru", "how are you"), texting.find_acronym_definition("HRU"))
        self.assertEqual(("hru", "how are you"), texting.find_acronym_definition("HRU doing?"))
        self.assertEqual(("eta", "estimated time of arrival"), texting.find_acronym_definition("What's your ETA?"))
        self.assertEqual(("eta", "estimated time of arrival"), texting.find_acronym_definition("My eta is 5pm."))
        self.assertEqual(("", ""), texting.find_acronym_definition("What time is it?"))


if __name__ == "__main__":
    unittest.main()
