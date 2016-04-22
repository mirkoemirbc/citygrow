import random


# Define an array for data saving
map_data = []

# Define static list sequence for elements choises.
list_map_tiles = ('301', '302')


def initializeMap(x, y):
    global map_data

    if x > 0 and y > 0:
        for AxisX in (x):
            for AxisY in (y):
                map_data[AxisX, AxisY] = random.choice(list_map_tiles)
    else:
        return None



