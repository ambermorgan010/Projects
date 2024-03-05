"""
FUNCTION: Final Practice Problems
"""

import random

#1
def strip_all_strings(lst):
    """
    Takes a list of strings and returns a new list with all strings stripped of
    extra spaces.
    """
    stripped_lst = []
    for item in lst:
        stripped_lst.append(item.strip())
    return stripped_lst

#2
def strip_all_strings_inplace(lst):
    """
    Takes a list of strings and replaces each string with the string stripped of
    extra spaces.
    """
    for i in range(len(lst)):
        lst[i] = lst[i].strip()

#3
def append_value_to_key(dictionary, key, value):
    """
    Adds the value to the list associated with the key in the dictionary. If
    there is no list associated with the key yet, an empty list is
    associated with it first.
    """
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)

    # if key not in dictionary:
    #     dictionary[key] = 1
    # else:
    #     dictionary[key] += 1

#4
def add_value_to_key(dictionary, key, value):
    """
    Adds the value to the integer associated with the key in the dictionary. If
    there is no integer associated with the key yet then it is set to 0 first.
    """
    if key not in dictionary:
        dictionary[key] = 0
    dictionary[key] += value

    # if key not in dictionary:
    #     dictionary[key] = value
    # else:
    #     dictionary[key] += value

#5
def diff(lst):
    """
    Returns a new list where each value is the difference between each pair of
    neighboring elements.
    """
    differences = []
    for i in range(len(lst) - 1):
        differences.append(lst[i + 1] - lst[i])
    return differences

#6
def get_word_lengths(string):
    """
    Takes a single string and returns a list containing the length of each word
    within the string.
    """
    lengths = []
    words = string.split()
    for word in words:
        lengths.append(len(word))
    return lengths

#7
def multiplication_table(n):
    """
    Prints an n-by-n multiplication table. The numbers are separated by
    whitespace and nicely line up in the output.
    """
    for row in range(n+1):
        for column in range(n+1):
            print("{:3d}".format(row*column), end=" ")
        print()

#8
def random_numbers(min, max, count):
    """
    Generates a list of random integers from min to max. A
    total of count integers are in the list. Returns the list.
    """
    integers = []
    for i in range(count):
        integers.append(random.randint(min, max))
    return integers

#9
def local_maxima(data):
    """
    Makes a list of all of the numbers in data which are larger than both the
    number before and after it in the list. Returns the list of local maxima.
    """
    larger_nums = []
    for i in range(1, len(data) - 1):
        if data[i-1] < data[i] > data[i+1]:
            larger_nums.append(data[i])
    return larger_nums

#10
def get_positions(string, letter):
    """
    Gets the list of positions of the given letter within the given string.
    """
    indexes = []
    for i in range(len(string)):
        if string[i] == letter:
            indexes.append(i)
    return indexes

#11
def count_letters(string):
    """
    Calculates the frequency of each letter, returning a dictionary where the
    letters are the keys and the values are the counts.
    """
    letter_occurrence = {}
    for letter in string:
        if letter.isalpha():
            letter = letter.lower()
            if letter not in letter_occurrence:
                letter_occurrence[letter] = 0
            letter_occurrence[letter] += 1
    return letter_occurrence

#12
def ball_dance(dancers):
    """
    Takes a list of names of dancers and returns a new list made of all the
    possible pairs of dancers. There are only two rules for pairing:
      1) A dancer cannot be paired with themselves.
      2) If A is already paired with B, then B cannot be paired with A.
    """
    pairs = []
    for i in range(len(dancers)):
        for i2 in range(i+1, len(dancers)):
            pairs.append([dancers[i], dancers[i2]])
    return pairs


#13
def addition(string):
    """
    Takes a string that has numbers and plus signs like '4+15+6+9' and returns
    the sum of all of the numbers.
    """
    # support addition & subtraction
    signs = []
    numbers = ""
    for character in string:
        if character.isdigit():
            numbers += character
        else:
            signs.append(character)
            numbers += ","
    numbers_lst = numbers.split(",")
    answer = int(numbers_lst[0])
    for i in range(len(signs)):
        if signs[i] == "+":
            answer += int(numbers_lst[i+1])
        elif signs[i] == "-":
            answer -= int(numbers_lst[i+1])
        elif signs[i] == "/":
            answer /= int(numbers_lst[i+1])
        elif signs[i] == "*":
            answer *= int(numbers_lst[i+1])
    return answer

