class VegetationRenderer:
    def __init__(self,screen, gardener):
        self.screen = screen
        self.gardener = gardener

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