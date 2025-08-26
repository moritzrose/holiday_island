import pygame

from src.game_configuration import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_WIDTH, MAP_HEIGHT
from src.service_registry import ServiceRegistry

# background colour
BG = (50, 50, 50)


class App:
    def __init__(self):

        # Initialize pygame
        pygame.init()

        # Create window
        pygame.display.set_caption("Holiday Island")

        # Mouse
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.event.set_grab(False)

        # Screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Game
        self.game = Game(screen)


        # Service Registry - contains singletons of all components
        #self.service_registry = ServiceRegistry()

        # asset manager
        #self.asset_manager = AssetManager()
        # Camera
        #self.camera = self.service_registry.camera

        # Cursor
        #self.cursor = self.service_registry.cursor

        # World Renderer
        #self.world_renderer = self.service_registry.world_renderer
        #self.world_renderer.set_screen(self.screen)

        #self.running = True

    def run(self):

        clock = pygame.time.Clock()

        while self.running:

            # set frame rate - no clue what is actually does TODO
            clock.tick(60)

            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update background
            self.screen.fill(BG)

            # update cursor position
            self.cursor.update(screen)

            # update camera position
            #self.camera.update()

            # render map
            self.world_renderer.render_world()

            # update display
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.game.run()