import pygame

from src.game_configuration import SCREEN_WIDTH, SCREEN_HEIGHT, SHOW_INFO_BOX
from src.utils import world_to_grid


class Cursor:

    def __init__(self, service_registry):

        # if I ever want to add one
        self.icon = None

        # screen coordinates
        self.screen_x = None
        self.screen_y = None

        # world coordinates
        self.world_x = None
        self.world_y = None

        # grid coordinates calculated from screen coordinates
        self.grid_x = None
        self.grid_y = None

        # camera, to calculate world coordinates
        self.camera = service_registry.camera

        # gardener, to get vegetation info
        self.gardener = service_registry.gardener

        # architect, to get building info TODO add architect
        # self.architect = role_registry.architect

    # update screen and grid coordinates
    def update(self):
        self.screen_x = pygame.mouse.get_pos()[0]
        self.screen_y = pygame.mouse.get_pos()[1]

        # calculate world coordinates from camera offset
        self.world_x = self.camera.scroll.x + self.screen_x
        self.world_y = self.camera.scroll.y + self.screen_y

        self.grid_x, self.grid_y = world_to_grid(self.world_x, self.world_y)

        if SHOW_INFO_BOX:
            self.show_infobox()

    # show tile or vegetation info if available
    def show_infobox(self):

        # screen coordinates
        screen_coordinates = (self.screen_x, self.screen_y)

        # world coordinates
        world_coordinates = None

        # grid coordinates
        grid_coordinates = (self.grid_x, self.grid_y)

        # ask gardener
        vegetation_info = self.gardener.get_plant_info(self.grid_x, self.grid_y)

        # ask architect
        building_info = None # TODO ask architect

        # show info
        print(f"screen coordinates: {screen_coordinates}\n"
              f"grid coordiantes: {grid_coordinates}\n"
              f"vegetation info: {vegetation_info}")