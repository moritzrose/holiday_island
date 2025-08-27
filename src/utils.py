from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT, ELEVATION_OFFSET
from src.game_configuration import MAP_WIDTH, MAP_HEIGHT

X_0 = (MAP_WIDTH * REFERENCE_TILE_WIDTH - REFERENCE_TILE_WIDTH) / 2
Y_0 = 0

def projection_to_grid(projection_x, projection_y):
    x_no_offset = projection_x - SURFACE_OFFSET_X
    y_no_offset = projection_y - SURFACE_OFFSET_Y

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
    projection_x = X_0 + (x - y) * REFERENCE_TILE_WIDTH * 0.5
    projection_y = Y_0 + (x + y) * REFERENCE_TILE_HEIGHT * 0.5 - z * ELEVATION_OFFSET
    return projection_x, projection_y

def calculate_tile_id(height_values):
    tile_id = (
            str(height_values[1] - height_values[0]) +  # tr - tl
            str(height_values[2] - height_values[1]) +  # br - tr
            str(height_values[3] - height_values[2]) +  # bl - br
            str(height_values[0] - height_values[3])  # tl - bl
    )
    return tile_id