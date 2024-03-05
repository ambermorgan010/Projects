"""
PURPOSE: Character find and replace. Replace all occurrences of the "find" character with the "replace"
character.

INPUT:
    1) Any string of characters
    2) A single character to find in the input string
    3) A character to replace the find character with

OUTPUT: The input string modified by replacing every instance of the
character to find with the replace character.

AUTHOR: Amber Morgan
"""

def get_text_from_user(prompt):
    """
    Gets a line of text from the user. The returned string is converted to lowercase
    before being returned.
    """
    return input(prompt).lower()


def get_letter_from_user(prompt, not_allowed):
    """
    Gets a single letter from the user after showing the given prompt. Validates the user input to
    make sure that it is a single letter and converts it to lowercase. It also makes sure that it
    does not match the 'not_allowed' parameter.
    """
    ltr = input(prompt).lower()
    while len(ltr) != 1 or not ltr.isalnum() or ltr.isdigit() or ltr == not_allowed:
        ltr = input("Invalid letter, try again: ").lower()
    return ltr



def main():
    text = get_text_from_user("Enter some text: ")
    ltr1 = get_letter_from_user("Enter a letter: ", '') # Get any letter
    ltr2 = get_letter_from_user("Enter another letter: ", ltr1) # Get a letter that doesn't match the first letter
    new_text = text.replace(ltr1, ltr2)
    print("The new text is", new_text)


if __name__ == "__main__":
    main()
