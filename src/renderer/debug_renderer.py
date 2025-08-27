import pygame
from src.game_configuration import MAP_WIDTH, MAP_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT

class DebugRenderer:
    def __init__(self,screen, debugger):
        self.screen = screen
        self.debugger = debugger

        # initialize debug surface
        self.debug_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT),
                                            pygame.SRCALPHA)

    def construct(self):
        # baue world surface
        pass

    def clean(self, ):
        # neu konstruieren, wenn tiles dirty
        pass

    def render(self, camera_position):

        # render surface according to camera position
        self.screen.blit(self.debug_surface, (-camera_position.x, -camera_position.y))