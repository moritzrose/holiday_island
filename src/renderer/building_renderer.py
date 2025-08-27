import pygame
from src.game_configuration import MAP_WIDTH, MAP_HEIGHT
from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT

class BuildingRenderer:
    def __init__(self,screen, architect):
        self.screen = screen
        self.architect = architect

        # initialize building surface
        self.building_surface = pygame.Surface((MAP_WIDTH * REFERENCE_TILE_WIDTH, MAP_HEIGHT * REFERENCE_TILE_HEIGHT),
                                               pygame.SRCALPHA)

    def construct(self):
        # baue world surface
        pass

    def clean(self, ):
        # neu konstruieren, wenn tiles dirty
        pass

    def render(self, camera_position):

        # render surface according to camera position
        self.screen.blit(self.building_surface, (-camera_position.x, -camera_position.y))