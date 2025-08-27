import pygame

from src.game import Game
from src.game_configuration import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_WIDTH, MAP_HEIGHT

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
        self.game = Game(self.screen)

        # Clock
        self.clock = pygame.time.Clock()

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

        self.running = True

    def run(self):

        while self.running:

            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    if hasattr(self.game, "handle_event"):
                        self.game.handle_event(event)

            # set frame rate
            dt_ms = self.clock.tick(60)
            dt = dt_ms / 1000

            # update game state
            self.game.update(dt)

            # update background
            self.screen.fill(BG)
            self.game.render()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.run()