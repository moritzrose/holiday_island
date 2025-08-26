class Game:
    def __init__(self,screen):

        # basics
        self.seed = 49 #42
        self.clock = pygame.time.Clock()
        self.height_map = generate_heightmap(seed)
        self.camera = Camera()
        self.cursor = Cursor()

        # staff
        self.asset_manager = AssetManager() # assets
        self.landscaper = LandScaper(self.height_map) # terrain
        self.gardener = Gardener() # vegetation
        self.architect = Architect() # buildings
        self.designer = Designer() # UI
        self.debugger = Debugger()

        # renderer
        # 0–9 → background, world
        # 10–49 → entities, effects
        # 50–89 → particles
        # 90–99 → GUI / HUD
        # 100+ → Debug, Developer-Overlays
        self.renderers = [
        (0, TerrainRenderer(screen, self.landscaper)),
        (10, VegetationRenderer(screen, self.gardener)),
        (20, BuildingRenderer(screen, self.architect)),
        (90, UIRenderer(screen, self.designer)),
        (100, DebugRenderer(screen, self.debugger))
        ]

        self.renderers.sort(key=lambda x: x[0])

        # construct world surface
        for _, renderer in self.renderers:
            renderer.construct()

    def run(self):

        running = True

        while running:

            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # update background
            self.screen.fill(BG)

            # construct world surface
            for _, renderer in self.renderers:
                renderer.render()

            # update display
            pygame.display.update()

            # set frame rate
            self.clock.tick(60)

        pygame.quit()

