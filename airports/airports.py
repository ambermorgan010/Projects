"""
FUNCTION: Plots information about US airports.
AUTHOR: Amber Morgan
"""
import matplotlib.pyplot as plt

def read_airport_data(filename):
    """
    Reads airport data from the given filename into a dictionary. The key of the dictionary
    is the name of the airport; the value is a list of information about the airport
    including:
     - name
     - city
     - scheduled departures
     - performed departures
     - enplaned passengers
     - enplaned tons of freight
     - enplaned tons of mail
    """
    file = open(filename)
    airports = {}
    for line in file:
        characteristics = [line[0:21].strip(), line[21:43].strip(),
                           int(line[43:49].strip()), int(line[50:56].strip()), int(line[57:65].strip()),
                           float(line[66:75].strip()), float(line[76:85].strip())]
        airports[line[0:20].strip()] = characteristics
    file.close()
    return airports

def make_dictionary_for_city_lookup(airports):
    """
    Takes the dictionary of airports (key is airport name; value is a list of airport information).
    Returns a new dictionary with keys of city names and values that are lists of airport names.
    """
    cities = {}
    for airport in airports:
        city = airports[airport][1]
        if city not in cities:
            cities[city] = []
        cities[city].append(airport)
    return cities

def get_city_name_from_user(city_names):
    """
    Gets a city name from the user and returns it. It also makes sure that the city name is one of
    the cities in the collection of city names given.
    """
    input_city = input("Enter city name: ")
    while input_city.upper() not in city_names:
        input_city = input("Invalid. Try again: ")
    return input_city.upper()

def get_airport_info(airport_names, airport_info_dict, index):
    """
    Gets a piece of information about each airport given in the list of airport names. The
    information comes from the airport information dictionary. That dictionary has a list for each
    value, and the index is used to retrieve the appropriate piece of information.
    """
    index_info = []
    for airport in airport_names:
        index_info.append(airport_info_dict[airport][index])
    return index_info

def bar_plot(values, offset, label, color):
    """
    Uses matplotlib to display a bar plot of data. The values are the Y values, the X values are
    (0 through the length of the values minus 1) plus the offset. Thus, for 5 values and an offset
    of 0, the X values are 0, 1, 2, 3, and 4. For 3 values and an offset of 0.25, the X values are
    0.25, 1.25, and 2.25.
    """
    Y = values
    X = []
    for number in range(len(values)):
        number += offset
        X.append(number)
    plt.bar(X, Y, label=label, color=color, width=0.25)

def main():
    airports = read_airport_data('airports.txt')
    city_lookup = make_dictionary_for_city_lookup(airports)
    city_name = get_city_name_from_user(city_lookup)
    airport_names = city_lookup[city_name]
    #scheduled_departures = get_airport_info(airport_names, airports, 2)
    #performed_departures = get_airport_info(airport_names, airports, 3)
    enplaned_passengers = get_airport_info(airport_names, airports, 4)
    enplaned_tons_of_freight = get_airport_info(airport_names, airports, 5)
    enplaned_tons_of_mail = get_airport_info(airport_names, airports, 6)
    airport_names = [name.title() for name in airport_names]

    # Displays the airports in that city along with tons of freight and number of enplaned passengers
    plt.title("Airports in %s" % city_name.title())
    plt.xlabel('Airport')
    axis1 = plt.gca()

    print(enplaned_tons_of_freight)
    print(enplaned_tons_of_mail)

    bar_plot(enplaned_tons_of_freight, -0.25, 'Tons of Freight', 'r')
    bar_plot(enplaned_tons_of_mail, 0, 'Tons of Mail', 'g')
    plt.ylabel('Tons')
    axis2 = plt.twinx()
    bar_plot(enplaned_passengers, 0.25, 'Enplaned Passengers', 'b')
    plt.ylabel('Passengers')
    lines1, labels1 = axis1.get_legend_handles_labels()
    lines2, labels2 = axis2.get_legend_handles_labels()
    plt.legend(lines1 + lines2, labels1 + labels2, loc=0)
    plt.gca().set_xticks(list(range(len(airport_names))))
    plt.gca().set_xticklabels(airport_names)
    plt.show()

if __name__ == "__main__":
    main()
