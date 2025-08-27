from src.game_configuration import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_WIDTH, MAP_HEIGHT
from src.height_map_generator import generate_heightmap
from src.camera import Camera
from src.cursor import Cursor
from src.staff.asset_manager import AssetManager
from src.staff.landscaper import Landscaper
from src.staff.gardener import Gardener
from src.staff.architect import Architect
from src.staff.designer import Designer
from src.staff.debugger import Debugger
from src.renderer.building_renderer import BuildingRenderer
from src.renderer.debug_renderer import DebugRenderer
from src.renderer.terrain_renderer import TerrainRenderer
from src.renderer.ui_renderer import UIRenderer
from src.renderer.vegetation_renderer import VegetationRenderer


class Game:
    def __init__(self,screen):

        # basics
        self.seed = 49 #42
        self.camera = Camera()
        self.cursor = Cursor()

        # map settings
        self.height_map = generate_heightmap(self.seed, MAP_WIDTH, MAP_HEIGHT)

        # staff
        self.asset_manager = AssetManager() # assets
        self.landscaper = Landscaper(self.height_map) # terrain
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
        for _, r in sorted(self.renderers, key=lambda x: x[0]):
            r.construct()


    # handle game events
    def handle_event(self, event):
        pass

    # update game logic
    def update(self, dt):
        pass

        # update cursor position
        #self.cursor.update(screen)

        # update camera position
        #self.camera.update()

        # render map
        #self.world_renderer.render_world()

        # update display
        #pygame.display.update()

    # render all surfaces
    def render(self):
        for _, renderer in sorted(self.renderers, key=lambda x: x[0]):
            renderer.render(self.camera.position)


