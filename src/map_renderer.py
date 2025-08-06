import pygame
import random

from collections import Counter
from height_map_generator import generate_heightmap

REFERENCE_TILE_DIMENSION = 62, 32
MORE_SAND_SUFFIX = "S"

# probabilites for tile variation - sum = 1
PROB_BASIC = 0.4
PROB_A = PROB_BASIC + 0.3
PROB_B = PROB_A + 0.2
PROB_C = PROB_B + 0.1



def grid_to_screen(grid_x, grid_y, tile_dimensions, terrain_level):
    width, height = tile_dimensions
    screen_x = 0.5 * (grid_x - grid_y) * width
    screen_y = 0.5 * (grid_x + grid_y) * height - terrain_level * 9
    return screen_x, screen_y


def tile_variation(tile_id):

    # random number, 0-1
    random_number = random.random()

    if  random_number < PROB_BASIC:
        return tile_id
    elif random_number < PROB_A:
        return tile_id + "a"
    elif random_number < PROB_B:
        return tile_id + "b"
    else:
        return tile_id + "c"


class MapRenderer:

    def load_tiles(self):
        self.tile_definitions_water = {
            "0000": {"sprite": pygame.image.load("../resources/tiles/water/0000.png").convert_alpha()},
            "1-100": {"sprite": pygame.image.load("../resources/tiles/water/1-100.png").convert_alpha()},
            "01-10": {"sprite": pygame.image.load("../resources/tiles/water/01-10.png").convert_alpha()},
            "001-1": {"sprite": pygame.image.load("../resources/tiles/water/001-1.png").convert_alpha()},
            "-1001": {"sprite": pygame.image.load("../resources/tiles/water/-1001.png").convert_alpha()},
            "10-10": {"sprite": pygame.image.load("../resources/tiles/water/10-10.png").convert_alpha()},
            "-1010": {"sprite": pygame.image.load("../resources/tiles/water/-1010.png").convert_alpha()},
            "010-1": {"sprite": pygame.image.load("../resources/tiles/water/010-1.png").convert_alpha()},
            "0-101": {"sprite": pygame.image.load("../resources/tiles/water/0-101.png").convert_alpha()},
            "100-1": {"sprite": pygame.image.load("../resources/tiles/water/100-1.png").convert_alpha()},
            "-1100": {"sprite": pygame.image.load("../resources/tiles/water/-1100.png").convert_alpha()},
            "0-110": {"sprite": pygame.image.load("../resources/tiles/water/0-110.png").convert_alpha()},
            "00-11": {"sprite": pygame.image.load("../resources/tiles/water/00-11.png").convert_alpha()},
            "1-11-1": {"sprite": pygame.image.load("../resources/tiles/water/1-11-1.png").convert_alpha()},
            "-11-11": {"sprite": pygame.image.load("../resources/tiles/water/-11-11.png").convert_alpha()},
            "11-1-1": {"sprite": pygame.image.load("../resources/tiles/water/11-1-1.png").convert_alpha()},
            "1-1-11": {"sprite": pygame.image.load("../resources/tiles/water/1-1-11.png").convert_alpha()},
            "-1-111": {"sprite": pygame.image.load("../resources/tiles/water/-1-111.png").convert_alpha()},
            "-111-1": {"sprite": pygame.image.load("../resources/tiles/water/-111-1.png").convert_alpha()},
        }

        self.tile_definitions_sand = {

            #basic tiles
            "0000": {"sprite": pygame.image.load("../resources/tiles/sand/basic/0000.png").convert_alpha()},
            "1-100": {"sprite": pygame.image.load("../resources/tiles/sand/basic/1-100.png").convert_alpha()},
            "01-10": {"sprite": pygame.image.load("../resources/tiles/sand/basic/01-10.png").convert_alpha()},
            "001-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/001-1.png").convert_alpha()},
            "-1001": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-1001.png").convert_alpha()},
            "10-10": {"sprite": pygame.image.load("../resources/tiles/sand/basic/10-10.png").convert_alpha()},
            "-1010": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-1010.png").convert_alpha()},
            "010-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/010-1.png").convert_alpha()},
            "0-101": {"sprite": pygame.image.load("../resources/tiles/sand/basic/0-101.png").convert_alpha()},
            "100-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/100-1.png").convert_alpha()},
            "-1100": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-1100.png").convert_alpha()},
            "0-110": {"sprite": pygame.image.load("../resources/tiles/sand/basic/0-110.png").convert_alpha()},
            "00-11": {"sprite": pygame.image.load("../resources/tiles/sand/basic/00-11.png").convert_alpha()},
            "1-11-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/1-11-1.png").convert_alpha()},
            "-11-11": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-11-11.png").convert_alpha()},
            "11-1-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/11-1-1.png").convert_alpha()},
            "1-1-11": {"sprite": pygame.image.load("../resources/tiles/sand/basic/1-1-11.png").convert_alpha()},
            "-1-111": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-1-111.png").convert_alpha()},
            "-111-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-111-1.png").convert_alpha()},

            #variation a
            "0000a": {"sprite": pygame.image.load("../resources/tiles/sand/a/0000.png").convert_alpha()},
            "1-100a": {"sprite": pygame.image.load("../resources/tiles/sand/a/1-100.png").convert_alpha()},
            "01-10a": {"sprite": pygame.image.load("../resources/tiles/sand/a/01-10.png").convert_alpha()},
            "001-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/001-1.png").convert_alpha()},
            "-1001a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-1001.png").convert_alpha()},
            "10-10a": {"sprite": pygame.image.load("../resources/tiles/sand/a/10-10.png").convert_alpha()},
            "-1010a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-1010.png").convert_alpha()},
            "010-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/010-1.png").convert_alpha()},
            "0-101a": {"sprite": pygame.image.load("../resources/tiles/sand/a/0-101.png").convert_alpha()},
            "100-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/100-1.png").convert_alpha()},
            "-1100a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-1100.png").convert_alpha()},
            "0-110a": {"sprite": pygame.image.load("../resources/tiles/sand/a/0-110.png").convert_alpha()},
            "00-11a": {"sprite": pygame.image.load("../resources/tiles/sand/a/00-11.png").convert_alpha()},
            "1-11-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/1-11-1.png").convert_alpha()},
            "-11-11a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-11-11.png").convert_alpha()},
            "11-1-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/11-1-1.png").convert_alpha()},
            "1-1-11a": {"sprite": pygame.image.load("../resources/tiles/sand/a/1-1-11.png").convert_alpha()},
            "-1-111a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-1-111.png").convert_alpha()},
            "-111-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-111-1.png").convert_alpha()},

            #variation b
            "0000b": {"sprite": pygame.image.load("../resources/tiles/sand/b/0000.png").convert_alpha()},

            #variation c
            "0000c": {"sprite": pygame.image.load("../resources/tiles/sand/c/0000.png").convert_alpha()},
        }

        self.tile_definitions_grass = {

            #basic
            "0000": {"sprite": pygame.image.load("../resources/tiles/grass/basic/0000.png").convert_alpha()},
            "1-100": {"sprite": pygame.image.load("../resources/tiles/grass/basic/1-100.png").convert_alpha()},
            "01-10": {"sprite": pygame.image.load("../resources/tiles/grass/basic/01-10.png").convert_alpha()},
            "001-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/001-1.png").convert_alpha()},
            "-1001": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-1001.png").convert_alpha()},
            "10-10": {"sprite": pygame.image.load("../resources/tiles/grass/basic/10-10.png").convert_alpha()},
            "-1010": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-1010.png").convert_alpha()},
            "010-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/010-1.png").convert_alpha()},
            "0-101": {"sprite": pygame.image.load("../resources/tiles/grass/basic/0-101.png").convert_alpha()},
            "100-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/100-1.png").convert_alpha()},
            "-1100": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-1100.png").convert_alpha()},
            "0-110": {"sprite": pygame.image.load("../resources/tiles/grass/basic/0-110.png").convert_alpha()},
            "00-11": {"sprite": pygame.image.load("../resources/tiles/grass/basic/00-11.png").convert_alpha()},
            "1-11-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/1-11-1.png").convert_alpha()},
            "-11-11": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-11-11.png").convert_alpha()},
            "11-1-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/11-1-1.png").convert_alpha()},
            "1-1-11": {"sprite": pygame.image.load("../resources/tiles/grass/basic/1-1-11.png").convert_alpha()},
            "-1-111": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-1-111.png").convert_alpha()},
            "-111-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-111-1.png").convert_alpha()},

            #variation a
            "0000a": {"sprite": pygame.image.load("../resources/tiles/grass/a/0000.png").convert_alpha()},
            "1-100a": {"sprite": pygame.image.load("../resources/tiles/grass/a/1-100.png").convert_alpha()},
            "01-10a": {"sprite": pygame.image.load("../resources/tiles/grass/a/01-10.png").convert_alpha()},
            "001-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/001-1.png").convert_alpha()},
            "-1001a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-1001.png").convert_alpha()},
            "10-10a": {"sprite": pygame.image.load("../resources/tiles/grass/a/10-10.png").convert_alpha()},
            "-1010a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-1010.png").convert_alpha()},
            "010-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/010-1.png").convert_alpha()},
            "0-101a": {"sprite": pygame.image.load("../resources/tiles/grass/a/0-101.png").convert_alpha()},
            "100-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/100-1.png").convert_alpha()},
            "-1100a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-1100.png").convert_alpha()},
            "0-110a": {"sprite": pygame.image.load("../resources/tiles/grass/a/0-110.png").convert_alpha()},
            "00-11a": {"sprite": pygame.image.load("../resources/tiles/grass/a/00-11.png").convert_alpha()},
            "1-11-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/1-11-1.png").convert_alpha()},
            "-11-11a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-11-11.png").convert_alpha()},
            "11-1-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/11-1-1.png").convert_alpha()},
            "1-1-11a": {"sprite": pygame.image.load("../resources/tiles/grass/a/1-1-11.png").convert_alpha()},
            "-1-111a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-1-111.png").convert_alpha()},
            "-111-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-111-1.png").convert_alpha()},

            #variation b
            "0000b": {"sprite": pygame.image.load("../resources/tiles/grass/b/0000.png").convert_alpha()},

            #variation c
            "0000c": {"sprite": pygame.image.load("../resources/tiles/grass/c/0000.png").convert_alpha()},
        }

        self.tile_definitions_sand_grass = {
            "1-100": {"sprite": pygame.image.load("../resources/tiles/sand_grass/1-100.png").convert_alpha()},
            "01-10": {"sprite": pygame.image.load("../resources/tiles/sand_grass/01-10.png").convert_alpha()},
            "001-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/001-1.png").convert_alpha()},
            "-1001": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-1001.png").convert_alpha()},
            "10-10": {"sprite": pygame.image.load("../resources/tiles/sand_grass/10-10.png").convert_alpha()},
            "-1010": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-1010.png").convert_alpha()},
            "010-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/010-1.png").convert_alpha()},
            "0-101": {"sprite": pygame.image.load("../resources/tiles/sand_grass/0-101.png").convert_alpha()},
            "100-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/100-1.png").convert_alpha()},
            "-1100": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-1100.png").convert_alpha()},
            "0-110": {"sprite": pygame.image.load("../resources/tiles/sand_grass/0-110.png").convert_alpha()},
            "00-11": {"sprite": pygame.image.load("../resources/tiles/sand_grass/00-11.png").convert_alpha()},
            "1-11-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/1-11-1.png").convert_alpha()},
            "-11-11": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-11-11.png").convert_alpha()},

            # diagonal tiles more grass
            "1-1-11": {"sprite": pygame.image.load("../resources/tiles/sand_grass/1-1-11.png").convert_alpha()},
            "11-1-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/11-1-1.png").convert_alpha()},
            "-1-111": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-1-111.png").convert_alpha()},
            "-111-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-111-1.png").convert_alpha()},

            # diagonal tiles more sand
            "1-1-11S": {"sprite": pygame.image.load("../resources/tiles/sand_grass/1-1-11S.png").convert_alpha()},
            "11-1-1S": {"sprite": pygame.image.load("../resources/tiles/sand_grass/11-1-1S.png").convert_alpha()},
            "-1-111S": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-1-111S.png").convert_alpha()},
            "-111-1S": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-111-1S.png").convert_alpha()},
        }

    def __init__(self, map_width, map_height):
        self.height_map = generate_heightmap(map_width, map_height)
        self.load_tiles()

    def get_tile(self, x, y):
        # determine surrounding height values
        tl = self.height_map[y + 1][x]
        tr = self.height_map[y][x]
        br = self.height_map[y][x + 1]
        bl = self.height_map[y + 1][x + 1]

        height_values = [tl, tr, br, bl]
        min_height : int = min(height_values)
        max_height : int = max(height_values)

        tile_id = str(tr - tl) + str(br - tr) + str(bl - br) + str(tl - bl)

        # if there is any water, return water tile
        if min_height == 0:
            return self.tile_definitions_water.get(tile_id)

        # if there is only sand, return sand tile
        elif max_height <= 2:
            tile_id = tile_variation(tile_id)

            return self.tile_definitions_sand.get(tile_id)

        # if there is sand and grass, return sand grass tile
        elif min_height <= 2 < max_height:
            # if it is a diagonal tile, determine variation
            if abs(max_height - min_height) > 1:
                dominant_height = Counter(height_values).most_common(1)[0][0]
                # if there is more sand than grass, append "more sand" suffix
                if dominant_height < 3:
                    tile_id = tile_id + MORE_SAND_SUFFIX

            return self.tile_definitions_sand_grass.get(tile_id)

        # return grass tile
        else:
            tile_id = tile_variation(tile_id)
            return self.tile_definitions_grass.get(tile_id)

    def render_tiles(self, screen, offset_x, offset_y):
        # Map zeichnen
        for y in range(len(self.height_map) - 1):
            for x in range(len(self.height_map[y]) - 1):
                tile = self.get_tile(x, y)
                terrain_level = self.height_map[y][x]
                if tile:
                    image = tile.get("sprite")
                    screen_x, screen_y = grid_to_screen(x, y, REFERENCE_TILE_DIMENSION, terrain_level)
                    screen_x += offset_x
                    screen_y += offset_y
                    screen.blit(image, (screen_x, screen_y))
