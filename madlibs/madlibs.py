"""
FUNCTION: Plays Mad-Libs. Randomly chooses one of the three files like madlibs#.txt and
uses it to play the game, displaying the result at the very end.

AUTHOR: Amber Morgan
"""

import textwrap
import random


def is_blank(word):
    """
    Checks if a word represents a blank, i.e. it starts with 2 underscores.
    Returns True if it does and False otherwise.
    """
    if word[0:2] == "__":
        return True
    else:
        return False


def print_lines(lines):
    """
    Takes a list of strings and prints each of those strings on its own line.
    """
    for string in lines:
        print(string)


def get_description_from_blank(blank):
    """
    Gets the description from a blank. This is only called when it is sure that
    the blank parameter is a string like "__noun__". It may still have
    punctuation on the end, such as "__noun__." This function simply removes any
    extra punctuation. This returns the description of the blank.
    """
    blank = blank.strip()
    if not blank[-1].isalpha():
        blank = blank[:-1]
    blank = blank.replace("_", " ")
    return blank.strip()


def process_blank(blank):
    """
    Processes a blank from a mablib game. It is assumed that whoever calls this
    function has already checked the argument is a blank with is_blank(). This
    gets the description from the blank and uses that description as part
    of a prompt to get a word from the user. It also checks if the given blank
    ends in a punctuation (actually anything that isn't _) and copies it to the
    new word entered by the user.
    
    Returns the new word, possibly with punctuation copied to the end.
    """
    formatted_blank = get_description_from_blank(blank)
    user_input = input("Enter a/an {}: ".format(formatted_blank)).strip()
    if blank[-1] != "_":
        user_input += blank[-1]
    return user_input


def play_madlibs(madlib):
    """
    Plays a madlib game. This works by breaking the madlib into individual
    words, then going through each word. If any word is a blank then this
    processes the blank, getting a new word to replace it with. Every word
    (either non-blank words in the madlib or new words from blanks) is added to
    a growing string that is the new test. Returns the completed new story at the end.
    """
    madlib_string = ""
    text = madlib.split()
    for word in text:
        if is_blank(word):
            word = process_blank(word)
        madlib_string += word + " "
    return madlib_string.strip()


def get_random_madlib():
    """
    Returns a random madlib game. This randomly picks one of the files
    madlib1.txt, madlib2.txt, or madlib3.txt, reads it in as a single string,
    and returns that string.
    """
    madlibs = ["madlib1.txt", "madlib2.txt", "madlib3.txt"]
    madlib = open(random.choice(madlibs))
    madlib_string = ''
    for line in madlib:
        madlib_string += line
    madlib.close()
    return madlib_string


def main():
    """
    Runs the Mad-Libs game.
    """
    print("Welcome to Mad-Libs!")
    print()
    madlib = get_random_madlib()
    output = play_madlibs(madlib)
    print()
    print_lines(textwrap.wrap(output, 80))


if __name__ == "__main__":
    main()
