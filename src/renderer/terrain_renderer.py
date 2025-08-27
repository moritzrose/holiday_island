import pygame
from src.game_configuration import MAP_WIDTH, MAP_HEIGHT
from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT


class TerrainRenderer:
    def __init__(self, screen, landscaper):
        self.screen = screen
        self.landscaper = landscaper

        # initialize world terrain surface
        self.surface = pygame.Surface((MAP_WIDTH * REFERENCE_TILE_WIDTH, MAP_HEIGHT * REFERENCE_TILE_HEIGHT),
                                              pygame.SRCALPHA)

    def construct(self):
        # baue world surface
        pass

    def clean(self, ):
        # neu konstruieren, wenn tiles dirty
        pass

    def render(self, camera_position):
        # render world surface
        pass

