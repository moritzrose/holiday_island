import pygame

from src.game_configuration import SCREEN_WIDTH, SCREEN_HEIGHT, SHOW_INFO_BOX
from src.utils import world_to_tile


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
        self.world_x = self.camera.position_world.x + self.screen_x
        self.world_y = self.camera.position_world.y + self.screen_y

        if SHOW_INFO_BOX:
            self.show_infobox()

    # show tile or vegetation info if available
    def show_infobox(self):

        # screen coordinates
        screen_coordinates = (self.screen_x, self.screen_y)

        # world coordinates
        world_coordinates = (self.world_x, self.world_y)

        # ask gardener
        vegetation_info = self.gardener.get_plant_info(self.world_x, self.world_y)

        # ask architect
        building_info = None # TODO ask architect

        # show info
        print(f"screen coordinates: {screen_coordinates}\n"
              f"world coordinates: {world_coordinates}\n"
              f"vegetation info: {vegetation_info}")