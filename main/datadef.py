# This module is exclusive for Constants and data definition

# Define Dictionaries
error_population = {
    'ERROR_POPULATION': -1,
    'OUT_OF_LIMITS': -2,
    'OUT_OF_CENTER': -3,
    'NO_LIMITS': -4,
}

# Define static dictionary of tuples with kind of tiles.
range_tiles_type = {'NOT_AVAILABLE': (0, 9),
                    # Terrain / Ground tiles
                    'GROUND': (10, 39),
                    'GRASS': (10, 19),
                    'STONE': (20, 29),
                    'BARREN': (30, 39),
                    'ROAD': (40, 49),
                    # Important Building / Facilities
                    'CENTER': (90, 90),
                    'LABORATORY': (91, 93),
                    'MILITARY': (94, 96),
                    'SOCIAL_CENTER': (97, 99),
                    # Houses
                    'HOUSE': (100, 179),
                    'COMMON_HOUSE': (100, 109),
                    'DOUBLE_HOUSE': (110, 119),
                    'MUTANT_HOUSE': (120, 129),
                    'PSIONIC_HOUSE': (130, 139),
                    'MILITARY_HOUSE': (140, 149),
                    'SPECIAL_HOUSE': (150, 159),
                    'RUINED_HOUSE': (160, 169),
                    'SLUM_HOUSE': (170, 179),
                    }

# Define static dictionary of tuple with tiles code and influence.
map_tiles_ground_value = {0: ('00000', 0.0),  # Tile None: Not available
                          # Tile Unusable: Water, rocks, lava, etc.
                          1: ('00001', 0.0), 2: ('00002', 0.0),
                          3: ('00003', 0.0), 4: ('00004', 0.0),
                          5: ('00005', 0.0), 6: ('00006', 0.0),
                          7: ('00007', 0.0), 8: ('00008', 0.0),
                          9: ('00009', 0.0),
                          # Tile Grass: grass with some of dirt, stones, water.
                          10: ('00010', 0.1), 11: ('00011', 0.1),
                          12: ('00012', 0.1), 13: ('00013', 0.1),
                          14: ('00014', 0.1), 15: ('00015', 0.1),
                          16: ('00016', 0.1), 17: ('00017', 0.1),
                          18: ('00018', 0.1), 19: ('00019', 0.1),
                          # Tile Stone: stone ground with sand, dirt and grass.
                          20: ('00020', 0.1), 21: ('00021', 0.1),
                          22: ('00022', 0.1), 23: ('00023', 0.1),
                          24: ('00024', 0.1), 25: ('00025', 0.1),
                          26: ('00026', 0.1), 27: ('00027', 0.1),
                          28: ('00028', 0.1), 29: ('00029', 0.1),
                          # Tile Barren: Dirt with very few brown grass.
                          30: ('00030', 0.1), 31: ('00031', 0.1),
                          32: ('00032', 0.1), 33: ('00033', 0.1),
                          34: ('00034', 0.1), 35: ('00035', 0.1),
                          36: ('00036', 0.1), 37: ('00037', 0.1),
                          38: ('00038', 0.1), 39: ('00039', 0.1),
                          # Tile Roads: Pavement or dirt, with grass or mud.
                          40: ('00040', 0.1), 41: ('00041', 0.1),
                          42: ('00042', 0.1), 43: ('00043', 0.1),
                          44: ('00044', 0.1), 45: ('00045', 0.1),
                          46: ('00046', 0.1), 47: ('00047', 0.1),
                          48: ('00048', 0.1), 49: ('00049', 0.1),
                          }

