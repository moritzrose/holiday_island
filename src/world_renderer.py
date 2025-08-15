import pygame
import random

from src.asset_manager import load_water_tiles, load_sand_tiles, load_grass_tiles, load_sand_grass_tiles
from src.camera import Camera

from collections import Counter
from height_map_generator import HeightMapGenerator
from src.game_configuration import MAP_WIDTH, MAP_HEIGHT
from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT
from src.game_constants import ELEVATION_OFFSET
from src.utils import tile_to_world

MORE_SAND_SUFFIX = "S"

# probabilites for tile variation - sum = 1
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


def calculate_tile_id(height_values):
    tile_id = (
            str(height_values[1] - height_values[0]) +  # tr - tl
            str(height_values[2] - height_values[1]) +  # br - tr
            str(height_values[3] - height_values[2]) +  # bl - br
            str(height_values[0] - height_values[3])  # tl - bl
    )
    return tile_id


class WorldRenderer:

    def __init__(self, service_registry):

        # load height map and tiles
        self.screen = None
        self.height_map_generator = HeightMapGenerator(MAP_WIDTH, MAP_HEIGHT)
        self.height_map = self.height_map_generator.generate_heightmap()

        # load tile surfaces
        self.water_tiles = load_water_tiles()
        self.sand_tiles = load_sand_tiles()
        self.sand_grass_tiles = load_sand_grass_tiles()
        self.grass_tiles = load_grass_tiles()

        # needs rerender?
        self.world_is_clean = False

        # initialize terrain surface to render all tiles on
        self.terrain_surface = pygame.Surface((MAP_WIDTH * REFERENCE_TILE_WIDTH, MAP_HEIGHT * REFERENCE_TILE_HEIGHT),
                                              pygame.SRCALPHA)

        # vegetation
        self.gardener = service_registry.gardener
        self.vegetation_surface_rendered = False
        # initialize vegetation surface to render all plants on
        self.vegetation_surface = pygame.Surface((MAP_WIDTH * REFERENCE_TILE_WIDTH, MAP_HEIGHT * REFERENCE_TILE_HEIGHT),
                                                 pygame.SRCALPHA)

        self.camera = service_registry.camera

    def get_tile(self, height_values):
        """
        Returns the correct tile according to corner height values and terrain level (water/sand/grass) - also applies variation if there are multiple versions of one tile
        """
        # calculate min and max height value
        min_height: int = min(height_values)
        max_height: int = max(height_values)

        # calculate tile_id from height values
        tile_id = calculate_tile_id(height_values)

        # if the tile has any height values = 0, return water tile
        if min_height == 0:
            return self.water_tiles.get(tile_id)

        # if the tile has only height values <= 2, return sand tile
        elif max_height <= 2:
            tile_id = apply_variation(tile_id)
            return self.sand_tiles.get(tile_id)

        # if the tile has height values 1-3, return sand grass tile
        elif min_height <= 2 < max_height:
            # if it is a diagonal tile, determine variation
            if abs(max_height - min_height) > 1:
                dominant_height = Counter(height_values).most_common(1)[0][0]
                # if there is more sand than grass, append "more sand" suffix
                if dominant_height < 3:
                    tile_id = tile_id + MORE_SAND_SUFFIX

            return self.sand_grass_tiles.get(tile_id)

        # if the tile only has height values >= 3, return grass tile
        else:
            tile_id = apply_variation(tile_id)
            return self.grass_tiles.get(tile_id)

    def set_screen(self, screen):
        self.screen = screen

    def render_world(self):

        # nothing dirty to rerender
        if self.world_is_clean:
            # camera position on the world map surface
            offset_x = self.camera.position_world.x
            offset_y = self.camera.position_world.y

            self.screen.blit(self.terrain_surface, (-offset_x, -offset_y))
            self.screen.blit(self.vegetation_surface, (-offset_x, -offset_y))
            return

        for row in range(len(self.height_map) - 1):
            for col in range(len(self.height_map[row]) - 1):
                # determine corner height values
                tl = self.height_map[row + 1][col]
                tr = self.height_map[row][col]
                br = self.height_map[row][col + 1]
                bl = self.height_map[row + 1][col + 1]
                height_values = [tl, tr, br, bl]

                self.render_terrain(height_values, col, row)
                self.render_vegetation(height_values, col, row)

        self.world_is_clean = True

    def render_terrain(self, height_values, tile_x, tile_y):
        tile = self.get_tile(height_values)

        # get terrain level for the current tile
        terrain_level = self.height_map[tile_y][tile_x]

        if tile:
            image = tile.get("sprite")

            # calculate world coordinates for the current tile
            world_x, world_y = tile_to_world(tile_x, tile_y)

            # account for terrain level
            world_y -= terrain_level * ELEVATION_OFFSET

            # adjust to the middle of the terrain surface
            world_x += self.terrain_surface.get_width() * 0.5 - REFERENCE_TILE_WIDTH * 0.5

            # draw all tiles as one terrain surface to avoid unnecessary rerendering of every single tile
            self.terrain_surface.blit(image, (world_x, world_y))

    def render_vegetation(self, height_values, tile_x, tile_y):

        # calculate tile_id from height values
        tile_id = calculate_tile_id(height_values)

        terrain_level = self.height_map[tile_y][tile_x]


        if terrain_level > 0:
            plant = self.gardener.grow_plants(tile_id, tile_x,
                                              tile_y)
            if plant:
                image = plant.get("sprite")

                # calculate world coordinates
                world_x, world_y = tile_to_world(tile_x, tile_y)

                # account for terrain level
                world_y -= terrain_level * ELEVATION_OFFSET

                # adjust to the middle of the vegetation surface
                world_x += self.vegetation_surface.get_width() * 0.5 - REFERENCE_TILE_WIDTH * 0.5

                # center on current tile (approximately)
                world_x += (REFERENCE_TILE_WIDTH - image.get_width()) * 0.5
                world_y -= REFERENCE_TILE_HEIGHT * 0.25

                self.vegetation_surface.blit(image, (world_x, world_y))
