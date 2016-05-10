import random

# My Imports
from main.datadef import range_tiles_type
from main.datadef import map_tiles_build_value, map_tiles_ground_value

# Local Constants
infPoint = 8


def percent(num1, num2):
    """ Return the percent """
    return round(num1 / num2 * 100, 2)


# **************************************************************** #
#  NEW CLASS DEFINITION                                            #
# **************************************************************** #

class CityMapTile:
    """ The tile information """

    available = 1
    tiletype = '00000'
    influence = 1
    population = 0

    def __init__(self, x, y, xorig=-1, yorig=-1):
        self.axis_x = x
        self.axis_y = y
        self.x_origin = xorig
        self.y_origin = yorig

    def movepopulation(self, population):
        self.population = population
        return population

    def moveinfluence(self, inf):
        self.influence = inf
        return inf


class CityMapBlock:
    """ The object to store each block in the City Map """

    hitpoint = 0
    hp_total = 0
    populationtotal = 0
    tileset = []

    def __init__(self, x, y, building):
        self.axis_x = x
        self.axis_y = y
        self.x_origin = x
        self.y_origin = y
        self.tilesetinit(building)

    def tilesetinit(self, building):
        """ This initiate a grid with some pre-config tiles."""
        # Here initiate random block of buildings taking in account
        # building parameter
        return

    def findnearestblock(self, direction):
        """ This search for another object in relative direction """
        return


class UserCityMap:
    """ The City Map class """

    citymapground = []
    citymap = []
    population = 0
    xcenter = 0
    ycenter = 0

    def __init__(self, xmax, ymax, terrain='GROUND', playerid=0):
        self.xmax = xmax
        self.ymax = ymax
        self.player = playerid
        self.initcitymapground(terrain, True if playerid != 0 else False)

    def initcitymapground(self, terrain, scratch):
        """ Initiate the City Map terrain randomly from scratch """
        for axis_x in range(self.xmax):
            col = []
            for axis_y in range(self.ymax):
                rangetile = random.randint(range_tiles_type[terrain][0],
                                           range_tiles_type[terrain][1])
                col.append(map_tiles_ground_value[rangetile][0])

            self.citymapground.append(col)

        if scratch:
            # Define the City Center spot
            self.xcenter = int(self.xmax / 2) + random.randint(-2, 2)
            self.ycenter = int(self.ymax / 2) + random.randint(-2, 2)
            citycenterblock = CityMapBlock(self.xcenter,
                                           self.ycenter,
                                           'CENTER')
            self.citymap.append(citycenterblock)

            # Fill up with random number of pre-done blocks
            # of Slum / Ruined / Common Houses.
            for housescount in range(random.randint(2, 6)):
                rand_x = self.xcenter + random.randint(-10, 10)
                rand_y = self.ycenter + random.randint(-10, 10)
                house_type = random.choice('SLUM_HOUSE',
                                           'RUINED_HOUSE',
                                           'COMMON_HOUSE')
                citybuild = CityMapBlock(rand_x, rand_y, house_type)
                self.citymap.append(citybuild)

    def citycenter(self):
        """ Return the axis_x and axis_y where the City Center is located. """
        return [self.xcenter, self.ycenter]

    def cityexpand(self, x, y):
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

    def cityexpandinhabitant(self, x, y):
        """ Inspect all building beside the point and raise the resident number """
        for axis_x in range(x - 1 if x - 1 >= 0 else 0,
                            x + 1 if x + 1 <= self.xmax else self.xmax):
            for axis_y in range(y - 1 if y - 1 >= 0 else 0,
                                y + 1 if y + 1 <= self.ymax else self.ymax):
                if axis_x != x and axis_y != y:
                    if percent(self.citymapinf[axis_x][axis_y],
                               self.citymapinf[x][y]) > 75:
                        self.population[axis_x][axis_y] += 1

    # TODO: Clase tile con una matriz de 5x5
    # TODO: Recorrer los tiles de la zona de influencia, desmarcando los
    # que eran "no cambiante"
