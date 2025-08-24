
OFFSET_X = 5
OFFSET_Y = 1

OFFSET_X_NEW = 5 * REFERENCE_TILE_WIDTH
OFFSET_Y_NEW = 3 * REFERENCE_TILE_HEIGHT

from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT

def tile_to_world(tile_x, tile_y):
    # calculate screen coordinates
    world_x = (tile_x - tile_y) * REFERENCE_TILE_WIDTH / 2
    world_y = (tile_x + tile_y) * REFERENCE_TILE_HEIGHT / 2

    world_x += OFFSET_X * REFERENCE_TILE_WIDTH
    world_y += OFFSET_Y * REFERENCE_TILE_HEIGHT

    return world_x, world_y

def world_to_tile(world_x, world_y, terrain_level):
    tile_x = (world_y // REFERENCE_TILE_HEIGHT - OFFSET_Y) + ((world_x // REFERENCE_TILE_WIDTH) - OFFSET_X)
    tile_y = (world_y // REFERENCE_TILE_HEIGHT - OFFSET_Y) - ((world_x // REFERENCE_TILE_WIDTH) - OFFSET_X)

    return tile_x, tile_y

def projection_to_grid(projection_x, projection_y):
    x_no_offset = projection_x - OFFSET_X_NEW
    y_no_offset = projection_y - OFFSET_Y_NEW

    normed_x = x_no_offset * 2 / REFERENCE_TILE_WIDTH  # u
    normed_y = y_no_offset * 2 / REFERENCE_TILE_HEIGHT  # v

    grid_x = math.floor((normed_x + normed_y) / 2)
    grid_y = math.floor((normed_y - normed_x) / 2)

    grid_x = min(MAP_WIDTH, grid_x)
    grid_y = min(MAP_WIDTH, grid_y)

    grid_x = max(0, grid_x)
    grid_y = max(0, grid_y)

    return grid_x, grid_y

def grid_to_projection(x, y, z):
    projection_x = (x - y) * REFERENCE_TILE_WIDTH * 0.5 + OFFSET_X_NEW
    projection_y = (x + y) * REFERENCE_TILE_HEIGHT * 0.5 - z * 9 + OFFSET_Y_NEW
    return projection_x, projection_y

def calculate_tile_id(height_values):
    tile_id = (
            str(height_values[1] - height_values[0]) +  # tr - tl
            str(height_values[2] - height_values[1]) +  # br - tr
            str(height_values[3] - height_values[2]) +  # bl - br
            str(height_values[0] - height_values[3])  # tl - bl
    )
    return tile_id