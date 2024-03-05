"""
This program is for studying how string slicing and the upper() and lower()
methods work in Python.

AUTHOR: Amber Morgan
"""


def main():
    my_str = "Hello World"

    print(my_str[3:7])
    print(my_str.lower())
    print(my_str.upper())

    # print out HELLO and world on two separate lines.
    print(my_str[0:5].upper())
    print(my_str[6:11].lower())


if __name__ == "__main__":
    main()
