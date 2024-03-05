"""
FUNCTION: Plotting Tool. Asks the user for plot information (title and X/Y labels); then, gets all points from
the user. Once they enter 0,0 the scatter plot is shown with all of the data.

AUTHOR: Amber Morgan
"""

from matplotlib.pylab import plt

def is_int(x):
    """
    Checks if a string represents a positive or negative integer. Returns True if it does and False
    otherwise.
    """
    return (x.isdigit() or (x[:1] == '-' and x[1:].isdigit()))

def is_float(x):
    """
    Checks if a string represents a positive or negative floating point number. Returns True if it
    does and False otherwise.
    """
    # Anything that is an integer can be converted to a float
    if is_int(x):
        return True
    parts = x.split('.')
    return len(parts) == 2 and is_int(parts[0]) and parts[1].isdigit()

def get_point():
    """
    Gets a point from the user. Each point is entered as a comma-seperated x and y value each of
    which is a floating point number (for example -3.4,5.6 is valid). This function returns the x and
    y values converted to floats after validating the user input.
    """
    input_point = input("Enter a point like x,y: ")
    points = input_point.split(",")
    while len(points) != 2 or not is_float(points[0]) or not is_float(points[1]):
        input_point = input("Invalid, try again: ")
        points = input_point.split(",")
    return float(points[0]), float(points[1])

def get_points():
    """
    Gets many points from the user and returns two lists: one of x values and one of y values.
    
    The user can keep entering points until they enter the point 0,0. This returns lists of
    all the x and y values up to but not including the 0,0 point.
    """
    print("Now enter the data. Enter 0,0 to stop.")
    x_values = []
    y_values = []
    x, y = get_point()
    while x != 0 or y != 0:
        x_values.append(float(x))
        y_values.append(float(y))
        x, y = get_point()
    return x_values, y_values

def main():
    title = input("Plot Title: ")
    x_label = input("X Label: ")
    y_label = input("Y Label: ")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    X, Y = get_points()
    plt.scatter(X, Y)
    plt.show()


if __name__ == "__main__":
    main()
