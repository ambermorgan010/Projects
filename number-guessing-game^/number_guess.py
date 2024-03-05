'''
CSCI 120 - Computer Science I
Instructors: Jeffrey Bush and Greg Schaper
Description: Lab 07 - Number Guessing Game
Teammates Names: 
'''

import random
import time


def get_guess_outcome(guessed, actual):
    """
    Checks a guessed number against an actual value. The return value is one of
    the following strings based on the difference between them:
        Your guess was too low (not even close)!
        Your guess was too low.
        Your guess was correct!
        Your guess was too high.
        Your guess was too high (not even close)!
    """
    diff = guessed - actual
    if diff < 0:
        return 'Your guess was too low.'
    elif diff < -20:
        return 'Your guess was too low (not even close)!'
    elif diff > 0:
        return 'Your guess was too high.'
    else:
        return 'Your guess was too high (not even close)!'


def get_user_guess(user_name, min_guess, max_guess):
    """
    Shows the user the range of possible numbers and then gets a user's guess
    which is an integer between min_guess and max_guess (inclusive). The prompt
    to the user includes the user's name. The input is fully validated and will
    not crash under any circumstance. Returns an int.

    For example, if called like get_user_guess("Jeff", 50, 100) this may end up
    running like the following (all things after : are user inputs):

        Jeff, enter your guess: 35
        Invalid guess, try again: apple
        Invalid guess, try again: 60

    And then returns the integer 60 (not string).

    This function only gets a *single* valid guess from the user, later you
    will call it in a loop to get multiple guesses.

    NOTE: due to user inputs this function cannot be easily automatically tested
    """
    pass



def thinking_of_a_number(user_name):
    """
    The computer "thinks" of a number and returns it. The full process is that
    a message is printed telling the user that the computer is thinking of a
    number, the computer pauses for a random number of seconds (from 1 to 10
    seconds (inclusive)), generates a random integer from 1 to 100 (inclusive),
    reports that it is ready to the user, and returns the generated number.

    For example, if this is called like thinking_of_a_number("Jeff") this would
    output:

        I am now thinking of a number...

    Then pause for a random amount of time from 1 to 10 secs and then output:

        Ok Jeff, try to guess the number now!
    
    And finally returning a random integer from 1 to 100.

    NOTE: due to printing this function cannot be easily automatically tested
    """
    pass


def display_result(username, number_of_guesses):
    """
    Displays the final result of a game with the given user. This makes sure
    the output message is accurate for the number of guesses.

    For example, if called like display_result("Jeff", 4) this would output:

        Jeff, it took you 4 guesses to get the correct number!

    And if called like display_result("Angela", 1) this would output:

        Angela, it took you 1 guess to get the correct number!

    (notice the "guess" vs "guesses" in each)
    """
    pass


def play_one_game(user_name):
    """
    Plays a single number-guessing game with the user (whose name is given as
    an argument). To play the game, the computer thinks of a number, and then
    repeatedly:
     * gets a guess from the user
     * checks the guess against the computer's number
     * prints the outcome string
     * updates the minimum and maximum allowed guesses
    That stops once the user guesses the correct number. Then, the user is
    informed how many guesses it took them.
    """
    # Initial values for several variables updated in this function
    num_guesses = 0
    min_guess = 1
    max_guess = 100
    correctly_guessed = False

    # Have the computer think of a number

    # Repeat until correctly guessed

        # Get the user's guess

        # Print the guess outcome

        # Update the minimum or maximum guess values based on the user's guess
        # or mark that it was correctly guessed

    # Display the results


def main():
    pass


if __name__ == "__main__":
    main()
