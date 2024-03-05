"""
FUNCTION: These are all of the question types utilized in questions.py.
AUTHOR: Amber Morgan
"""


def ask_yes_no_question(question):
    """
    Asks a yes or no question and returns it as True or False.
    """
    print(question)
    answer = input("Yes or no: ")
    answer = answer.lower()
    possible = ["yes", "y", "no", "n"]
    while answer not in possible:
        answer = input("Invalid. Please answer yes or no: ")
        answer = answer.lower()
    if answer == "yes" or answer == "y":
        return True
    else:
        return False


def ask_multiple_choice_question(question, options):
    """
    Asks a multiple choice questions, displays the options, and returns the selection.
    """
    print(question)
    for letter in options:
        print(letter, options[letter])
    answer = input("Enter the corresponding letter to your choice: ")
    while answer.lower() not in options:
        answer = input("Invalid. Please select one of the options above: ")
    return answer.lower()


def ask_numerical_question(question, lower, upper):
    """
    Asks a question and uses the lower and upper bounds to ensure the integer is valid. Returns integer.
    """
    print(question)
    if lower is None and upper is None:
        integer = input("Enter an integer: ")
        while not integer.strip("-").isdigit():
            integer = input("Invalid. Please enter an integer: ")
    elif lower is None:
        integer = input("Enter an integer (maximum: {}): ".format(upper))
        while not integer.strip("-").isdigit() or int(integer) > upper:
            integer = input("Invalid. Please enter an integer less than {}: ".format(upper))
    elif upper is None:
        integer = input("Enter an integer (minimum: {}): ".format(lower))
        while not integer.strip("-").isdigit() or int(integer) < lower:
            integer = input("Invalid. Please enter an integer greater than {}: ".format(lower))
    else:
        integer = input("Enter an integer from {} to {}: ".format(lower, upper))
        while not integer.strip("-").isdigit() or int(integer) < lower or int(integer) > upper:
            integer = input("Invalid. Please enter an integer between {} and {}: ".format(lower, upper))
    return int(integer)
