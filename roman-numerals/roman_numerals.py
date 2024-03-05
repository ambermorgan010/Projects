"""
FUNCTION: Decodes Roman numerals into integers.

AUTHOR: Amber Morgan
"""

def roman_numeral_to_list(numeral):
    """
    Converts a Roman numeral like MCMLXXVII to a list of integers representing
    each of the digits.
    """
    numeral_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    characters = []
    numeral = numeral.upper()
    for i in range(len(numeral)):
        if numeral[i] not in numeral_values:
            return []
        else:
            characters.append(numeral_values[numeral[i]])
    return characters

def compute_roman_numeral_value(values):
    """
    Takes a list of digits from a converted Roman numeral such as. This returns
    the numerical value following the rules of Roman numerals.
    """
    total = 0
    for i in range(len(values)):
        if values[i] is values[-1] or values[i] >= values[i+1]:
            total += values[i]
        else:
            total -= values[i]
    return total

def decode_roman_numeral(roman_numeral):
    """
    Decodes a Roman numeral.
    """
    list_of_numerals = roman_numeral_to_list(roman_numeral)
    if not list_of_numerals:
        return -1
    value = compute_roman_numeral_value(list_of_numerals)
    return value

def main():
    value = decode_roman_numeral(input("Enter a Roman numeral: "))
    while value == -1:
        value = decode_roman_numeral(input("Invalid, try again: "))
    print("The value is", value)

if __name__ == '__main__':
    main()
