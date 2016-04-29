import random

# My Imports
from datadef import error_population, list_map_tiles
from collections import defaultdict

# Local Constants
infPoint = 8

# Define array for data saving
map_data = defaultdict(lambda: defaultdict(int))
map_growing_rate = defaultdict(lambda: defaultdict(int))


def initializeRandomMap(x, y):
    global map_data, map_growing_rate

    # We'll fillout all array with valid and random information
    if x > 0 and y > 0:
        for AxisX in range(0, x):
            for AxisY in range(0, y):
                map_data[AxisX][AxisY] = random.choice(list_map_tiles)
                map_growing_rate[AxisX][AxisY] = 1
    else:
        return False

    # Define the City Center spot
    rand_x = int(x / 2) + random.randint(-2, 2)
    rand_y = int(y / 2) + random.randint(-2, 2)
    map_data[rand_x, rand_y] = '00091'
    map_growing_rate[rand_x, rand_y] = 10

    return True


def initializeSchematicMap(x, y, cx, cy):
    # Return amount of population in the city or error_population code.
    global map_data, map_growing_rate

    if cx > x:
        cx = x / 2
    if cy > y:
        cy = y / 2

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


def showMap(x, y, asHTML=True):
    # Print the Map structure

    if x > 0 and y > 0:
        for AxisX in range(0, x):
            if asHTML:
                print "<tr>"
            for AxisY in range(0, y):
                if asHTML:
                    print
                    # print '<td title="Growing Rate: ' + \
                    #     map_growing_rate[AxisX][AxisY] + '">' + \
                    #     str(map_data[AxisX][AxisY]) + '</td>'
                else:
                    print map_data[AxisX][AxisY]

            if asHTML:
                print "</tr>"


def evaluateCityPatern(x, y):
    # Return amount of population in the growing area.
    global map_data, map_growing_rate
