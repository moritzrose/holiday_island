
OFFSET_X = 5
OFFSET_Y = 1

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


def calculate_tile_id(height_values):
    tile_id = (
            str(height_values[1] - height_values[0]) +  # tr - tl
            str(height_values[2] - height_values[1]) +  # br - tr
            str(height_values[3] - height_values[2]) +  # bl - br
            str(height_values[0] - height_values[3])  # tl - bl
    )
    return tile_id