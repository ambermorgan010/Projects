"""
FUNCTION: Sorting timing code. This code implements three different sorting algorithms
and code to time_algorithm them.

AUTHOR: Amber Morgan
"""

import random
import timeit
from itertools import permutations


def is_sorted(data):
    """
    Checks if the values in 'data' are sorted.
    """
    for i in range(len(data) - 1):
        if data[i] > data[i+1]:
            return False  # found neighbors that are out-of-order, not sorted
    return True  # all neighbors are in-order, we are sorted


def bogosort(data):
    """
    Sorts the values within 'data' using the bogosort algorithm.
    """
    for permutation in permutations(data):
        if is_sorted(permutation):
            break  # stop - we are sorted!


def insertion_sort(data):
    """
    Sorts the values within 'data' using the insertion sort algorithm.
    """
    for i in range(1, len(data)):
        # Get the next unsorted value
        x = data[i]
        # Find where it should be inserted, shifting other elements out of the way
        j = i - 1
        while j >= 0 and x < data[j]:
            data[j+1] = data[j]
            j -= 1
        # Insert the value
        data[j+1] = x


def merge_sort(data):
    """
    Sorts the values within 'data' using the merge sort algorithm.
    """
    work = list(data)  # need a temporary copy to work with
    __merge_sort_internal(work, 0, len(data), data)


def __merge_sort_internal(work, start, stop, data):
    """
    Internal method of merge sorting, calls itself recursively with smaller
    pieces of the data until it is so small it must already be sorted.
    """
    if stop - start < 2:  # already sorted
        return
    mid = (stop + start) // 2  # midpoint of the data
    # Sort each half
    __merge_sort_internal(data, start, mid, work)
    __merge_sort_internal(data, mid, stop, work)
    # Merge, keep taking the smallest value from the start of the two halves
    i, j = start, mid
    for k in range(start, stop):
        if i < mid and (j >= stop or work[i] <= work[j]):
            data[k] = work[i]
            i += 1
        else:
            data[k] = work[j]
            j += 1


def time_algorithm(data, algorithm):
    """
    Time an algorithm giving is the list data. Returns the best time of 3
    trials, each containing enough repeats to take at least 0.2 secs.
    """
    timer = timeit.Timer(lambda: algorithm(list(data)))
    n_loops, time = timer.autorange()
    best = min(time, timer.timeit(n_loops), timer.timeit(n_loops))
    return best / n_loops


def run_timing(max_value, number_of_values):
    """
    Try running merge sort, insertion sort, and bogosort on a list of random
    integers that go from 0 to 'max_value' and contains a total of
    'number_of_values' items in the list. This will print out the timing
    results of running the algorithms.
    """
    # Get random data
    x = [random.randint(0, max_value) for _ in range(number_of_values)]

    # Run merge sort
    print("Running merge sort timing...")
    alg_time = time_algorithm(x, merge_sort)
    print("Best of 3 trials took an average of %.07f secs to sort the data" % alg_time)

    # Run insertion sort
    print("Running insertion sort timing...")
    alg_time = time_algorithm(x, insertion_sort)
    print("Best of 3 trials took an average of %.07f secs to sort the data" % alg_time)

    # Run bogosort
    print("Running bogosort timing...")
    alg_time = time_algorithm(x, bogosort)
    print("Best of 3 trials took an average of %.07f secs to sort the data" % alg_time)


def main():
    magnitude = 1000
    data_set_size = 10
    run_timing(magnitude, data_set_size)

if __name__ == "__main__":
    main()
