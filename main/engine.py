import random

# My Imports
from datadef import error_population, list_map_tiles

# Define array for data saving
map_data = []
map_growing_rate = []


def initializeRandomMap(x, y):
    global map_data, map_growing_rate

    # We'll fillout all array with valid and random information
    if x > 0 and y > 0:
        for AxisX in (x):
            for AxisY in (y):
                map_data[AxisX, AxisY] = random.choice(list_map_tiles)
                map_growing_rate[AxisX, AxisY] = 1
    else:
        return False

    # Define the City Center spot
    rand_x = int(x / 2) + random.randint(-2, 2)
    rand_y = int(y / 2) + random.randint(-2, 2)
    map_data[rand_x, rand_y] = '00091'
    map_growing_rate[rand_x, rand_y] = 10

    return True


def initializeSchematicMap(x, y, cx=x / 2, cy=y / 2):
    # Return amount of population in the city
    global map_data, map_growing_rate

    # We'll generate a city with an specific center
    if x > 0 and y > 0:
        if cx > (x / 4) or cy > (y / 4):
            return error_population['OUT_OF_CENTER']

        # Define the City Center spot
        if map_data[cx, cy] != '00091':
            map_data[cx, cy] = '00091'
            map_growing_rate[cx, cy] = 10

    else:
        return error_population['NO_LIMITS']


def showMap(x, y):
    # Print the Map structure

    if x > 0 and y > 0:
        for AxisX in (x):
            print "<tr>"

            for AxisY in (y):
                print '<td title="Growing Rate: ' + \
                      map_growing_rate[AxisX, AxisY] + '">' + \
                      map_data[AxisX, AxisY] + "</td>"

            print "</tr>"
