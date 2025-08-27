class InteractionRenderer:
    def __init__(self, screen, landscaper, gardener, architect):
        self.screen = screen
        self.landscaper = landscaper
        self.gardener = gardener
        self.architect = architect

    def render(self, camera_position):

        # camera off set
        offset_x = -camera_position.x
        offset_y = -camera_position.y

        # render world surface at camera position
        self.screen.blit(self.surface,(offset_x, offset_y))