import pygame
import random
from src.camera import Camera

from collections import Counter
from height_map_generator import HeightMapGenerator
from src.gardener import Gardener

REFERENCE_TILE_DIMENSION_X = 62
REFERENCE_TILE_DIMENSION_Y = 32
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


def calculate_tile_id(height_values):
    tile_id = (
            str(height_values[1] - height_values[0]) +  # tr - tl
            str(height_values[2] - height_values[1]) +  # br - tr
            str(height_values[3] - height_values[2]) +  # bl - br
            str(height_values[0] - height_values[3])  # tl - bl
    )
    return tile_id


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

            # basic tiles
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

            # variation a
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

            # variation b
            "0000b": {"sprite": pygame.image.load("../resources/tiles/sand/b/0000.png").convert_alpha()},

            # variation c
            "0000c": {"sprite": pygame.image.load("../resources/tiles/sand/c/0000.png").convert_alpha()},
        }

        self.tile_definitions_grass = {

            # basic
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

            # variation a
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

            # variation b
            "0000b": {"sprite": pygame.image.load("../resources/tiles/grass/b/0000.png").convert_alpha()},

            # variation c
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

        # load height map and tiles
        self.height_map_generator = HeightMapGenerator(map_width, map_height)
        self.height_map = self.height_map_generator.generate_heightmap()

        # load tile surfaces
        self.load_tiles()

        self.world_is_clean = False

        # render one surface consisting of all tiles, instead of every tile over and over
        self.terrain_surface = pygame.Surface((map_width * REFERENCE_TILE_DIMENSION_X , map_height * REFERENCE_TILE_DIMENSION_Y), pygame.SRCALPHA)

        # vegetation
        self.gardener = Gardener()
        self.vegetation_surface_rendered = False
        self.vegetation_surface = pygame.Surface((map_width * REFERENCE_TILE_DIMENSION_X , map_height * REFERENCE_TILE_DIMENSION_Y), pygame.SRCALPHA)

        # Camera
        start_pos_x = self.terrain_surface.get_width() * -0.5
        start_pos_y = self.terrain_surface.get_height() * -0.5
        self.camera = Camera(start_pos_x, start_pos_y)

    def get_tile(self, height_values):

        # calculate min and max height value

        min_height: int = min(height_values)
        max_height: int = max(height_values)

        # calculate tile_id from height values
        tile_id = calculate_tile_id(height_values)

        # if the tile has any height values = 0, return water tile
        if min_height == 0:
            return self.tile_definitions_water.get(tile_id)

        # if the tile has only height values <= 2, return sand tile
        elif max_height <= 2:
            tile_id = apply_variation(tile_id)
            return self.tile_definitions_sand.get(tile_id)

        # if the tile has height values 1-3, return sand grass tile
        elif min_height <= 2 < max_height:
            # if it is a diagonal tile, determine variation
            if abs(max_height - min_height) > 1:
                dominant_height = Counter(height_values).most_common(1)[0][0]
                # if there is more sand than grass, append "more sand" suffix
                if dominant_height < 3:
                    tile_id = tile_id + MORE_SAND_SUFFIX

            return self.tile_definitions_sand_grass.get(tile_id)

        # if the tile only has height values >= 3, return grass tile
        else:
            tile_id = apply_variation(tile_id)
            return self.tile_definitions_grass.get(tile_id)

    def render_world(self, screen):

        # nothing dirty to rerender
        if self.world_is_clean:

            # camera position on the world map surface
            offset_x = self.camera.scroll.x
            offset_y = self.camera.scroll.y
            self.camera.update()

            screen.blit(self.terrain_surface, (offset_x, offset_y))
            screen.blit(self.vegetation_surface, (offset_x, offset_y))
            return

        # draw world map as one surface to avoid unnecessary rerendering of every single tile
        for y in range(len(self.height_map) - 1):
            for x in range(len(self.height_map[y]) - 1):

                # determine corner height values
                tl = self.height_map[y + 1][x]
                tr = self.height_map[y][x]
                br = self.height_map[y][x + 1]
                bl = self.height_map[y + 1][x + 1]
                height_values = [tl, tr, br, bl]

                self.render_terrain(height_values, x, y)
                self.render_decoration(height_values, x, y)

        self.world_is_clean = True

    def render_terrain(self, height_values, x, y):
        tile = self.get_tile(height_values)
        terrain_level = self.height_map[y][x]
        if tile:
            image = tile.get("sprite")
            screen_x, screen_y = grid_to_screen(x, y, (REFERENCE_TILE_DIMENSION_X, REFERENCE_TILE_DIMENSION_Y),
                                                terrain_level)

            # draw in the middle of the world map surface
            screen_x += self.terrain_surface.get_width() * 0.5
            self.terrain_surface.blit(image, (screen_x, screen_y))

    def render_decoration(self, height_values, x, y):

        # calculate tile_id from height values
        tile_id = calculate_tile_id(height_values)
        terrain_level = self.height_map[y][x]
        if terrain_level > 0:
            plant = self.gardener.grow_plants(tile_id) #TODO hier weiter machen, Tile instanziieren, Tile speichern usw.
            plant_grows = plant is not None  # just because I can
            if plant_grows:
                image = plant.get("sprite")
                screen_x, screen_y = grid_to_screen(x, y, (REFERENCE_TILE_DIMENSION_X, REFERENCE_TILE_DIMENSION_Y),
                                                    terrain_level)
                # draw in the middle of the world map surface
                screen_x += self.terrain_surface.get_width() * 0.5
                # center one tile horiontally
                screen_x += REFERENCE_TILE_DIMENSION_X * 0.5
                self.vegetation_surface.blit(image, (screen_x, screen_y))