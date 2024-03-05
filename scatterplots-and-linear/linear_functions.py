"""
FUNCTION: Graphs a comparison between 3 linear functions.
AUTHOR: Amber Morgan
"""

import matplotlib.pyplot as plt
X = []
Y = []


def main():
    x_values = []
    y_values1 = []
    y_values2 = []
    for value in range(1, 6):
        x_values.append(value)
        y_values1.append(value ** 2)
        y_values2.append(2 * (value ** 2) + value + 4)
    plt.plot(x_values, y_values1, 'b-', label='Order')  # plt.plot gives us lines
    plt.plot(x_values, y_values2, 'r--', label='Runtime')  # plt.plot gives us lines
    plt.title('Graph Comparison')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
