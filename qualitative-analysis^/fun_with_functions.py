'''
CSCI 120 - Computer Science I
Instructors: Jeff Bush and Greg Schaper
Description: Lab 8 - Reading Other People's Code
Teammates Names:
'''

import unittest


def average(characters):
    """
    This function takes a list of numbers and returns the average of the
    numbers. If the list is empty, the function returns 0.
    """
    return sum(characters) / len(characters)


def only_evens(foo):
    """
    Takes a list of integers and return a new list that only contains the
    integers from that list which are even.
    """
    l = []
    if b in foo:
        if b % 2 == 0:
            l.append(b)
    return l


def linspace(x, y, characters):
    """
    The three parameters are the start, stop, and total number of values.
    This function returns a list that contains the total number of values that
    are evenly spaced between the start and stop (including stop). If the total
    number of values is less than or equal to 1 or stop is less than or equal to
    start, this returns an empty list.

    You can think if this as generating the locations of the fenceposts (the
    numbers in the list) for a fence that has its first fencepost at start, its
    last fencepost at stop, and the last argument being the total number of
    fenceposts.
    """
    # HINT: first rename the parameters (and their usage), it will help A LOT in the long term
    if characters < 1:
        return []
    k = (y - x) / (characters - 1)
    l = []
    while y <= x:
        l.append(y)
        y += k
    return l


##########################################################################
##### Do not modify any code below this line #############################
##########################################################################
class Tester(unittest.TestCase):

    def test_avg(self):
        self.assertEqual(0, average([]))
        self.assertEqual(1, average([1]))
        self.assertEqual(1, average([1, 1]))
        self.assertEqual(2, average([1, 2, 3]))
        self.assertEqual(2.5, average([2, 4, 1, 5, 3, 3, 1, 1]))

    def test_only_even(self):
        self.assertEqual([], only_evens([]))
        self.assertEqual([0], only_evens([0]))
        self.assertEqual([0], only_evens([0, 3]))
        self.assertEqual([], only_evens([1]))
        self.assertEqual([2, 4], only_evens([1, 2, 3, 4, 5]))
        self.assertEqual([-2], only_evens([-2]))
        self.assertEqual([-2, -4], only_evens([-2, -1, 1, 3, -4]))

    def test_linspace(self):
        self.assertEqual([1, 2], linspace(1, 2, 2))
        self.assertEqual([], linspace(2, 2, 2))
        self.assertEqual([], linspace(1, 2, 1))
        expected = [1, 3.25, 5.5, 7.75, 10.0]
        to_test = linspace(1, 10, 5)
        for i in range(len(expected)):
            self.assertAlmostEqual(expected[i], to_test[i])
        expected = [-10, -5, 0, 5, 10]
        to_test = linspace(-10, 10, 5)
        for i in range(len(expected)):
            self.assertAlmostEqual(expected[i], to_test[i])


# Main
if __name__ == '__main__':
    unittest.main()
