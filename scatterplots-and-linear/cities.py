"""
FUNCTION: Displays a scatterplot from a file of data on cities in the US.
AUTHOR: Amber Morgan
"""
import matplotlib.pyplot as plt
def read_cities():
    """
    Separates and categorizes the data provided in the file. Creates a list of cities and
    a list of attributes associated with each one.
    """
    file = open('us-cities.csv')
    cities = {}
    for line in file:
        city = line.strip().split(',')
        population = int(city[1])
        lat = float(city[2])
        long = float(city[3])
        surrounding = list(city[4:])
        cities[city[0]] = [population, lat, long, surrounding]
    file.close()
    return cities

def main():
    """
    Creates a scatterplot of cities using latitude and longitude as x and y axes.
    Points are scaled based on population.
    """
    cities = read_cities()
    X = []
    Y = []
    sizes = []
    for city in cities:
        city_info = cities[city]
        X.append(city_info[2])
        Y.append(city_info[1])
        sizes.append(city_info[0] / 25000)
        plt.annotate(city, xy=(city_info[2], city_info[1]))

    # Plot them
    plt.scatter(X, Y, s=sizes)
    plt.show()


if __name__ == '__main__':
    main()
