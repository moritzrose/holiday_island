import pygame

from src.game_configuration import SCREEN_WIDTH, SCREEN_HEIGHT, SHOW_INFO_BOX, MAP_WIDTH
from src.game_constants import MAX_TERRAIN_LEVEL, REFERENCE_TILE_WIDTH, ELEVATION_OFFSET

from src.utils import world_to_tile


class Cursor:

    def __init__(self, service_registry):

        # if I ever want to add one
        self.icon = None

        # screen coordinates
        self.screen_x = None
        self.screen_y = None

        # tile coordinates
        self.tile_x = None
        self.tile_y = None

        # world coordinates
        self.world_x = None
        self.world_y = None

        # camera, to calculate world coordinates
        self.camera = service_registry.camera

        # world height map to calculate correct tile coordinates
        self.height_map = service_registry.world_renderer.height_map

        # gardener, to get vegetation info
        self.gardener = service_registry.gardener

        # architect, to get building info TODO add architect
        # self.architect = role_registry.architect

    # update screen and grid coordinates
    def update(self):
        self.screen_x = pygame.mouse.get_pos()[0]
        self.screen_y = pygame.mouse.get_pos()[1]

        # calculate world coordinates from camera offset
        self.world_x = self.camera.position_world.x + self.screen_x
        self.world_y = self.camera.position_world.y + self.screen_y

        # 1. loop through all possible terrain level offsets h, starting with hmax = MAX_TERRAIN_LEVEL
        # 2. compare terrain level of tile(x,y) with terrain level in height map
        # 3. first match means tile_x and tile_y are correct - ask me if you do not understand this - it took me a while as well!

        # account for surface offsets which changes the tiles' screen_x coordinate
        world_pos_no_offset_x = self.world_x - 0.5 * MAP_WIDTH * REFERENCE_TILE_WIDTH + 0.5 * REFERENCE_TILE_WIDTH

        for terrain_level in range(MAX_TERRAIN_LEVEL, -1, -1):

            # account for terrain level, which offsets the tiles' screen_y coordinate
            world_pos_no_offset_y = self.world_y - ELEVATION_OFFSET * terrain_level

            tile_x, tile_y = world_to_tile(world_pos_no_offset_x, world_pos_no_offset_y, terrain_level)
            if self.height_map[tile_y][tile_x] >= terrain_level:
                self.tile_x = tile_x
                self.tile_y = tile_y
                break;

        if SHOW_INFO_BOX:
            self.show_infobox()

    # show tile or vegetation info if available
    def show_infobox(self):

        # screen coordinates
        screen_coordinates = (self.screen_x, self.screen_y)

        # world coordinates
        world_coordinates = (self.world_x, self.world_y)

        # tile coordinates
        tile_coordinates = (self.tile_x, self.tile_y)

        # ask gardener
        vegetation_info = self.gardener.get_plant_info(self.tile_x, self.tile_y)

        # ask architect
        building_info = None # TODO ask architect

        # show info
        print(f"screen coordinates: {screen_coordinates}\n"
              f"world coordinates: {world_coordinates}\n"
              f"tile coordinates: {tile_coordinates}\n"
              f"vegetation info: {vegetation_info}")