map_tiles_build_value = {90: ('00090', 10.0), 'CENTER': ('00090', 10.0),
                         # Facilities Buildings. Laboratory
                         91: ('00091', 10.0), 'LAB-LVL-1': ('00091', 10.0),
                         92: ('00092', 10.0), 'LAB-LVL-2': ('00092', 10.0),
                         93: ('00093', 10.0), 'LAB-LVL-3': ('00093', 10.0),
                         # Facilities Buildings. Military
                         94: ('00094', 10.0), 'MIL-LVL-1': ('00094', 10.0),
                         95: ('00095', 10.0), 'MIL-LVL-2': ('00095', 10.0),
                         96: ('00096', 10.0), 'MIL-LVL--3': ('00096', 10.0),
                         # Facilities Buildings. Social Center
                         97: ('00097', 10.0), 'SOC-LVL-1': ('00097', 10.0),
                         98: ('00098', 10.0), 'SOC-LVL-2': ('00098', 10.0),
                         99: ('00099', 10.0), 'SOC-LVL-3': ('00099', 10.0),
                         # Common Houses.
                         100: ('00100', 0.5), 101: ('00101', 0.5),
                         102: ('00102', 0.5), 103: ('00103', 0.5),
                         104: ('00104', 0.5), 105: ('00105', 0.5),
                         106: ('00106', 0.5), 107: ('00107', 0.5),
                         # Double Houses.
                         110: ('00110', 0.8), 111: ('00111', 0.8),
                         112: ('00112', 0.8), 113: ('00113', 0.8),
                         114: ('00114', 0.8), 115: ('00115', 0.8),
                         116: ('00116', 0.8), 117: ('00117', 0.8),
                         # Mutant Houses.
                         120: ('00120', 0.8), 121: ('00121', 0.8),
                         122: ('00122', 0.8), 123: ('00123', 0.8),
                         124: ('00124', 0.8), 125: ('00125', 0.8),
                         126: ('00126', 0.8), 127: ('00127', 0.8),
                         # Psionic Houses.
                         130: ('00130', 0.8), 131: ('00131', 0.8),
                         132: ('00132', 0.8), 133: ('00133', 0.8),
                         134: ('00134', 0.8), 135: ('00135', 0.8),
                         136: ('00136', 0.8), 137: ('00137', 0.8),
                         # Military Houses.
                         140: ('00140', 0.8), 141: ('00141', 0.8),
                         142: ('00142', 0.8), 143: ('00143', 0.8),
                         144: ('00144', 0.8), 145: ('00145', 0.8),
                         146: ('00146', 0.8), 147: ('00147', 0.8),
                         # Special Houses.
                         150: ('00150', 0.8), 151: ('00151', 0.8),
                         152: ('00152', 0.8), 153: ('00153', 0.8),
                         154: ('00154', 0.8), 155: ('00155', 0.8),
                         156: ('00156', 0.8), 157: ('00157', 0.8),
                         # Ruined Houses.
                         160: ('00160', 0.5), 161: ('00161', 0.5),
                         162: ('00162', 0.5), 163: ('00163', 0.5),
                         164: ('00164', 0.5), 165: ('00165', 0.5),
                         166: ('00166', 0.5), 167: ('00167', 0.5),
                         # Slum Houses.
                         170: ('00170', 0.5), 171: ('00171', 0.5),
                         172: ('00172', 0.5), 173: ('00173', 0.5),
                         174: ('00174', 0.5), 175: ('00175', 0.5),
                         176: ('00176', 0.5), 177: ('00177', 0.5),
                         }

map_tiles_center = ('00090', 10.0)

range_block_type = {'NOT_AVAILABLE': (10000, 10009),
                    # Important Building / Facilities
                    'CENTER': (90, 90),
                    'LABORATORY': (91, 93),
                    'MILITARY': (94, 96),
                    'SOCIAL_CENTER': (97, 99),
                    # Houses
                    'HOUSE': (10010, 10030, 10050, 10070, 10090,
                              10110, 10130, 10150, 10170, 10190,
                              10210, 10230, 10250, 10270, 10290,
                              10310, 10330, 10350, 10370, 10390,
                              10410, 10430, 10450, 10470, 10490,
                              10510, 10530, 10550, 10570, 10590,
                              10610, 10630, 10650, 10670, 10690,
                              10710, 10730, 10750, 10770, 10790,),
                    'COMMON_HOUSE': (10010, 10030, 10050, 10070, 10090),
                    'DOUBLE_HOUSE': (10110, 10130, 10150, 10170, 10190),
                    'MUTANT_HOUSE': (10210, 10230, 10250, 10270, 10290),
                    'PSIONIC_HOUSE': (10310, 10330, 10350, 10370, 10390),
                    'MILITARY_HOUSE': (10410, 10430, 10450, 10470, 10490),
                    'SPECIAL_HOUSE': (10510, 10530, 10550, 10570, 10590),
                    'RUINED_HOUSE': (10610, 10630, 10650, 10670, 10690),
                    'SLUM_HOUSE': (10710, 10730, 10750, 10770, 10790),
                    }

map_block_code = {10000: ('10000', 0.0),  # Deserted Block
                  # City Center
                  90: ('00090', 10.0),
                  # Common Houses.
                  10010: ('10010', 0.5), 10030: ('10030', 0.5),
                  10050: ('10050', 0.5), 10070: ('10070', 0.5),
                  10090: ('10090', 0.5),
                  # Double Houses.
                  10110: ('10110', 0.8), 10130: ('10130', 0.8),
                  10150: ('10150', 0.8), 10170: ('10170', 0.8),
                  10190: ('10190', 0.8),
                  # Mutant Houses.
                  10210: ('10210', 0.8), 10230: ('10230', 0.8),
                  10250: ('10250', 0.8), 10270: ('10270', 0.8),
                  10290: ('10290', 0.8),
                  # Psionic Houses.
                  10310: ('10310', 0.8), 10330: ('10330', 0.8),
                  10350: ('10350', 0.8), 10370: ('10370', 0.8),
                  10390: ('10390', 0.8),
                  # Military Houses.
                  10410: ('10410', 0.8), 10430: ('10430', 0.8),
                  10450: ('10450', 0.8), 10470: ('10470', 0.8),
                  10490: ('10490', 0.8),
                  # Special Houses.
                  10510: ('10510', 0.8), 10530: ('10530', 0.8),
                  10550: ('10550', 0.8), 10570: ('10570', 0.8),
                  10590: ('10590', 0.8),
                  # Ruined Houses.
                  10610: ('10610', 0.5), 10630: ('10630', 0.5),
                  10650: ('10650', 0.5), 10670: ('10670', 0.5),
                  10690: ('10690', 0.5),
                  # Slum Houses.
                  10710: ('10710', 0.5), 10730: ('10730', 0.5),
                  10750: ('10750', 0.5), 10770: ('10770', 0.5),
                  10790: ('10790', 0.5),
                  }
