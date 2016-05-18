import random

# My Imports
from main.datadef import range_tiles_type, range_block_type
from main.datadef import map_block_code, map_tiles_ground_value

# Local Constants
infPoint = 8


def percent(num1, num2):
    """ Return the percent """
    return round(num1 / num2 * 100, 2)


# **************************************************************** #
#  NEW CLASS DEFINITION                                            #
# **************************************************************** #

class CityMapBlock:
    """ The object to store each block in the City Map """

    hitpoint = 0
    hp_total = 0
    population_block = 0
    blocktileset = 10000
    health_level = 0

    def __init__(self, x, y, building, scratch=True, height=5, width=5):
        self.axis_x = x
        self.axis_y = y
        self.x_origin = x
        self.y_origin = y
        self.height = height
        self.width = width
        if scratch:
            self.blocktilesetinit(building)

    def blocktilesetoverlap(self, neighbour):
        """ This determines if this block is overlapping another block """
        # Calculate xsup,ysup and xinf,yinf. This way we know the block.
        # Take in account the outter columns and rows as just road.
        xinf = self.x_origin
        yinf = self.y_origin

        xsup = xinf + self.width - 2
        ysup = yinf + self.height - 2

        # Calculate xsup,ysup and xinf,yinf for neighbour block.
        # For Neighbour, we'll consider the roads as well.
        xinf_neighbour = neighbour.x_origin - 1
        yinf_neighbour = neighbour.y_origin - 1

        xsup_neighbour = xinf_neighbour + neighbour.width
        ysup_neighbour = yinf_neighbour + neighbour.height

        # Return True if the neighbour block is within this block borders.
        # Check out every BORDER.
        if (xinf_neighbour >= xinf and yinf_neighbour >= yinf) and \
           (xinf_neighbour <= xsup and yinf_neighbour <= ysup):
           return True
        elif (xsup_neighbour >= xinf and ysup_neighbour >= yinf) and \
           (xsup_neighbour <= xsup and ysup_neighbour <= ysup):
           return True
        else:
           return False

    def findnearestblock(self, direction):
        """ This search for another object in relative direction """
        return

    def blocktilesetinit(self, building):
        """ This will set the initial parameters for the completely block """
        initialcode = random.choice(range_block_type[building])
        self.blocktileset = initialcode
        return initialcode

    def blocktileset_per_population(self, inhabitants):
        """ Returns the tilesetcode of the block taking in account population """
        if self.blocktileset >= 10000 and self.blocktileset < 20000:
            return self.blocktileset + int(self.blocktileset / 20)
        else:
            return self.blocktileset


class UserCityMap:
    """ The City Map class """

    citymapground = []
    citymap = []
    populationtotal = 0
    populationmilitartotal = 0
    populationidletotal = 0
    populationworkertotal = 0
    xcenter = 0
    ycenter = 0

    def __init__(self, xmax, ymax, terrain='GROUND', playerid=0):
        self.xmax = xmax
        self.ymax = ymax
        self.player = playerid
        self.initcitymapground(terrain, True if playerid == 0 else False)

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
            # of Slum / Ruined Houses.
            for housescount in range(random.randint(2, 8)):
                range_inf = -10 if self.xcenter - 10 > 0 else 1
                range_sup = 10 if self.xcenter + 10 < self.xmax - 5 else self.xmax - 5
                rand_x = self.xcenter + random.randint(range_inf, range_sup)
                range_inf = -10 if self.ycenter - 10 > 5 else 5
                range_sup = 10 if self.ycenter + 10 < self.ymax - 5 else self.xmax - 5
                rand_y = self.ycenter + random.randint(range_inf, range_sup)

                house_type = random.choice(('SLUM_HOUSE',
                                           'RUINED_HOUSE'))
                citybuild = CityMapBlock(rand_x, rand_y, house_type)
                citybuild.population_block = random.randint(1, 4)

                # Control that the new block doesn't overlap another in map
                for tempmap in self.citymap:
                    tabstr = '.' * len(self.citymap)
                    if citybuild.blocktilesetoverlap(tempmap):
                        print(tabstr + "OVERLAP!! [map: " + str(tempmap.x_origin) + 
                              "," + str(tempmap.y_origin) + "] [new: " +
                              str(citybuild.x_origin) + "," + str(citybuild.x_origin) + "]")
                        while citybuild.blocktilesetoverlap(tempmap):
                            # import ipdb; ipdb.set_trace()
                            overrand_x = self.xcenter + random.randint(range_inf, range_sup)
                            citybuild.x_origin = overrand_x
                            overrand_y = self.ycenter + random.randint(range_inf, range_sup)
                            citybuild.y_origin = overrand_y
                    else:
                        print(tabstr + "NOT OVERLAP!!")

                # Add the new block into the citymap.
                self.citymap.append(citybuild)
                self.populationtotal += citybuild.population_block

            self.populationidletotal = self.populationtotal

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
        # si ha llegado al 75% de la influencia total. Luego marcar como
        # "no cambiante".

    def cityexpandinhabitant(self, x, y):
        """ Inspect all blocks around the point and raise resident number """
        for axis_x in range(x - 1 if x - 1 >= 0 else 0,
                            x + 1 if x + 1 <= self.xmax else self.xmax):
            for axis_y in range(y - 1 if y - 1 >= 0 else 0,
                                y + 1 if y + 1 <= self.ymax else self.ymax):
                if axis_x != x and axis_y != y:
                    if percent(self.citymapinf[axis_x][axis_y],
                               self.citymapinf[x][y]) > 75:
                        self.populationtotal[axis_x][axis_y] += 1

    # TODO: Recorrer los tiles de la zona de influencia, desmarcando los
    # que eran "no cambiante"

    def citymapprintcoord(self):
        """ This function is only for console use """
        for i, listelem in enumerate(self.citymap):
            print("[" + str(i) + "] (" + str(listelem.axis_x) +
                  "," + str(listelem.axis_y) + ") [W:" +
                  str(listelem.width) + " H:" + str(listelem.height) + "]" +
                  " [Pop: " + str(listelem.population_block) + "]")
            print("    " + str(listelem.axis_x - 1) + "," +
                  str(listelem.axis_y - 1) + " : " +
                  str(listelem.axis_x + listelem.width - 1) +
                  "," + str(listelem.axis_y + listelem.height - 1) +
                  " -> " + str(listelem.blocktileset))
