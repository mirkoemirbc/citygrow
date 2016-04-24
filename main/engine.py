import random


# Define an array for data saving
map_data = []

# Define static list sequence for elements choises.
list_map_tiles = ('00000', '00003', '00011', '00012', '00012', '00013', '00022', '00041', 
                  '00061', '00073', '00083', '00302', '00402', '00501')


def initializeMap(x, y):
    global map_data

    # We'll fillout all array with valid and random information
    if x > 0 and y > 0:
        for AxisX in (x):
            for AxisY in (y):
                map_data[AxisX, AxisY] = random.choice(list_map_tiles)
    else:
        return false

    # We'll determinate the center of the City
    map_data [(x/2)+random.randint(-2,2), (y/2)+random.randint(-2,2)] = '00091'

    return true


def showMap(x, y):
    # Print the Map structure

    if x > 0 and y > 0:
        for AxisX in (x):
            for AxisY in (y):
                print "[" + AxisX + "]" + "[" + AxisY + "]:" + map_data[AxisX, AxisY]

    return None


