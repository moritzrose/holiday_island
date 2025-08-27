import random
from src.utils import calculate_tile_id, grid_to_projection
from collections import Counter

MORE_SAND_SUFFIX = "S"

# probabilites for tile variation; sum = 1
PROB_BASIC = 0.4
PROB_A = PROB_BASIC + 0.3
PROB_B = PROB_A + 0.2
PROB_C = PROB_B + 0.1

def apply_variation(tile_id):
    # random number, 0-1
    random_number = random.random()

    # more variations for 0000
    if tile_id == "0000":
        if random_number < PROB_BASIC:
            return tile_id
        elif random_number < PROB_A:
            return tile_id + "a"
        elif random_number < PROB_B:
            return tile_id + "b"
        else:
            return tile_id + "c"
    else:
        if random_number < 1 - PROB_A:
            return tile_id + "a"
        return tile_id

class Landscaper:
    def __init__(self, height_map, asset_manager):
        self.height_map = height_map
        self.asset_manager = asset_manager

    def determine_sprite(self,x,y):

        z = self.height_map[y][x]

        tl = self.height_map[y + 1][x]
        tr = self.height_map[y][x]
        br = self.height_map[y][x + 1]
        bl = self.height_map[y + 1][x + 1]
        height_values = [tl, tr, br, bl]
        tile_id = calculate_tile_id(height_values)

        # calculate min and max height value
        min_height: int = min(height_values)
        max_height: int = max(height_values)

        # if the tile has any height values = 0, return water tile
        if min_height == 0:
            return self.asset_manager.water_tiles.get(tile_id)

        # if the tile has only height values <= 2, return sand tile
        elif max_height <= 2:
            tile_id = apply_variation(tile_id)
            return self.asset_manager.sand_tiles.get(tile_id)

        # if the tile has height values 1-3, return sand grass tile
        elif min_height <= 2 < max_height:
            # if it is a diagonal tile, determine variation
            if abs(max_height - min_height) > 1:
                dominant_height = Counter(height_values).most_common(1)[0][0]
                # if there is more sand than grass, append "more sand" suffix
                if dominant_height < 3:
                    tile_id = tile_id + MORE_SAND_SUFFIX

            return self.asset_manager.sand_grass_tiles.get(tile_id)

        # if the tile only has height values >= 3, return grass tile
        else:
            tile_id = apply_variation(tile_id)
            return self.asset_manager.grass_tiles.get(tile_id)

    def determine_location(self,x,y):
        z = self.height_map[y][x]
        return grid_to_projection(x,y,z)