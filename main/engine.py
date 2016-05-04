import random

# My Imports
from main.datadef import list_map_tiles
from collections import defaultdict

# Local Constants
infPoint = 8

# Define static list of tuple with tiles code and influence.
map_tiles_value = (('00000', 0.5), ('00003', 0.5), ('00011', 0.5),
                   ('00012', 1.0), ('00013', 1.0), ('00022', 1.0),
                   ('00041', 1.0), ('00061', 1.0), ('00073', 1.0),
                   ('00083', 1.0), ('00302', 1.0), ('00402', 1.0),
                   ('00501', 1.0))

map_tiles_center = ('00091', 10.0)

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
        self.citymap[self.xcenter][self.ycenter] = map_tiles_center[0]
        self.citymapinf[self.xcenter][self.ycenter] = map_tiles_center[1]

    def citycenter(self):
        """ Return the axis_x and axis_y where the City Center is located. """
        return [self.xcenter, self.ycenter]

    def citygrow(self, x, y):
        """ Evaluate a point in the map and grow the zone sorrounding """
        randomizer = 20
        choisenone = 0
        for axis_x in range(x - 1 if x - 1 >= 0 else 0,
                            x + 1 if x + 1 <= self.xmax else self.xmax):
            for axis_y in range(y - 1 if y - 1 >= 0 else 0,
                                y + 1 if y + 1 <= self.ymax else self.ymax):
                if axis_x != x and axis_y != y:
                    if choisenone <= 6:
                        if random.randint(0, 100) < randomizer:
                            choisenone += 1
                            randomizer = 20
                        else:
                            randomizer += 25
                        if choisenone <= 4:
                            rn = random.randint(1, 3) + random.random()
                            if self.citymapinf[axis_x][axis_y] + rn < self.citymapinf[x][y]:
                                self.citymapinf[axis_x][axis_y] += rn
                            else:
                                self.citymapinf[axis_x][axis_y] = self.citymapinf[x][y]
                        else:
                            if self.citymapinf[axis_x][axis_y] + 1 < self.citymapinf[x][y]:
                                self.citymapinf[axis_x][axis_y] += 1

        # TODO: recorrer los edificios cercanos al punto y sumar habitantes,
        # si ha llegado al 80% de la influencia total. Luego marcar como
        # "no cambiante".
        # TODO: Clase tile con una matriz de 5x5
        # TODO: Recorrer los tiles de la zona de influencia, desmarcando los
        # que eran "no cambiante"
