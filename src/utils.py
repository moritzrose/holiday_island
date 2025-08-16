# transformation matrix
import math

from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT

# watch this if you want to understand https://www.youtube.com/watch?v=04oQ2jOUjkU

i_x = 0.5
i_y = - 0.5
j_x = 0.5
j_y = 0.5


def tile_to_world(tile_x, tile_y):
    # calculate screen coordinates
    world_x = tile_x * i_x * REFERENCE_TILE_WIDTH + tile_y * j_x * REFERENCE_TILE_WIDTH  # (A * tile_x + B * tile_y)
    world_y = tile_x * i_y * REFERENCE_TILE_HEIGHT + tile_y * j_y * REFERENCE_TILE_HEIGHT  # (C * tile_x + D * tile_y)

    # x: tile.x * i_x * 0.5 * w + tile.y * j_x * 0.5 * w,
    # y: tile.x * i_y * 0.5 * h + tile.y * j_y * 0.5 * h,

    return world_x, world_y


def invert_matrix(a, b, c, d):
    # determinant
    det = 1 / (a * d - b * c)
    return det * d, det * -b, det * -c, det * a


def world_to_tile(world_x, world_y, terrain_level):

    a = i_x * REFERENCE_TILE_WIDTH
    b = j_x * REFERENCE_TILE_WIDTH
    c = i_y * REFERENCE_TILE_HEIGHT
    d = j_y * REFERENCE_TILE_HEIGHT

    a,b,c,d = invert_matrix(a,b,c,d)

    tile_x = world_x * a + world_y * b
    tile_y = world_x * c + world_y * d

    # determinant
    #determinant = 1 / (A * D - B * C)

    #tile_x = determinant * (D * world_x - B * world_y)
    #tile_y = determinant * (-C * world_x + A * world_y)

    # need to round down cause tile_x = 0.9 is still tile_x = 0
    tile_x_rounded = math.floor(tile_x)
    tile_y_rounded = math.floor(tile_y)

    return tile_x_rounded, tile_y_rounded
