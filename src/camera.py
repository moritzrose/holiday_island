import pygame
from src.game_configuration import CAMERA_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, MAP_WIDTH, MAP_HEIGHT
from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT


class Camera:
    def __init__(self):

        # initial position of the camera
        start_world_x = 0 # MAP_WIDTH * REFERENCE_TILE_WIDTH / 2 # -  SCREEN_WIDTH / 2
        start_world_y = 0 # MAP_HEIGHT * REFERENCE_TILE_HEIGHT / 2 - SCREEN_HEIGHT / 2

        self.position_world = pygame.Vector2(start_world_x, start_world_y)

        # movement chunks per frame
        self.dx = 0
        self.dy = 0

    def update(self):

        mouse_pos_x = pygame.mouse.get_pos()[0]
        mouse_pos_y = pygame.mouse.get_pos()[1]

        # horizontal edge
        if mouse_pos_x > 0.97 * SCREEN_WIDTH:
            self.dx = CAMERA_SPEED
        elif mouse_pos_x < 0.03 * SCREEN_WIDTH:
            self.dx = -CAMERA_SPEED
        else:
            self.dx = 0

        # vertical edge
        if mouse_pos_y > 0.97 * SCREEN_HEIGHT:
            self.dy = CAMERA_SPEED
        elif mouse_pos_y < 0.03 * SCREEN_HEIGHT:
            self.dy = -CAMERA_SPEED
        else:
            self.dy = 0

        # update camera position
        self.position_world.x += self.dx
        self.position_world.y += self.dy
