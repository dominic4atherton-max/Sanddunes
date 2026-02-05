import numpy as np  
import matplotlib.pyplot as plt 

def sand_pile_collapse_modular(dune_map, x_loc, y_loc):
    dune_width, dune_length = dune_map.shape
    dune_map[x_loc, y_loc] -= 4
    dune_map[(x_loc - 1)%dune_length, y_loc] += 1
    dune_map[(x_loc + 1)%dune_length, y_loc] += 1
    dune_map[x_loc, (y_loc - 1)%dune_width] += 1
    dune_map[x_loc, (y_loc + 1)%dune_width] += 1
    return dune_map

def central_sand_drop(dune_map, total_sand):
    dune_width, dune_length = dune_map.shape
    center_x = dune_length // 2
    center_y = dune_width // 2
    for i in range(total_sand):
        dune_map[center_x, center_y] += 1
        sand_propagator(dune_map, center_x, center_y)
    return dune_map

def sand_propagator(dune_map, x_loc, y_loc):
    dune_width, dune_length = dune_map.shape
    search_coords = np.array([[x_loc, y_loc, 0]])
    while len(search_coords) > 0:
        current_coord = search_coords[0]
        search_coords = np.delete(search_coords, 0, axis=0)
        i, j, tag = current_coord
        if dune_map[i, j] >= 4:
            sand_pile_collapse_modular(dune_map, i, j)
            # Now add adjacent squares to search coords
            adjacent_coords = np.array([
                [(i - 1)%dune_length, j, tag + 1],
                [(i + 1)%dune_length, j, tag + 1],
                [i, (j - 1)%dune_width, tag +1],
                [i, (j + 1)%dune_width, tag+1]
            ])
            search_coords = np.vstack((search_coords, adjacent_coords))
    return dune_map
