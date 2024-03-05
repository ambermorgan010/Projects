"""
FUNCTION: Plotting code for sort timing results.

AUTHOR: Amber Morgan
"""

import matplotlib.pyplot as plt

# Data to plot
merge_sort_X = []
merge_sort_Y = []
insert_sort_X = []
insert_sort_Y = []
bogosort_X = []
bogosort_Y = []

# Makes sure the data is sorted by the X values
merge_sort_X, merge_sort_Y = zip(*sorted(zip(merge_sort_X, merge_sort_Y)))
insert_sort_X, insert_sort_Y = zip(*sorted(zip(insert_sort_X, insert_sort_Y)))
bogosort_X, bogosort_Y = zip(*sorted(zip(bogosort_X, bogosort_Y)))

# Code that plots the data in a labeled graph
plt.plot(merge_sort_X, merge_sort_Y, '.-', label='Merge Sort')
plt.plot(insert_sort_X, insert_sort_Y, '.-', label='Insertion Sort')
plt.plot(bogosort_X, bogosort_Y, '.-', label='Bogosort')
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.legend()
plt.xlabel('Size of Data Set')
plt.ylabel('Computation Time (seconds)')
plt.title('Comparison of Sorting Algorithms')
plt.show()
