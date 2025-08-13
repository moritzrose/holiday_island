

class Tile:
    def __init__(self, tile_id, grid_x, grid_y):

        self.tile_id = tile_id

        self.grid_x = grid_x
        self.grid_y = grid_y

        self.is_dirty = False
        #
        self.building = None
