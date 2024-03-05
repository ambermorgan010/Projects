"""
Plays the game Hangman, randomly choosing a word from the words.txt file.

AUTHORS:
"""

import random


def read_words(filename):
    """
    Read all of the words from the given file into a list.
    """
    words = []
    file = open(filename, 'r')
    for line in file:
        word = line.strip()
        words.append(word)
    file.close()
    return words


def random_item(items):
    """
    Pick a random item from the list.

    This must work for lists of any length and you should make sure that it can
    return any item from the list. See PDF for testing hints.
    """
    return '' # TODO: remove this entire line, it is simply a placeholder


def select_word():
    """
    Selects a random word to play the game with. This calls read_words() and
    random_item(), returning the result.

    Extra credit: this asks the user the level of difficulty (Python, easy, or
    hard), validates that input, and uses the corresponding filename to get the
    random word.
    """
    return '' # TODO: remove this entire line, it is simply a placeholder


def should_keep_playing(word, guessed_word, mistakes):
    """
    We want to keep playing while the guessed word is not equal to complete
    word and the number of mistakes is less than 5.

    This function does no repetition. It simply uses the parameters to
    determine if the game shoudl keep playing or not, returning True if it
    should keep playing and False the game should end.
    """
    return False # TODO: remove this entire line, it is simply a placeholder


def print_status(guessed_word, mistakes, guessed_letters):
    """
    Prints out the status of the game. For example, if called like:

        print_status("__in_", 3, ["a", "e", "i", "n", "s"])

    This would output:

        The word is: __in_
        You have made 3 out of 5 mistakes
        You have guessed: a e i n s

    This function returns nothing.
    """
    pass # TODO: remove this entire line, it is simply a placeholder


def user_guess_letter(not_allowed_letters):
    """
    Get a letter from the user. The user's input is validated to make sure it
    is a single letter, is in the alphabet, and is not one of the letters in
    the given list of not allowed letters. The returned value is lowercase.

    This function just gets 1 value from the user (that is fully validated).
    """
    return '' # TODO: remove this entire line, it is simply a placeholder


def play_round(word, guessed_word, guessed_letters, mistakes):
    """
    To play a single round of the game we need to get a letter from the user
    (that cannot be one of the letters already guessed), adds that letter to
    the list of guessed letters, if the letter is in the actual word updates
    the guessed word otherwise increases the number of mistakes.

    This returns the updated guessed word and the updated number of mistakes.
    """
    return guessed_word, mistakes # TODO: remove this entire line, it is simply a placeholder


def update_guessed_word(word, guessed_word, letter):
    """
    Create a new guessed word, replacing the corresponding _ with the guessed
    letter.

    The word is the actual word. The guessed word is one that still has some
    blanks for some of the letters. The letter is to fill in within guessed
    word.

    This goes over the indices of the word. At each position, if the letter in
    word matches the given letter, then the given letter is concatenated to the
    new guessed word. If it doesn't match then the current letter or underscore
    in guessed word in that position is concatenated to the new guessed word.
    The new guessed word is returned.
    """
    return guessed_word # TODO: remove this entire line, it is simply a placeholder


def main():
    # Get the random word from the list of words
    word = select_word()

    # Create a word that is the same length as word but is all _ characters
    guessed_word = "_" * len(word)

    # Play rounds until the guessed word is complete or the user has 5 mistakes
    guessed_letters = []
    mistakes = 0
    while should_keep_playing(word, guessed_word, mistakes):
        print_status(guessed_word, mistakes, guessed_letters)
        guessed_word, mistakes = play_round(word, guessed_word, guessed_letters, mistakes)
        print()

    # Print out the final results
    if guessed_word == word:
        print("Congratulations! The word was '"+word+"'")
    else:
        print("Too many mistakes... The word was '"+word+"'")


if __name__ == "__main__": main()
