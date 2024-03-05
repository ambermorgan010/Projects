"""
PURPOSE: Creates a choropleth of a select field (user input) in a county stats file.
AUTHOR: Amber Morgan
SUBJECT: Political Science
CSV SOURCE: https://www.kaggle.com/etsc9287/2020-general-election-polls
SHAPEFILE SOURCE: https://eric.clst.org/tech/usgeojson/
NOTE: Edited the file in Google Sheets to include FIPS codes for easier organization.
As it is, the code only prints the contiguous US. However, line 126 (commented out) has the code for US + Alaska &
Hawaii.
"""

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from shapely import geometry


def unpack_data_file(filename):
    """
    Opens the given file. Creates dictionary with the FIPS code as a key & a list of the stats as the value. Creates
    list of the available field names. Removes lat & long fields, as they are not stats. Returns stat dictionary & field
    list.
    """
    file = open(filename)
    counties = {}
    field_names = []
    for line in file:
        data = line.split(",")
        if data[0] != "FIPS":  # assigns FIPS code with data (excluding state & county name)
            counties[data[0]] = data[3:]
        else:  # separates fields from data
            field_names = [x.strip().lower() for x in data[3:]]
    # invalid fields
    field_names.remove("lat")
    field_names.remove("long")
    file.close()
    return counties, field_names


def get_user_input(options):
    """
    Gets user input containing a field from the available information. Returns input as str.
    """
    print("Enter a field from the list:", end="")
    text = ""
    for option in options:
        text += " " + option + ","
    text = text[:-1]  # removes comma
    print("{}".format(text))
    user_input = input("Input field of information: ")
    while user_input.lower() not in options:
        user_input = input("Invalid input: ")
    return user_input.lower()


def get_field_data(field, dictionary, dict_index):
    """
    Finds the index of the user input field. Creates a dictionary with tuple (long, lat) as the key and the value of the
    given field as the value. Returns dictionary.
    field: user input field
    dictionary: dictionary containing all stats organized by county
    dict_index: list containing all the stat fields (used to find index of given field)
    """
    index = dict_index.index(field)
    loc_to_field = {(float(value[10]), float(value[11])): float(value[index]) for key, value in dictionary.items()}
    return loc_to_field


def get_colorizer(cmap, metrics):
    """
    This function returns a function that can be used as a feature styler.
    cmap: ScalarMappable (to determine the colors to use)
    metrics: dictionary with tuple (long, lat) as keys and the metric for the value
    """
    def colorizer(geom):
        metric = None
        point_lst = {}
        for lat, long in metrics:  # creates dict with coordinate tuple for key & Point for value
            point_lst[(lat, long)] = geometry.Point(long, lat)
        for point in point_lst:
            if geom.contains(point_lst[point]):
                metric = metrics[point]  # gets geometry.point from dict
        if metric is None:
            return {'facecolor': 'none'}
        else:
            return {'facecolor': cmap.to_rgba(metric)}
    return colorizer


def color_choropleth(ax, counties, field_dict, cmap):
    """
    Creates choropleth by coloring each county on the map according to the metric value.
    ax: GeoAxes to be plotted on
    counties: ShapelyFeature to color
    field_dict: dictionary with tuple (long, lat) as keys and metric as values
    cmap: name of the colormap to be used
    """
    mn = min(field_dict.values())
    mx = max(field_dict.values())
    norm = Normalize(vmin=mn, vmax=mx)
    colors = plt.cm.ScalarMappable(norm, cmap)
    ax.add_feature(counties, edgecolor='gray', styler=get_colorizer(colors, field_dict))
    plt.colorbar(colors, ax=ax)

def main():
    county_data_dict, dict_index = unpack_data_file("FIPS County Stats - county_statistics.csv")
    field = get_user_input(dict_index)
    county_field_data = get_field_data(field, county_data_dict, dict_index)

    reader = shpreader.Reader("gz_2010_us_050_00_20m/gz_2010_us_050_00_20m.shp")
    counties = list(reader.geometries())
    COUNTIES = cfeature.ShapelyFeature(counties, ccrs.PlateCarree())

    plt.figure(figsize=(10, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.add_feature(cfeature.LAND.with_scale('50m'))
    ax.add_feature(cfeature.OCEAN.with_scale('50m'))
    ax.add_feature(cfeature.LAKES.with_scale('50m'))
    ax.coastlines('50m')

    # sets viewable area (longitudes and latitudes)
    # This iteration contains Hawaii & Alaska, but makes the US counties too difficult to see.
    # ax.set_extent([-175, -66, 71, 17])

    # sets viewable area for contiguous US
    ax.set_extent([-125, -66, 50, 24])

    color_choropleth(ax, COUNTIES, county_field_data, "magma")  # makes choropleth

    plt.show()


if __name__ == "__main__":
    main()
