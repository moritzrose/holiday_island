# transformation matrix
from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT

# watch this if you want to understand https://www.youtube.com/watch?v=04oQ2jOUjkU
A = 0.5
B = -0.5
C = 0.5
D = 0.5


# I used this less optimized representation, to show A B C and D and understand the inverse calculation
def grid_to_world(grid_x, grid_y):

    # calculate screen coordinates
    world_x = (A * grid_x + B * grid_y) * REFERENCE_TILE_WIDTH
    world_y = (C * grid_x + D * grid_y) * REFERENCE_TILE_HEIGHT

    return world_x, world_y


def world_to_grid(world_x, world_y):

    # determinant
    determinant = 1 / (A * D - B * C)


    # calculate grid coordinates
    grid_x = determinant * (D * world_x - B * world_y) * REFERENCE_TILE_WIDTH
    grid_y = determinant * (-C * grid_x + A * world_y) * REFERENCE_TILE_HEIGHT

    return grid_x, grid_y
