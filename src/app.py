import pygame
from map_renderer import MapRenderer
from src.world_configuration import Config

# background colour
BG = (50, 50, 50)
DEBUG = False

class App:
    def __init__(self):

        # Initialize pygame
        pygame.init()

        # Create window
        pygame.display.set_caption("Holiday Island")

        # Mouse
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.event.set_grab(True)

        # Screen
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

        # Map Generator
        self.map_generator = MapRenderer(Config.MAP_WIDTH, Config.MAP_HEIGHT)

        self.running = True

    def run(self):

        clock = pygame.time.Clock()

        while self.running:

            # set frame rate
            clock.tick(60)

            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update background
            self.screen.fill(BG)

            # render map
            self.map_generator.render_map(self.screen)

            # update display
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.run()