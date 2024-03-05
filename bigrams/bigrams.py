"""
FUNCTION: Bigrams text generator.
AUTHOR: Amber Morgan
"""

import random
import subprocess


def read_words(textfilename):
    """
    Opens the file. Converts it into a list containing all the words and returns the list.
    """
    file = open(textfilename)
    words = []
    for line in file:
        words_in_line = line.strip().split()
        for word in words_in_line:
            words.append(word)
    file.close()
    return words


def build_bigrams(words):
    """
    Converts list of words into dictionary keys. Makes the items associated with each key
    the words that follows the key word in the list. Returns the dictionary.
    """
    bigrams = {}
    for i in range(len(words) - 1):
        if words[i] not in bigrams:
            bigrams[words[i]] = []
        bigrams[words[i]].append(words[i + 1])
    return bigrams


def generate_words_from_bigrams(bigram, length):
    """
    Takes a random word from the list of keys and appends to the list of generated words. Then, takes a random word
    associated with that word in the dictionary and appends that to the list. That item becomes the new key. Repeats
    until the given length is met. Returns list of generated words.
    """
    keys = list(bigram)
    generated_words = []
    random_word1 = random.choice(keys)
    while len(generated_words) < length:
        generated_words.append(random_word1)
        random_word2 = random.choice(bigram[random_word1])
        random_word1 = random_word2
    return generated_words


def words_to_text(words):
    """
    Converts the words in the list into a string with spaces in between them.
    """
    string = ''
    for word in words:
        string += word + ' '
    return string.strip()


def main():
    words = read_words('tom-swift.txt')
    bigrams_dict = build_bigrams(words)
    gen_words = generate_words_from_bigrams(bigrams_dict, 100)
    string_words = words_to_text(gen_words)
    print(string_words)
    subprocess.call(['say', string_words])


if __name__ == "__main__":
    main()