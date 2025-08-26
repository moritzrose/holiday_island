class DebugRenderer:
    def __init__(self,screen, debugger):
        self.screen = screen
        self.debugger = debugger

        # initialize world terrain surface
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT),
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