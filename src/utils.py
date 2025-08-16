# transformation matrix
import math

from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT

# watch this if you want to understand https://www.youtube.com/watch?v=04oQ2jOUjkU
A = 0.5 * REFERENCE_TILE_WIDTH
B = -0.5 * REFERENCE_TILE_WIDTH
C = 0.5 * REFERENCE_TILE_HEIGHT
D = 0.5 * REFERENCE_TILE_HEIGHT


def tile_to_world(tile_x, tile_y):

    # calculate screen coordinates
    world_x = (A * tile_x + B * tile_y)
    world_y = (C * tile_x + D * tile_y)

    return world_x, world_y


def world_to_tile(world_x, world_y, terrain_level):

    # determinant
    determinant = 1 / (A * D - B * C)

    tile_x = determinant * (D * world_x - B * world_y)
    tile_y = determinant * (-C * world_x + A * world_y)

    # need to round down cause tile_x = 0.9 is still tile_x = 0
    tile_x_rounded = math.floor(tile_x)
    tile_y_rounded = math.floor(tile_y)

    return tile_x_rounded, tile_y_rounded
