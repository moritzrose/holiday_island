import pygame

class AssetManager:
    def __init__(self):
        self.water_tiles = self.load_water_tiles()
        self.sand_tiles = self.load_sand_tiles()
        self.sand_grass_tiles = self.load_sand_grass_tiles()
        self.grass_tiles = self.load_grass_tiles()
        self.highlight_tiles = self.load_highlight_tiles()
        self.plants = self.load_plants()

    # terrain

    def load_water_tiles(self):
        water_tiles = {
            "0000": pygame.image.load("../resources/tiles/water/0000.png").convert_alpha(),
            "1-100": pygame.image.load("../resources/tiles/water/1-100.png").convert_alpha(),
            "01-10": pygame.image.load("../resources/tiles/water/01-10.png").convert_alpha(),
            "001-1": pygame.image.load("../resources/tiles/water/001-1.png").convert_alpha(),
            "-1001": pygame.image.load("../resources/tiles/water/-1001.png").convert_alpha(),
            "10-10": pygame.image.load("../resources/tiles/water/10-10.png").convert_alpha(),
            "-1010": pygame.image.load("../resources/tiles/water/-1010.png").convert_alpha(),
            "010-1": pygame.image.load("../resources/tiles/water/010-1.png").convert_alpha(),
            "0-101": pygame.image.load("../resources/tiles/water/0-101.png").convert_alpha(),
            "100-1": pygame.image.load("../resources/tiles/water/100-1.png").convert_alpha(),
            "-1100": pygame.image.load("../resources/tiles/water/-1100.png").convert_alpha(),
            "0-110": pygame.image.load("../resources/tiles/water/0-110.png").convert_alpha(),
            "00-11": pygame.image.load("../resources/tiles/water/00-11.png").convert_alpha(),
            "1-11-1": pygame.image.load("../resources/tiles/water/1-11-1.png").convert_alpha(),
            "-11-11": pygame.image.load("../resources/tiles/water/-11-11.png").convert_alpha(),
            "11-1-1": pygame.image.load("../resources/tiles/water/11-1-1.png").convert_alpha(),
            "1-1-11": pygame.image.load("../resources/tiles/water/1-1-11.png").convert_alpha(),
            "-1-111": pygame.image.load("../resources/tiles/water/-1-111.png").convert_alpha(),
            "-111-1": pygame.image.load("../resources/tiles/water/-111-1.png").convert_alpha(),
        }
        return water_tiles

    def load_sand_tiles(self):

        sand_tiles = {

            # basic tiles
            "0000": pygame.image.load("../resources/tiles/sand/basic/0000.png").convert_alpha(),
            "1-100": pygame.image.load("../resources/tiles/sand/basic/1-100.png").convert_alpha(),
            "01-10": pygame.image.load("../resources/tiles/sand/basic/01-10.png").convert_alpha(),
            "001-1": pygame.image.load("../resources/tiles/sand/basic/001-1.png").convert_alpha(),
            "-1001": pygame.image.load("../resources/tiles/sand/basic/-1001.png").convert_alpha(),
            "10-10": pygame.image.load("../resources/tiles/sand/basic/10-10.png").convert_alpha(),
            "-1010": pygame.image.load("../resources/tiles/sand/basic/-1010.png").convert_alpha(),
            "010-1": pygame.image.load("../resources/tiles/sand/basic/010-1.png").convert_alpha(),
            "0-101": pygame.image.load("../resources/tiles/sand/basic/0-101.png").convert_alpha(),
            "100-1": pygame.image.load("../resources/tiles/sand/basic/100-1.png").convert_alpha(),
            "-1100": pygame.image.load("../resources/tiles/sand/basic/-1100.png").convert_alpha(),
            "0-110": pygame.image.load("../resources/tiles/sand/basic/0-110.png").convert_alpha(),
            "00-11": pygame.image.load("../resources/tiles/sand/basic/00-11.png").convert_alpha(),
            "1-11-1": pygame.image.load("../resources/tiles/sand/basic/1-11-1.png").convert_alpha(),
            "-11-11": pygame.image.load("../resources/tiles/sand/basic/-11-11.png").convert_alpha(),
            "11-1-1": pygame.image.load("../resources/tiles/sand/basic/11-1-1.png").convert_alpha(),
            "1-1-11": pygame.image.load("../resources/tiles/sand/basic/1-1-11.png").convert_alpha(),
            "-1-111": pygame.image.load("../resources/tiles/sand/basic/-1-111.png").convert_alpha(),
            "-111-1": pygame.image.load("../resources/tiles/sand/basic/-111-1.png").convert_alpha(),

            # variation a
            "0000a": pygame.image.load("../resources/tiles/sand/a/0000.png").convert_alpha(),
            "1-100a": pygame.image.load("../resources/tiles/sand/a/1-100.png").convert_alpha(),
            "01-10a": pygame.image.load("../resources/tiles/sand/a/01-10.png").convert_alpha(),
            "001-1a": pygame.image.load("../resources/tiles/sand/a/001-1.png").convert_alpha(),
            "-1001a": pygame.image.load("../resources/tiles/sand/a/-1001.png").convert_alpha(),
            "10-10a": pygame.image.load("../resources/tiles/sand/a/10-10.png").convert_alpha(),
            "-1010a": pygame.image.load("../resources/tiles/sand/a/-1010.png").convert_alpha(),
            "010-1a": pygame.image.load("../resources/tiles/sand/a/010-1.png").convert_alpha(),
            "0-101a": pygame.image.load("../resources/tiles/sand/a/0-101.png").convert_alpha(),
            "100-1a": pygame.image.load("../resources/tiles/sand/a/100-1.png").convert_alpha(),
            "-1100a": pygame.image.load("../resources/tiles/sand/a/-1100.png").convert_alpha(),
            "0-110a": pygame.image.load("../resources/tiles/sand/a/0-110.png").convert_alpha(),
            "00-11a": pygame.image.load("../resources/tiles/sand/a/00-11.png").convert_alpha(),
            "1-11-1a": pygame.image.load("../resources/tiles/sand/a/1-11-1.png").convert_alpha(),
            "-11-11a": pygame.image.load("../resources/tiles/sand/a/-11-11.png").convert_alpha(),
            "11-1-1a": pygame.image.load("../resources/tiles/sand/a/11-1-1.png").convert_alpha(),
            "1-1-11a": pygame.image.load("../resources/tiles/sand/a/1-1-11.png").convert_alpha(),
            "-1-111a": pygame.image.load("../resources/tiles/sand/a/-1-111.png").convert_alpha(),
            "-111-1a": pygame.image.load("../resources/tiles/sand/a/-111-1.png").convert_alpha(),

            # variation b
            "0000b": pygame.image.load("../resources/tiles/sand/b/0000.png").convert_alpha(),

            # variation c
            "0000c": pygame.image.load("../resources/tiles/sand/c/0000.png").convert_alpha(),
        }
        return sand_tiles

    def load_sand_grass_tiles(self):

        sand_grass_tiles = {

            #  basic
            "1-100": pygame.image.load("../resources/tiles/sand_grass/1-100.png").convert_alpha(),
            "01-10": pygame.image.load("../resources/tiles/sand_grass/01-10.png").convert_alpha(),
            "001-1": pygame.image.load("../resources/tiles/sand_grass/001-1.png").convert_alpha(),
            "-1001": pygame.image.load("../resources/tiles/sand_grass/-1001.png").convert_alpha(),
            "10-10": pygame.image.load("../resources/tiles/sand_grass/10-10.png").convert_alpha(),
            "-1010": pygame.image.load("../resources/tiles/sand_grass/-1010.png").convert_alpha(),
            "010-1": pygame.image.load("../resources/tiles/sand_grass/010-1.png").convert_alpha(),
            "0-101": pygame.image.load("../resources/tiles/sand_grass/0-101.png").convert_alpha(),
            "100-1": pygame.image.load("../resources/tiles/sand_grass/100-1.png").convert_alpha(),
            "-1100": pygame.image.load("../resources/tiles/sand_grass/-1100.png").convert_alpha(),
            "0-110": pygame.image.load("../resources/tiles/sand_grass/0-110.png").convert_alpha(),
            "00-11": pygame.image.load("../resources/tiles/sand_grass/00-11.png").convert_alpha(),
            "1-11-1": pygame.image.load("../resources/tiles/sand_grass/1-11-1.png").convert_alpha(),
            "-11-11": pygame.image.load("../resources/tiles/sand_grass/-11-11.png").convert_alpha(),

            # diagonal tiles more grass
            "1-1-11": pygame.image.load("../resources/tiles/sand_grass/1-1-11.png").convert_alpha(),
            "11-1-1": pygame.image.load("../resources/tiles/sand_grass/11-1-1.png").convert_alpha(),
            "-1-111": pygame.image.load("../resources/tiles/sand_grass/-1-111.png").convert_alpha(),
            "-111-1": pygame.image.load("../resources/tiles/sand_grass/-111-1.png").convert_alpha(),

            # diagonal tiles more sand
            "1-1-11S": pygame.image.load("../resources/tiles/sand_grass/1-1-11S.png").convert_alpha(),
            "11-1-1S": pygame.image.load("../resources/tiles/sand_grass/11-1-1S.png").convert_alpha(),
            "-1-111S": pygame.image.load("../resources/tiles/sand_grass/-1-111S.png").convert_alpha(),
            "-111-1S": pygame.image.load("../resources/tiles/sand_grass/-111-1S.png").convert_alpha(),
        }

        return sand_grass_tiles

    def load_grass_tiles(self):

        grass_tiles = {
            # basic
            "0000": pygame.image.load("../resources/tiles/grass/basic/0000.png").convert_alpha(),
            "1-100": pygame.image.load("../resources/tiles/grass/basic/1-100.png").convert_alpha(),
            "01-10": pygame.image.load("../resources/tiles/grass/basic/01-10.png").convert_alpha(),
            "001-1": pygame.image.load("../resources/tiles/grass/basic/001-1.png").convert_alpha(),
            "-1001": pygame.image.load("../resources/tiles/grass/basic/-1001.png").convert_alpha(),
            "10-10": pygame.image.load("../resources/tiles/grass/basic/10-10.png").convert_alpha(),
            "-1010": pygame.image.load("../resources/tiles/grass/basic/-1010.png").convert_alpha(),
            "010-1": pygame.image.load("../resources/tiles/grass/basic/010-1.png").convert_alpha(),
            "0-101": pygame.image.load("../resources/tiles/grass/basic/0-101.png").convert_alpha(),
            "100-1": pygame.image.load("../resources/tiles/grass/basic/100-1.png").convert_alpha(),
            "-1100": pygame.image.load("../resources/tiles/grass/basic/-1100.png").convert_alpha(),
            "0-110": pygame.image.load("../resources/tiles/grass/basic/0-110.png").convert_alpha(),
            "00-11": pygame.image.load("../resources/tiles/grass/basic/00-11.png").convert_alpha(),
            "1-11-1": pygame.image.load("../resources/tiles/grass/basic/1-11-1.png").convert_alpha(),
            "-11-11": pygame.image.load("../resources/tiles/grass/basic/-11-11.png").convert_alpha(),
            "11-1-1": pygame.image.load("../resources/tiles/grass/basic/11-1-1.png").convert_alpha(),
            "1-1-11": pygame.image.load("../resources/tiles/grass/basic/1-1-11.png").convert_alpha(),
            "-1-111": pygame.image.load("../resources/tiles/grass/basic/-1-111.png").convert_alpha(),
            "-111-1": pygame.image.load("../resources/tiles/grass/basic/-111-1.png").convert_alpha(),

            # variation a
            "0000a": pygame.image.load("../resources/tiles/grass/a/0000.png").convert_alpha(),
            "1-100a": pygame.image.load("../resources/tiles/grass/a/1-100.png").convert_alpha(),
            "01-10a": pygame.image.load("../resources/tiles/grass/a/01-10.png").convert_alpha(),
            "001-1a": pygame.image.load("../resources/tiles/grass/a/001-1.png").convert_alpha(),
            "-1001a": pygame.image.load("../resources/tiles/grass/a/-1001.png").convert_alpha(),
            "10-10a": pygame.image.load("../resources/tiles/grass/a/10-10.png").convert_alpha(),
            "-1010a": pygame.image.load("../resources/tiles/grass/a/-1010.png").convert_alpha(),
            "010-1a": pygame.image.load("../resources/tiles/grass/a/010-1.png").convert_alpha(),
            "0-101a": pygame.image.load("../resources/tiles/grass/a/0-101.png").convert_alpha(),
            "100-1a": pygame.image.load("../resources/tiles/grass/a/100-1.png").convert_alpha(),
            "-1100a": pygame.image.load("../resources/tiles/grass/a/-1100.png").convert_alpha(),
            "0-110a": pygame.image.load("../resources/tiles/grass/a/0-110.png").convert_alpha(),
            "00-11a": pygame.image.load("../resources/tiles/grass/a/00-11.png").convert_alpha(),
            "1-11-1a": pygame.image.load("../resources/tiles/grass/a/1-11-1.png").convert_alpha(),
            "-11-11a": pygame.image.load("../resources/tiles/grass/a/-11-11.png").convert_alpha(),
            "11-1-1a": pygame.image.load("../resources/tiles/grass/a/11-1-1.png").convert_alpha(),
            "1-1-11a": pygame.image.load("../resources/tiles/grass/a/1-1-11.png").convert_alpha(),
            "-1-111a": pygame.image.load("../resources/tiles/grass/a/-1-111.png").convert_alpha(),
            "-111-1a": pygame.image.load("../resources/tiles/grass/a/-111-1.png").convert_alpha(),

            # variation b
            "0000b": pygame.image.load("../resources/tiles/grass/b/0000.png").convert_alpha(),

            # variation c
            "0000c": pygame.image.load("../resources/tiles/grass/c/0000.png").convert_alpha(),
        }
        return grass_tiles

    # colored edge tiles to check tile borders
    def load_highlight_tiles(self):
        highlight_tiles = {
            "0000": pygame.image.load("../resources/tiles/border_cheat/0000.png").convert_alpha(),
            "1-100": pygame.image.load("../resources/tiles/border_cheat/1-100.png").convert_alpha(),
            "01-10": pygame.image.load("../resources/tiles/border_cheat/01-10.png").convert_alpha(),
            "001-1": pygame.image.load("../resources/tiles/border_cheat/001-1.png").convert_alpha(),
            "-1001": pygame.image.load("../resources/tiles/border_cheat/-1001.png").convert_alpha(),
            "10-10": pygame.image.load("../resources/tiles/border_cheat/10-10.png").convert_alpha(),
            "-1010": pygame.image.load("../resources/tiles/border_cheat/-1010.png").convert_alpha(),
            "010-1": pygame.image.load("../resources/tiles/border_cheat/010-1.png").convert_alpha(),
            "0-101": pygame.image.load("../resources/tiles/border_cheat/0-101.png").convert_alpha(),
            "100-1": pygame.image.load("../resources/tiles/border_cheat/100-1.png").convert_alpha(),
            "-1100": pygame.image.load("../resources/tiles/border_cheat/-1100.png").convert_alpha(),
            "0-110": pygame.image.load("../resources/tiles/border_cheat/0-110.png").convert_alpha(),
            "00-11": pygame.image.load("../resources/tiles/border_cheat/00-11.png").convert_alpha(),
            "1-11-1": pygame.image.load("../resources/tiles/border_cheat/1-11-1.png").convert_alpha(),
            "-11-11": pygame.image.load("../resources/tiles/border_cheat/-11-11.png").convert_alpha(),
            "11-1-1": pygame.image.load("../resources/tiles/border_cheat/11-1-1.png").convert_alpha(),
            "1-1-11": pygame.image.load("../resources/tiles/border_cheat/1-1-11.png").convert_alpha(),
            "-1-111": pygame.image.load("../resources/tiles/border_cheat/-1-111.png").convert_alpha(),
            "-111-1": pygame.image.load("../resources/tiles/border_cheat/-111-1.png").convert_alpha(),
        }
        return highlight_tiles

    # vegetation

    def load_plants(self):
        # plants
        plants = {
            "bush": pygame.image.load("../resources/plants/bush.png").convert_alpha(),
            "palm1": pygame.image.load("../resources/plants/palm1.png").convert_alpha(),
            "palm2": pygame.image.load("../resources/plants/palm2.png").convert_alpha(),
            "palm3": pygame.image.load("../resources/plants/palm3.png").convert_alpha(),
            "palm4": pygame.image.load("../resources/plants/palm4.png").convert_alpha(),
            "palm5": pygame.image.load("../resources/plants/palm5.png").convert_alpha(),
            "palm6": pygame.image.load("../resources/plants/palm6.png").convert_alpha(),
            "palm7": pygame.image.load("../resources/plants/palm7.png").convert_alpha(),
            "palm8": pygame.image.load("../resources/plants/palm8.png").convert_alpha(),
            "palm9": pygame.image.load("../resources/plants/palm9.png").convert_alpha(),
        }
        return plants
