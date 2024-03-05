"""
Review of dictionary manipulation.

You can manually test the code by running it. The main function demonstrates
every one of the functions. Actual tests will be run when you push and commit.

NAME: Amber Morgan
"""

def create_dict():
    """
    Creates and returns a dictionary with the following key-value pairs:
        school -> fun
        count  -> 5
        friends -> ["Jeff", "Sue", "Billy", "Jane"]
        
    The dictionary can be created empty and then have the associations added
    or can be created with the associations already in-place.
    """
    dictionary = {"school": "fun", "count": 5, "friends": ["Jeff", "Sue", "Billy", "Jane"]}
    return dictionary


def print_friends(data):
    """
    Goes over the list associated with the key "friends" in the given
    dictionary and prints each friend on its own line.
    """
    for friend in data["friends"]:
        print(friend)


def increase_count(data):
    """
    Adds 3 to the value associated with the key "count" in the given
    dictionary.
    """
    
    data["count"] += 3

    
def print_keys(data):
    """
    Prints the keys of the dictionary with 1 key per line.
    """
    for key in data.keys():
        print(key)


def print_items(data):
    """
    Prints the key-value pairs in the given dictionary, one
    item per line.
    """
    for items in data.items():
        print(items)


def print_items_2(data):
    """
    Prints the key-value pairs in the given dictionary without using
    the .items() method. Each pair is on its own line without the extra
    () being shown like in the previous function.
    """
    for key in data:
        print(key, data[key])


def add_friend(data, new_name):
    """
    Adds a new friend with the given name to the list associated with key
    "friends" in the given dictionary.
    """
    data["friends"].append(new_name)


def print_items_sorted(data):
    """
    Prints the items in the dictionary sorted by the key field with one entry
    per line.
    """
    keys = []
    for key in data.keys():
        keys.append(key)
    key_sort = sorted(keys)
    for key in key_sort:
        print(key, data[key])


def main():
    # The main function just demonstrates the usage of the above functions.
    print("Creating dictionary")
    d = create_dict()
    print(d)
    print()
    
    print("Printing friends")
    print_friends(d)
    print()
    
    print("Increasing count")
    increase_count(d)
    print("Updated dict:", d)
    print()
    
    print("Printing keys")
    print_keys(d)
    print()

    print("Printing items")
    print_items(d)
    print()

    print("Printing items w/o using .items()")
    print_items_2(d)
    print()

    print("Adding a new friend")
    add_friend(d, "John")
    print("Updated dict:", d)
    print()

    print("Printing items sorted by key")
    print_items_sorted(d)
    print()


if __name__ == "__main__": main()
