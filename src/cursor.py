import pygame

from src.asset_manager import load_cheat_tiles
from src.game_configuration import SCREEN_WIDTH, SCREEN_HEIGHT, SHOW_INFO_BOX, MAP_WIDTH
from src.game_constants import REFERENCE_TILE_WIDTH, REFERENCE_TILE_HEIGHT
from src.utils import world_to_tile, calculate_tile_id

RED = (255, 0, 0)


class Cursor:

    def __init__(self):
        # if I ever want to add one
        self.icon = None

        # screen coordinates
        self.screen_x = None
        self.screen_y = None

        # tile coordinates
        self.tile_x = None
        self.tile_y = None

        # world coordinates
        self.world_x = None
        self.world_y = None

        # camera, to calculate world coordinates
        #self.camera = service_registry.camera

        # world height map to calculate correct tile coordinates
        #self.world_renderer = service_registry.world_renderer

        # gardener, to get vegetation info
        #self.gardener = service_registry.gardener

        #self.cheat_tiles = load_cheat_tiles()

        # architect, to get building info TODO add architect
        # self.architect = role_registry.architect

    def mouse_in_tile(self, mouse_x, mouse_y, screen_x, screen_y, tile_id):
        local_x = mouse_x - screen_x
        local_y = mouse_y - screen_y

        sprite = grass_sprites.get(tile_id).get("sprite") # TODO grass sprites aus worldrenderer holen
        sprite_mask = grass_sprite_masks.get(tile_id + "M") # TODO sprite masks erzeugen oder holen

        if 0 <= local_x < sprite.get_width() and 0 <= local_y < sprite.get_height():
            return sprite_mask.get_at((local_x, local_y)) == 1

    # update screen and grid coordinates
    def update(self, screen):
        self.screen_x = pygame.mouse.get_pos()[0]
        self.screen_y = pygame.mouse.get_pos()[1]

        # calculate world coordinates from camera offset
        self.world_x = int (self.camera.position_world.x + self.screen_x)
        self.world_y = int (self.camera.position_world.y + self.screen_y)

        # mouse pos to grid coordinates
        grid_x, grid_y = projection_to_grid(mouse_x, mouse_y)


        # grid coordinates to screen coordinates
        screen_x, screen_y = grid_to_projection(grid_x, grid_y, height_map[grid_y][grid_x])

        self.world_renderer.calculate_tile_id(grid_x, grid_y)

        if mouse_in_tile(self.screen_x, self.screen_y, screen_x, screen_y, tile_id):
            sprite = highlight_sprites.get(tile_id).get("sprite") # TODO highlight sprites fehlen
            self.tile_x = grid_x
            self.tile_y = grid_y
            screen.blit(sprite, (screen_x, screen_y))
            return

        # if the cursor is not in the sprite of the calculated tile, check neighbours
        neighbours = [(grid_x - 1, grid_y), (grid_x, grid_y - 1), (grid_x + 1, grid_y), (grid_x, grid_y + 1)]

        for neighbour in neighbours:
            temp_grid_x = neighbour[0]
            temp_grid_y = neighbour[1]

            temp_grid_x = min(len(height_map[0]) - 2, temp_grid_x)
            temp_grid_y = min(len(height_map) - 2, temp_grid_y)

            temp_grid_x = max(0, temp_grid_x)
            temp_grid_y = max(0, temp_grid_y)

            screen_x, screen_y = grid_to_projection(temp_grid_x, temp_grid_y, height_map[temp_grid_y][temp_grid_x])
            tile_id = self.world_renderer.calculate_tile_id(temp_grid_x, temp_grid_y)

            if mouse_in_tile(mouse_x, mouse_y, screen_x, screen_y, tile_id):
                sprite = highlight_sprites.get(tile_id).get("sprite")
                screen.blit(sprite, (screen_x, screen_y))
                return

        # if still not, check the diagonal neighbours
        diagonal_neighbours = [(grid_x - 1, grid_y - 1), (grid_x + 1, grid_y - 1), (grid_x + 1, grid_y + 1), (grid_x - 1, grid_y + 1)]

        for neighbour in diagonal_neighbours:
            temp_grid_x = neighbour[0]
            temp_grid_y = neighbour[1]

            temp_grid_x = min(len(height_map[0]) - 2, temp_grid_x)
            temp_grid_y = min(len(height_map) - 2, temp_grid_y)

            temp_grid_x = max(0, temp_grid_x)
            temp_grid_y = max(0, temp_grid_y)

            screen_x, screen_y = grid_to_projection(temp_grid_x, temp_grid_y, height_map[temp_grid_y][temp_grid_x])
            tile_id = self.world_renderer.calculate_tile_id(temp_grid_x, temp_grid_y)

            if mouse_in_tile(mouse_x, mouse_y, screen_x, screen_y, tile_id):
                sprite = highlight_sprites.get(tile_id).get("sprite")
                screen.blit(sprite, (screen_x, screen_y))
                return

        if SHOW_INFO_BOX:
            self.show_infobox()

    # show tile or vegetation info if available
    def show_infobox(self):
        # screen coordinates
        screen_coordinates = (self.screen_x, self.screen_y)

        # world coordinates
        world_coordinates = (self.world_x, self.world_y)

        # tile coordinates
        tile_coordinates = (self.tile_x, self.tile_y)

        # ask gardener
        vegetation_info = self.gardener.get_plant_info(self.tile_x, self.tile_y)

        # ask architect
        building_info = None  # TODO ask architect

        # show info
        print(f"screen coordinates: {screen_coordinates}\n"
              f"world coordinates: {world_coordinates}\n"
              f"tile coordinates: {tile_coordinates}\n"
              f"vegetation info: {vegetation_info}")
