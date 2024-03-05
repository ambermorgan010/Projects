'''
PURPOSE: Count the vowels in an entire file.

AUTHOR: Amber Morgan
'''


def count_vowels(filename):
    """
    Counts and returns the number of vowels in the file with the given name. Since the file could
    be very large, the file must be read line-by-line.
    """
    file = open(filename)
    vowels = ['a', 'e', 'i', 'o', 'u']
    all_vowels = []
    for line in file:
        for character in line:
            if character.lower() in vowels:
                all_vowels.append(character)
    return len(all_vowels)


def main():
    vowel_count = count_vowels('alice.txt')
    print("There are", vowel_count, "in Alice in Wonderland")


if __name__ == "__main__":
    main()
