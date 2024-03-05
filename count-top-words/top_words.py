"""
FUNCTION: Gets the counts for all of the words in a file and shows the top ones.

NAME: Amber Morgan
"""


def strip_non_letters(text):
    """
    Removes all non-letters from the beginning and end of the given string.

    The first loop continues as long as the text has at least 1 character and
    the first letter in the text is not a letter. Each iteration of the loop
    the first letter is removed.

    The second loop checks if the last character is not a letter, and during
    each iteration the last letter is removed.

    Finally, it returns the string.
    """
    text = text.strip()
    while len(text) > 0 and not text[0].isalpha():
        text = text[1:]
    while len(text) > 0 and not text[-1].isalpha():
        text = text[:-1]
    return text


def get_word_counts(filename):
    """
    Gets the word counts in a file. Returns a dictionary with the key as the
    word and the value as the count of the number of times the word appeared in
    the file.

    Words are all converted to lowercase, and all non-letters are stripped from
    the ends of the word using the function strip_non_letters. If the word has
    no letters in it after the stripping then it is not placed in the dictionary.
    """
    file = open(filename)
    words = {}
    for line in file:
        groupings = line.lower().split(' ')
        for word in groupings:
            word = strip_non_letters(word)
            if word != '':
                if word not in words:
                    words[word] = 0
                words[word] += 1
    file.close()
    return words


def get_item_count(item):
    """
    Gets the count then the word from a word, count item tuple.

    The count is the second element in "item" and the word is the first element
    in "item".
    """
    item_count = [item[1], item[0]]
    return item_count


def get_top_counts(counts, top_number):
    """
    This takes a dictionary where the values are the counts of how many times
    the key shows up. This returns a list with the top_number keys and counts
    in it. For example, if top_number is 3, then this returns the 3 items with
    the highest counts.
    """
    # Get the items of counts as a list
    items = list(counts.items())

    # Sort the items, first by their count then by the word if there is a tie.
    # The highest count item comes first.
    items.sort(key=get_item_count, reverse=True)

    return items[:top_number]


def main():
    word_counts = get_word_counts('constitution.txt')
    top_word_counts = get_top_counts(word_counts, 100)
    print('The top 100 words in the constitution are:')
    for word, count in top_word_counts:
        print(word, 'which shows up', count, 'times')


if __name__ == "__main__":
    main()
