"""
Trigrams text generator.
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


def build_trigrams(words):
    """
    Converts list of words into consecutive tuples which are used as dictionary keys.
    Makes the items associated with each key the words that follow the key
    word in the list. Returns the dictionary.
    """
    trigrams = {}
    for i in range(len(words) - 2):
        two_words = (words[i], words[i + 1])
        if two_words not in trigrams:
            trigrams[two_words] = []
        trigrams[two_words].append(words[i + 2])
    return trigrams


def generate_words_from_trigrams(trigram, length):
    """
    Takes a random word from the list of keys and appends to the list of generated words. Then, takes a random word
    associated with that word in the dictionary and appends that to the list. A new tuple is made using the new word and the word prior, which becomes the new key.
    Repeats until the given length is met. Returns list of generated words.
    """
    trigram_keys = list(trigram)
    generated_words = []
    random_word1, random_word2 = random.choice(trigram_keys)
    generated_words.append(random_word1)
    generated_words.append(random_word2)
    random_tuple = (random_word1, random_word2)
    while len(generated_words) < length:
        random_word3 = random.choice(trigram[random_tuple])
        generated_words.append(random_word3)
        random_tuple = (random_word2, random_word3)
        random_word2 = random_word3
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
    trigrams_dict = build_trigrams(words)
    gen_words = generate_words_from_trigrams(trigrams_dict, 100)
    string_words = words_to_text(gen_words)
    print(string_words)
    subprocess.call(['say', string_words])


if __name__ == "__main__":
    main()