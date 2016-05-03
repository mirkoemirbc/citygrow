import random

# My Imports
from main.datadef import error_population, list_map_tiles
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
    map_data[rand_x][rand_y] = '00091'
    map_growing_rate[rand_x][rand_y] = 10

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
        if map_data[cx][cy] != '00091':
            map_data[cx][cy] = '00091'
            map_growing_rate[cx][cy] = 10
    else:
        return error_population['NO_LIMITS']


def evaluateCityGrow(x, y):
    # Return amount of population in the growing area.
    # This function evauate the influence received for all sorounding slots
    # of a given point of the map.
    global map_data, map_growing_rate

    randomizer = 20
    choisenone = 0
    for AxisX in range(x - 1, x + 1):
        for AxisY in range(y - 1, y + 1):
            if map_data[AxisX][AxisY] != 0:
                if choisenone <= 6:
                    if random.randint(0, 100) < randomizer:
                        choisenone += 1
                        randomizer = 20
                    else:
                        randomizer += 25
                    if choisenone <= 4:
                        map_growing_rate[AxisX][AxisY] += random.randint(1, 4)
                    else:
                        map_growing_rate[AxisX][AxisY] += 1
                else:
                    break


def findCityCenter(x, y):
    # This function will find and return the AxisX and AxisY where
    # the City Center is located.
    for AxisX in range(0, x):
        for AxisY in range(0, y):
            if map_data[AxisX][AxisY] == '00091':
                return AxisX, AxisY

    return 0, 0


# **************************************************************** #
#                    BORRON Y CUENTA NUEVA                         #
#                 OTRA FORMA DE HACER LO MISMO                     #
# **************************************************************** #
#  CLASS DEFINITION                                                #
# **************************************************************** #

class UserCityMap:
    """ The City Map class """
    def __init__(self, xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.citymap = []
        self.citymapinf = []
        self.player = 0
        self.xcenter = 0
        self.ycenter = 0
        self.initcitymap()

    def initcitymap(self):
        """ Initiate the City Map randomly """
        for axis_x in range(self.xmax):
            col = []
            inf = []
            for axis_y in range(self.ymax):
                col.append(random.choice(list_map_tiles))
                inf.append(1.0)

            self.citymapinf.append(inf)
            self.citymap.append(col)

        # Define the City Center spot
        self.xcenter = int(self.xmax / 2) + random.randint(-2, 2)
        self.ycenter = int(self.ymax / 2) + random.randint(-2, 2)
        # Change the City Center Code here
        self.citymap[self.xcenter][self.ycenter] = '00091'
        self.citymapinf[self.xcenter][self.ycenter] = 10.0

    def citycenter(self):
        """ Return the axis_x and axis_y where the City Center is located. """
        return [self.xcenter, self.ycenter]

    def citygrow(self, x, y):
        """ Evaluate a point in the map and grow the zone sorrounding """
        return
