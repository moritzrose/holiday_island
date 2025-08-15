# transformation matrix
import math

from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT
from src.game_constants import ELEVATION_OFFSET

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

    # account for terrain level, which offsets the tiles' screen coordinates
    terrain_offset = ELEVATION_OFFSET * terrain_level

    # need to round down cause tile_x = 0.9 is still tile_x = 0
    tile_x = math.floor(determinant * (D * world_x - B * (world_y - terrain_offset)) - 100)
    tile_y = math.floor(determinant * (-C * world_x + A * (world_y - terrain_offset)) + 100)
    # I do not know why I need the 100/-100 ... it works ... my head hurts ... it happens to be 200 / 2 with 200 being the number of tiles I have in x and y direction ... coincident?

    return tile_x, tile_y
