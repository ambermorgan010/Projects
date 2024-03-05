'''
Tests for the Bigrams.
Note: The generate_words_from_bigrams test is very basic since it is extremely hard to test
due to the shear number of possibilities.
'''

import unittest

from bigrams import read_words, build_bigrams, generate_words_from_bigrams, words_to_text

class Tester(unittest.TestCase):
    def test_read_words(self):
        words = read_words('tom-swift.txt')
        self.assertEqual(42772, len(words))
        self.assertEqual(['Tom', 'Swift', 'and', 'his', 'Airship', 'by', 'Victor', 'Appleton', 'Chapter', '1'], words[:10])
        self.assertEqual(['Tom', 'Swift', 'and', 'his', 'friends,', 'trusting', 'to', 'meet', 'them', 'again.'], words[-10:])
        self.assertEqual(['Tom', 'quickly', 'picked', 'up', 'his', 'valise,', 'shutting', 'it,', 'but', 'he'], words[20009:20019])

    def test_build_bigrams(self):
        words = read_words('tom-swift.txt')
        bigram = build_bigrams(words)
        self.assertEqual(['went', 'said', 'observed', 'whispered', 'observed', 'and', 'replied', 'he', 'added'], bigram['now,"'])
        self.assertEqual({'a':['b','c','b'], 'b':['c','a'], 'c':['a','c','b']}, build_bigrams(['a','b','c','a','c','c','b','a','b']))

    def test_generate_words_from_bigrams(self):
        words = read_words('tom-swift.txt')
        bigram = build_bigrams(words)
        self.assertEqual(100, len(generate_words_from_bigrams(bigram, 100)))
        self.assertIn(generate_words_from_bigrams({'a':['b'],'b':['a']}, 5),
            (['a','b','a','b','a'], ['b','a','b','a','b']))

    def test_words_to_text(self):
        self.assertEqual('a B c', words_to_text(['a', 'B', 'c']))
        self.assertEqual('a', words_to_text(['a']))
        self.assertEqual('', words_to_text([]))

if __name__ == '__main__':
    unittest.main()
