'''
FUNCTION: Tests for the Roman numeral decoder.

AUTHOR: Amber Morgan
'''

import unittest

from roman_numerals import roman_numeral_to_list, compute_roman_numeral_value, decode_roman_numeral

class Tester(unittest.TestCase):
    def test_roman_numeral_to_list(self):
        self.assertEqual([1], roman_numeral_to_list('i'))
        self.assertEqual([], roman_numeral_to_list(''))
        self.assertEqual([], roman_numeral_to_list('abc'))
        self.assertEqual([1], roman_numeral_to_list('I'))
        self.assertEqual([1, 5], roman_numeral_to_list('iV'))
        self.assertEqual([1, 1, 1], roman_numeral_to_list('iii'))
        self.assertEqual([1, 10], roman_numeral_to_list('Ix'))
        self.assertEqual([1, 1], roman_numeral_to_list('ii'))
        self.assertEqual([1, 1000], roman_numeral_to_list('im'))
        self.assertEqual([500], roman_numeral_to_list('D'))
        self.assertEqual([], roman_numeral_to_list('10C'))
        # Make sure to have 10 additional tests and to cover all situations (i.e. bad inputs, basic inputs, complex inputs, mixed capitalization)

    def test_compute_roman_numeral_value(self):
        self.assertEqual(1, compute_roman_numeral_value([1]))
        self.assertEqual(6, compute_roman_numeral_value([5, 1]))
        self.assertEqual(70, compute_roman_numeral_value([50, 10, 10]))
        self.assertEqual(4, compute_roman_numeral_value([1, 5]))
        self.assertEqual(9, compute_roman_numeral_value([1, 10]))
        self.assertAlmostEqual(2.0, compute_roman_numeral_value([5.0, 7.0]), places=1)
        self.assertEqual(10, compute_roman_numeral_value([5+1, 4]))
        self.assertEqual(1005000, compute_roman_numeral_value([1000000, 5000]))
        self.assertEqual(1977, compute_roman_numeral_value([1000, 100, 1000, 50, 10, 10, 5, 1, 1]))
        self.assertEqual(14, compute_roman_numeral_value([14]))
        self.assertEqual(0, compute_roman_numeral_value([]))
        # Make sure to have 10 additional tests and to cover all situations (i.e. bad inputs, basic inputs, complex inputs)

    def test_decode_roman_numeral(self):
        self.assertEqual(1977, decode_roman_numeral('MCmLxXViI'))
        self.assertEqual(1207, decode_roman_numeral('MCCvII'))
        self.assertEqual(2506, decode_roman_numeral('MMDVI'))
        self.assertEqual(2570, decode_roman_numeral('mmdlxx'))
        self.assertEqual(2896, decode_roman_numeral('MMDCCCXCVI'))
        self.assertEqual(2702, decode_roman_numeral('MMDCCII'))
        self.assertEqual(1408, decode_roman_numeral('MCDVIII'))
        self.assertEqual(1429, decode_roman_numeral('mcdxxix'))
        self.assertEqual(2644, decode_roman_numeral('MMDCXLIV'))
        self.assertEqual(4, decode_roman_numeral('iv'))
        self.assertEqual(-1, decode_roman_numeral(''))
        # Make sure to have 10 additional tests and to cover all situations (i.e. bad inputs, basic inputs, complex inputs)

if __name__ == '__main__':
    unittest.main()
