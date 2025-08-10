import pygame
from world_configuration import Config

class Camera:
    def __init__(self, start_x, start_y):
        self.width = Config.SCREEN_WIDTH
        self.height = Config.SCREEN_HEIGHT

        self.scroll = pygame.Vector2(start_x,start_y)

        # movement chunks in x and y
        self.dx = 0
        self.dy = 0

        # scrolling speed
        self.speed = 15

    def update(self):

        mouse_pos_x = pygame.mouse.get_pos()[0]
        mouse_pos_y = pygame.mouse.get_pos()[1]

        # horizontal edge
        if mouse_pos_x > 0.97 * self.width:
            self.dx = -self.speed
        elif mouse_pos_x < 0.03 * self.width:
            self.dx = self.speed
        else:
            self.dx = 0

        # vertical edge
        if mouse_pos_y > 0.97 * self.height:
            self.dy = -self.speed
        elif mouse_pos_y < 0.03 * self.height:
            self.dy = self.speed
        else:
            self.dy = 0

        # update camera position
        self.scroll.x += self.dx
        self.scroll.y += self.dy