import pygame
from map_renderer import MapRenderer


# Configuration
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
MAP_WIDTH = 200
MAP_HEIGHT = 200
BG = (50, 50, 50)
DEBUG = False

class App:
    def __init__(self):

        # Initialize pygame
        pygame.init()

        # Create window
        pygame.display.set_caption("Holiday Island")

      # Screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Map Generator
        self.map_generator = MapRenderer(MAP_WIDTH, MAP_HEIGHT)

        self.running = True

    def run(self):

        clock = pygame.time.Clock()

        while self.running:

            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update background
            self.screen.fill(BG)

            # render map
            self.map_generator.render_tiles(self.screen, 600, 300)

            # set frame rate
            clock.tick(60)

            # update display
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.run()