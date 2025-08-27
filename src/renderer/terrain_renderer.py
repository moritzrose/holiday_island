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
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                # projection coordinates
                projection_x, projection_y = self.landscaper.determine_location(x,y)
                # sprite
                sprite = self.landscaper.determine_sprite(x,y)
                # build world surface
                self.surface.blit(sprite, (projection_x, projection_y))

    def render(self, camera_position):

        # camera off set
        offset_x = -camera_position.x
        offset_y = -camera_position.y

        # render world surface at camera position
        self.screen.blit(self.surface,(offset_x, offset_y))

