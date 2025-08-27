from noise import pnoise2
import matplotlib.pyplot as plt

from src.game_configuration import SHOW_HEIGHT_DISTRIBUTION
from src.game_constants import MAX_TERRAIN_LEVEL


def transform_noise_to_height(normalized_noise_value: float):
    if normalized_noise_value <= 0.51:
        return 0
    elif normalized_noise_value <= 0.53:
        return 1
    elif normalized_noise_value <= 0.55:
        return 2
    elif normalized_noise_value <= 0.6:
        return 3
    elif normalized_noise_value <= 0.63:
        return 4
    elif normalized_noise_value <= 0.75:
        return 5
    else:
        return MAX_TERRAIN_LEVEL


def clamp(value, min_value, max_value):
    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value

def generate_heightmap(seed, map_width, map_height):

    # corner-grid-dimensions - 200 tiles = 201 corners:
    h_corners = map_width + 1
    v_corners = map_height + 1

    # init 2d array with -1 for debug purposes
    height_map = [[-1 for x in range(h_corners)] for y in range(v_corners)]

    for v in range(v_corners):
        for h in range(h_corners):

            # calculate noise value
            noise_val = pnoise2(h * 0.03, v * 0.03, octaves=15, persistence=0.4, base=seed)

            # normalize noise value to interval 0 - 1
            normalized_noise_val = (noise_val + 1) * 0.5

            # transform noise value to height value
            height_value = transform_noise_to_height(normalized_noise_val)

            # add height value to height map
            height_map[v][h] = height_value

    # flatten any height jumps > 1 between adjacent corners
    height_map_flattened = flatten_jumps(h_corners, v_corners, height_map)

    if SHOW_HEIGHT_DISTRIBUTION:
        show_height_distribution()

    return height_map_flattened

# flattens height jumps > 1
def flatten_jumps(h_corners, v_corners, height_map):

    for v in range(v_corners):
        for h in range(h_corners):

            height = height_map[v][h]
            min_height = max(height - 1, 0)
            max_height = min(height + 1, MAX_TERRAIN_LEVEL)

            if v < v_corners - 1:
                v_neighbour = height_map[v + 1][h]
                if v_neighbour > max_height or v_neighbour < min_height:
                    v_neighbour = clamp(v_neighbour, min_height, max_height)
                    height_map[v + 1][h] = v_neighbour
            if h < v_corners - 1:
                h_neighbour = height_map[v][h + 1]
                if h_neighbour > max_height or h_neighbour < min_height:
                    h_neighbour = clamp(h_neighbour, min_height, max_height)
                    height_map[v][h + 1] = h_neighbour

    return height_map

    # helper method to show height distribution statistic
def show_height_distribution(height_map):
    werte = [val for row in height_map for val in row]
    plt.hist(werte, bins=30)  # 30 Balken im Histogramm
    plt.title('Verteilung der Heightmap-Werte')
    plt.xlabel('Wert')
    plt.ylabel('Häufigkeit')
    plt.show()
