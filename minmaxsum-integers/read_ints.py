'''
PURPOSE: Calculates the minimum, maximum, and sum of user-input integers.

INPUT: The first input is the number of values the user will type in, then the user
types in that many integers (positive or negative).

OUTPUT: The minimum, maximum, and sum of the numbers.

AUTHOR: Amber Morgan
'''


def read_number_of_values():
    """
    Reads a non-negative integer from the user that will be the number of other integers to
    read from the user. Returns an integer.
    """
    read = input("How many ints should be read? ")
    while not read.isdigit():
        read = input("Invalid. Enter a positive integer: ")
    return int(read)


def is_int(string):
    """
    Checks if the given string represents an integer. This returns True if
    the string is all digits or if the first character of the string is the minus sign and
    every character after that is a digit. False is return in all other cases.
    """
    if string == '':
        return False
    elif string.isdigit() or string[0] == '-' and string[1:].isdigit():
        return True
    else:
        return False


def read_int():
    """
    Reads a postive or negative integer from the user, re-prompting the user if they give invalid input.
    This calls the function is_int() to check if what the user typed in is an integer.
    """
    integer = input("Add an integer: ")
    while not is_int(integer):
        integer = input("Invalid integer. Try again: ")
    return int(integer)


def read_ints():
    """
    Reads a list of integers from the user and returns it. First, this gets the number of values that
    will be in the list (using read_number_of_values()) and then repeatadly calls read_int() that
    many times, adding each entered integer to a list of integers.
    """
    int_lst = []
    reads = read_number_of_values()
    for i in range(reads):
        integer = read_int()
        int_lst.append(integer)
    return int_lst


def main():
    data = read_ints()
    print("The min is", min(data))
    print("The max is", max(data))
    print("The sum is", sum(data))


if __name__ == "__main__":
    main()