#14
def get_duplicates(lst):
    """
    Returns a list containing all values that show up more than once in the given
    list.
    """
    values_freq = {}
    repeats = []
    for item in lst:
        if item not in values_freq:
            values_freq[item] = 0
        values_freq[item] += 1
    for key in values_freq:
        if values_freq[key] > 1:
            repeats.append(key)
    return repeats

#15
def common_values(list_1, list_2):
    """
    Returns a new list that contains the values that show up in both list_1 and
    list_2. Duplicates are only shown once in the return value.
    """
    return list(set(list_1) & set(list_2))

def main():
    print("#1 strip_all_strings(['a ', ' b', 'c', ' d '])")
    stripped_list = strip_all_strings(['a ', ' b', 'c', ' d '])
    print("Returns ", stripped_list)
    print()

    print("#2")
    print("my_list = ['a ', ' b', 'c', ' d ']")
    print("strip_all_strings_inplace(my_list)")
    my_list = ['a ', ' b', 'c', ' d ']
    strip_all_strings_inplace(my_list)
    print("my_list is now ", my_list)
    print()

    print("#3")
    print("my_data = {5:['hi'], 'foo':['bar']}")
    print("append_value_to_key(my_data, 5, 'hello')")
    print("append_value_to_key(my_data, 5, 'world')")
    print("append_value_to_key(my_data, 'code', 'neat')")
    my_data = {5:['hi'], 'foo':['bar']}
    append_value_to_key(my_data, 5, 'hello')
    append_value_to_key(my_data, 5, 'world')
    append_value_to_key(my_data, 'code', 'neat')
    print("my_data is now ", my_data)
    print()

    print("#4")
    my_data = {'blue': 7, 'red': 7, 'green': 16, 'yellow': 30}
    print("my_data =", my_data)
    print("add_value_to_key(my_data, 'red', 6)")
    print("add_value_to_key(my_data, 'green', 7)")
    print("add_value_to_key(my_data, 'purple', 0)")
    print("add_value_to_key(my_data, 'orange', 100)")
    add_value_to_key(my_data, 'red', 6)
    add_value_to_key(my_data, 'green', 7)
    add_value_to_key(my_data, 'purple', 0)
    add_value_to_key(my_data, 'orange', 100)
    print("my_data is now ", my_data)
    print()

    print("#5")
    print("diff([5, 4, 1, 6, 2, 1, 0, -5, 6, 8])")
    differences = diff([5, 4, 1, 6, 2, 1, 0, -5, 6, 8])
    print("Returns ", differences)
    print()

    print("#6")
    print("get_word_lengths('hello world foo bar this. is. coding.')")
    lengths = get_word_lengths('hello world foo bar this. is. coding.')
    print("Returns ", lengths)
    print()

    print("#7")
    print("multiplication_table(10)")
    multiplication_table(10)
    print()

    print("#8")
    print("random_numbers(0, 1000, 100)")
    rnd_lst = random_numbers(0, 1000, 100)
    print("Returns ", rnd_lst)
    print()

    print("#9")
    print("local_maxima([1, 2, 4, 5, 3, 6, 7, 2, 1, 4, 3, 5])")
    maxima = local_maxima([1, 2, 4, 5, 3, 6, 7, 2, 1, 4, 3, 5])
    print("Returns ", maxima)
    print()

    print("#10")
    print("get_positions('Mississippi', 'i')")
    pos = get_positions('Mississippi', 'i')
    print("Returns ", pos)
    print()

    print("#11")
    print("count_letters('Mississippi.m; 0')")
    counts = count_letters('Mississippi.m; 0')
    print("Returns ", counts)
    print()

    print("#12")
    print("ball_dance(['john', 'mary', 'paul', 'gloria'])")
    dancer_pairs = ball_dance(['john', 'mary', 'paul', 'gloria'])
    print("Returns ", dancer_pairs)
    print()

    print("#13")
    print("addition('4+5+19+0+2')")
    sum = addition('4+5+19+0+2')
    print("Returns ", sum)
    print()

    print("#14")
    print("get_duplicates(['hello', 'world', 'foo', 'hello', 'World', 'bar', 'foo'])")
    dups = get_duplicates(['hello', 'world', 'foo', 'hello', 'World', 'bar', 'foo'])
    print("Returns ", dups)
    print()

    print("#15")
    print("common_values(['a', 'b', 'c', 'r', 'b', 2, 8, 4, 'x'], ['a', 'd', 'b', 4, 'e', 'f', 'c', 4, 'y'])")
    common = common_values(['a', 'b', 'c', 'r', 'b', 2, 8, 4, 'x'], ['a', 'd', 'b', 4, 'e', 'f', 'c', 4, 'y'])
    print("Returns ", common)
    print()


if __name__ == "__main__": main()
