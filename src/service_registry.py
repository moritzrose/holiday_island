# this class holds an instance of each role (gardener, architect, ...) and passes them to subclasses if needed
from src.camera import Camera
from src.cursor import Cursor
from src.gardener import Gardener
from src.world_renderer import WorldRenderer


class ServiceRegistry:

    def __init__(self):

        # world builder
        self.gardener = Gardener()

        # Basics
        self.camera = Camera()

        # renderer
        self.world_renderer = WorldRenderer(self)

        self.cursor = Cursor(self)

