import pygame
from src.game_configuration import MAP_WIDTH, MAP_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT
from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT

class UIRenderer():
    def __init__(self,screen, designer):
        self.screen = screen
        self.designer = designer

        # initialize ui_surface
        self.ui_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT),
                                         pygame.SRCALPHA)

    def construct(self):
        # baue world surface
        pass

    def clean(self, ):
        # neu konstruieren, wenn tiles dirty
        pass

    def render(self, camera_position):

        # render surface according to camera position
        self.screen.blit(self.ui_surface, (-camera_position.x, -camera_position.y))