import random

# My Imports
from main.datadef import range_tiles_type, range_block_type
from main.datadef import map_block_code, map_tiles_ground_value
from main.generic import *

# Local Constants


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
    must_change = True
    influence = 0.0

    def __init__(self, x, y, building, scratch=True, height=5, width=5):
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

        xsup_neighbour = xinf_neighbour + neighbour.width - 1
        ysup_neighbour = yinf_neighbour + neighbour.height - 1

        # Return True if the neighbour block is within this block borders.
        # Check out every BORDER.
        # import ipdb; ipdb.set_trace()
        if (xsup_neighbour >= xinf >= xinf_neighbour) and \
           (ysup_neighbour >= yinf >= yinf_neighbour):
            return True
        elif (xsup_neighbour >= xsup >= xinf_neighbour) and \
             (ysup_neighbour >= yinf >= yinf_neighbour):
            return True
        elif (xsup_neighbour >= xinf >= xinf_neighbour) and \
             (ysup_neighbour >= ysup >= yinf_neighbour):
            return True
        elif (xsup_neighbour >= xsup >= xinf_neighbour) and \
             (ysup_neighbour >= ysup >= yinf_neighbour):
            return True
        else:
            return False

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

    def cityexpandinhabitant(self, blockref):
        """
        Compare influence between two blocks and raise residents number by 1 or 2
        if the influence is at 75% or greater.
        """
        if percent(self.influence, blockref.influence) > 75 and \
           percent(self.influence, blockref.influence) < 100:
            if self.must_change:
                self.population_block += random.randint(1, 2)
                self.must_change = False
            else:
                self.must_change = True

    def cityexpandinfluence(self):
        """
        Depends on the blocktype influence, the influence of self block will raise.
        The raise is multiplied by a random number between 1 and 3.
        """
        influenceplus = map_block_code[self.blocktileset][1] * random.randint(1, 3)
        self.influence += influenceplus


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
            citycenterblock = CityMapBlock(self.xcenter, self.ycenter, 'CENTER')
            citycenterblock.influence = map_block_code[90][1]
            self.citymap.append(citycenterblock)

            # Fill up with random number of pre-done blocks
            # of Slum / Ruined Houses.
            for housescount in range(random.randint(3, 8)):
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
                citybuild.influence = 0.15

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

    def citymapinfluencegreaterthan(self, limit):
        """ Return a list of blocks with high influence """
        listreturn = []
        for blocks in self.citymap:
            if blocks.influence >= limit:
                listreturn.append(blocks)
        return listreturn

    def findnearestblock(self, blockref, direction='ALL'):
        """ This search for another object in relative direction from a reference object """
        return_id = -1
        return_x = -1
        return_y = -1

        refx_origin = blockref.x_origin - 1
        refy_origin = blockref.y_origin - 1
        refx_width = blockref.x_origin + blockref.width - 2
        refy_height = blockref.y_origin + blockref.height - 2

        for i, listelem in enumerate(self.citymap):
            if (blockref.x_origin == listelem.x_origin) and \
               (blockref.y_origin == listelem.y_origin):
                continue
            # We'll check for the North (consider if the choice is ALL)
            if direction == 'ALL' or direction == 'NORTH':
                if (refx_origin <= listelem.x_origin <= refx_width) and \
                   (listelem.y_origin >= refy_origin):
                    if (return_y > listelem.y_origin or return_y == -1):
                        return_x = listelem.x_origin
                        return_y = listelem.y_origin
                        return_id = i
            # We'll check for East (consider if the choice is ALL)
            if direction == 'ALL' or direction == 'EAST':
                if (listelem.x_origin >= refx_width) and \
                   (refy_origin >= listelem.y_origin >= refy_height):
                    if return_x > listelem.x_origin or return_x == -1:
                        return_x = listelem.x_origin
                        return_y = listelem.y_origin
                        return_id = i
            # We'll check for South (consider if the choice is ALL)
            if direction == 'ALL' or direction == 'SOUTH':
                if (refx_origin <= listelem.x_origin <= refx_origin) and \
                   (listelem.y_origin <= refy_origin):
                    if return_y < listelem.y_origin or return_y == -1:
                        return_x = listelem.x_origin
                        return_y = listelem.y_origin
                        return_id = i
            # We'll check for West (consider if the choice is ALL)
            if direction == 'ALL' or direction == 'WEST':
                if (listelem.x_origin <= refx_origin) and \
                   (refy_origin >= listelem.y_origin >= refy_height):
                    if return_x < listelem.x_origin:
                        return_x = listelem.x_origin
                        return_y = listelem.y_origin
                        return_id = i
            # We'll check for North East (consider if the choice is ALL)
            if direction == 'ALL' or direction == 'NE':
                if (listelem.x_origin >= refx_width) and (listelem.y_origin >= refy_height):
                    if (return_x > listelem.x_origin or return_x == -1) and \
                       (return_y > listelem.y_origin or return_y == -1):
                        return_x = listelem.x_origin
                        return_y = listelem.y_origin
                        return_id = i
            # We'll check for South East (consider if the choice is ALL)
            if direction == 'ALL' or direction == 'SE':
                if (listelem.x_origin >= refx_width) and (listelem.y_origin <= refy_origin):
                    if (return_x > listelem.x_origin or return_x == -1) and \
                       (return_y > listelem.y_origin or return_y == -1):
                        return_x = listelem.x_origin
                        return_y = listelem.y_origin
                        return_id = i
            # We'll check for South West (consider if the choice is ALL)
            if direction == 'ALL' or direction == 'SW':
                if (listelem.x_origin <= refx_origin) and (listelem.y_origin <= refy_origin):
                    if (return_x > listelem.x_origin or return_x == -1) and \
                       (return_y > listelem.y_origin or return_y == -1):
                        return_x = listelem.x_origin
                        return_y = listelem.y_origin
                        return_id = i
            # We'll check for North West (consider if the choice is ALL)
            if direction == 'ALL' or direction == 'NW':
                if (listelem.x_origin <= refx_origin) and (listelem.y_origin >= refy_height):
                    if return_x < listelem.x_origin and return_y < listelem.y_origin:
                        return_x = listelem.x_origin
                        return_y = listelem.y_origin
                        return_id = i

        return (return_id, return_x, return_y)

    def cityexpand(self):
        """
        Evaluate a point in the map and grow the zone sorrounding.
        The function will evaluate each cardinal point and raise the influence of random number
        of blocks.
        """
        influencegt = 5
        cardinaldirection = ['NORTH', 'NE', 'EAST', 'SE', 'SOUTH', 'SW', 'WEST', 'NW']

        # First, collect all block id with influence greater than influencegt [default = 5]
        blocklist = self.citymapinfluencegreaterthan(influencegt)
        for importantblocks in blocklist:
            # Take four random cardinal directions to verify
            randomcardinal = containedin(cardinaldirection, 4)

            # Verify all blocks in the influence zone. Saving the nearest in every direction.
            for eachcardinal in randomcardinal:
                nearestblockid = self.findnearestblock(importantblocks, eachcardinal)[0]
                if nearestblockid >= 0:
                    self.citymap[nearestblockid].cityexpandinfluence()
                    self.citymap[nearestblockid].cityexpandinhabitant(importantblocks)
                else:
                    # If there is not any block in this direction, then try to create a new block
                    # with new SLUM_HOUSE. Maybe this is not possible.
                    if eachcardinal == 'NORTH':
                        if importantblocks.y_origin + 6 <= self.ymax:
                            new_x = importantblocks.x_origin
                            new_y = importantblocks.y_origin + 4
                            newblock = CityMapBlock(new_x, new_y, 'SLUM_HOUSE')
                            while newblock.blocktilesetoverlap(self.citymap[nearestblockid]):
                                newblock.y_origin += 1
                                if newblock.y_origin > self.ymax - 3:
                                    break
                            else:
                                newblock.population_block = random.randint(1, 3)
                                newblock.cityexpandinfluence()
                                self.citymap.append(newblock)

                    elif eachcardinal == 'EAST':
                        if importantblocks.x_origin + 6 <= self.xmax:
                            new_x = importantblocks.x_origin + 4
                            new_y = importantblocks.y_origin
                            newblock = CityMapBlock(new_x, new_y, 'SLUM_HOUSE')
                            while newblock.blocktilesetoverlap(self.citymap[nearestblockid]):
                                newblock.x_origin += 1
                                if newblock.x_origin > self.xmax - 3:
                                    break
                            else:
                                newblock.population_block = random.randint(1, 3)
                                newblock.cityexpandinfluence()
                                self.citymap.append(newblock)

                    elif eachcardinal == 'SOUTH':
                        if importantblocks.y_origin - 4 >= 0:
                            new_x = importantblocks.x_origin
                            new_y = importantblocks.y_origin - 4
                            newblock = CityMapBlock(new_x, new_y, 'SLUM_HOUSE')
                            while newblock.blocktilesetoverlap(self.citymap[nearestblockid]):
                                newblock.x_origin -= 1
                                if newblock.x_origin < 0:
                                    break
                            else:
                                newblock.population_block = random.randint(1, 3)
                                newblock.cityexpandinfluence()
                                self.citymap.append(newblock)

                    elif eachcardinal == 'WEST':
                        if importantblocks.x_origin - 4 >= 0:
                            new_x = importantblocks.x_origin - 4
                            new_y = importantblocks.y_origin
                            newblock = CityMapBlock(new_x, new_y, 'SLUM_HOUSE')
                            while newblock.blocktilesetoverlap(self.citymap[nearestblockid]):
                                newblock.x_origin -= 1
                                if newblock.x_origin < 0:
                                    break
                            else:
                                newblock.population_block = random.randint(1, 3)
                                newblock.cityexpandinfluence()
                                self.citymap.append(newblock)

                    elif eachcardinal == 'NE':
                        if importantblocks.x_origin + 6 <= self.xmax and \
                           importantblocks.y_origin + 6 <= self.ymax:
                            new_x = importantblocks.x_origin + 4
                            new_y = importantblocks.y_origin + 4
                            newblock = CityMapBlock(new_x, new_y, 'SLUM_HOUSE')
                            while newblock.blocktilesetoverlap(self.citymap[nearestblockid]):
                                newblock.x_origin += 1
                                newblock.y_origin += 1
                                if newblock.x_origin > self.xmax - 3 or \
                                   newblock.y_origin > self.ymax - 3:
                                    break
                            else:
                                newblock.population_block = random.randint(1, 3)
                                newblock.cityexpandinfluence()
                                self.citymap.append(newblock)

                    elif eachcardinal == 'SE':
                        if importantblocks.x_origin + 6 <= self.xmax and \
                           importantblocks.y_origin - 4 >= 0:
                            new_x = importantblocks.x_origin + 4
                            new_y = importantblocks.y_origin - 4
                            newblock = CityMapBlock(new_x, new_y, 'SLUM_HOUSE')
                            while newblock.blocktilesetoverlap(self.citymap[nearestblockid]):
                                newblock.x_origin -= 1
                                newblock.y_origin += 1
                                if newblock.x_origin < 0 or \
                                   newblock.y_origin > self.ymax - 3:
                                    break
                            else:
                                newblock.population_block = random.randint(1, 3)
                                newblock.cityexpandinfluence()
                                self.citymap.append(newblock)

                    elif eachcardinal == 'SW':
                        if importantblocks.x_origin + 6 <= self.xmax and \
                           importantblocks.y_origin - 4 >= 0:
                            new_x = importantblocks.x_origin - 4
                            new_y = importantblocks.y_origin - 4
                            newblock = CityMapBlock(new_x, new_y, 'SLUM_HOUSE')
                            while newblock.blocktilesetoverlap(self.citymap[nearestblockid]):
                                newblock.x_origin -= 1
                                newblock.y_origin -= 1
                                if newblock.x_origin < 0 or newblock.y_origin < 0:
                                    break
                            else:
                                newblock.population_block = random.randint(1, 3)
                                newblock.cityexpandinfluence()
                                self.citymap.append(newblock)

                    elif eachcardinal == 'NW':
                        if importantblocks.x_origin - 4 >= 0 and \
                           importantblocks.y_origin + 6 <= self.ymax:
                            new_x = importantblocks.x_origin - 4
                            new_y = importantblocks.y_origin + 4
                            newblock = CityMapBlock(new_x, new_y, 'SLUM_HOUSE')
                            while newblock.blocktilesetoverlap(self.citymap[nearestblockid]):
                                newblock.x_origin -= 1
                                newblock.y_origin += 1
                                if newblock.x_origin < 0 or \
                                   newblock.y_origin > self.ymax - 3:
                                    break
                            else:
                                newblock.population_block = random.randint(1, 3)
                                newblock.cityexpandinfluence()
                                self.citymap.append(newblock)

    def citymapprintcoord(self):
        """ This function is only for console use """
        for i, listelem in enumerate(self.citymap):
            print("[" + str(i) + "] (" + str(listelem.x_origin) +
                  "," + str(listelem.y_origin) + ") [W:" +
                  str(listelem.width) + " H:" + str(listelem.height) + "]" +
                  " [Pop: " + str(listelem.population_block) + "][Inf: " +
                  str(listelem.influence) + "]")
            print("    " + str(listelem.x_origin - 1) + "," +
                  str(listelem.y_origin - 1) + " : " +
                  str(listelem.x_origin + listelem.width - 2) +
                  "," + str(listelem.y_origin + listelem.height - 2) +
                  " -> " + str(listelem.blocktileset))
