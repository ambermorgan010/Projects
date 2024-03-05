"""
FUNCTION: Displays a scatterplot from a file of data on colleges in Lehigh Valley.
AUTHOR: Amber Morgan
"""
import matplotlib.pyplot as plt


def separate_schools(filename):
    """
    Separates and categorizes the data provided in the file. Creates a list of colleges and
    a list of attributes associated with each one.
    """
    file = open(filename)
    colleges = {}
    for line in file:
        school_data = line.split(",")
        name = school_data[0]
        long = float(school_data[1])
        lat = float(school_data[2])
        enrollment = int(school_data[3])
        prim_color = school_data[4]
        sec_color = school_data[5].strip()
        colleges[name] = [long, lat, enrollment, prim_color, sec_color]
    return colleges


def main():
    """
    Creates a scatterplot of schools using latitude and longitude as x and y axes.
    Points are scaled based on enrollment and colored to match primary and secondary
    colors (if applicable).
    """
    colleges = separate_schools("lv-schools.csv")
    X = []
    Y = []
    enrollment = []
    colors = []
    secondary_colors = []
    for college in colleges:
        X.append(colleges[college][0])
        Y.append(colleges[college][1])
        enrollment.append(colleges[college][2] / 10)
        colors.append(colleges[college][3])
        secondary_colors.append(colleges[college][4])
        plt.annotate(college, xy=(colleges[college][2], colleges[college][1]))
    plt.scatter(X, Y, s=enrollment, color=colors, edgecolors=secondary_colors)
    plt.show()


if __name__ == '__main__':
    main()
