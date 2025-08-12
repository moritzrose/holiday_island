# This class provides methods to load all tiles, instead of having huge maps inside other classes
import pygame

# terrain

def load_water_tiles():
    water_tiles = {
        "0000": {"sprite": pygame.image.load("../resources/tiles/water/0000.png").convert_alpha()},
        "1-100": {"sprite": pygame.image.load("../resources/tiles/water/1-100.png").convert_alpha()},
        "01-10": {"sprite": pygame.image.load("../resources/tiles/water/01-10.png").convert_alpha()},
        "001-1": {"sprite": pygame.image.load("../resources/tiles/water/001-1.png").convert_alpha()},
        "-1001": {"sprite": pygame.image.load("../resources/tiles/water/-1001.png").convert_alpha()},
        "10-10": {"sprite": pygame.image.load("../resources/tiles/water/10-10.png").convert_alpha()},
        "-1010": {"sprite": pygame.image.load("../resources/tiles/water/-1010.png").convert_alpha()},
        "010-1": {"sprite": pygame.image.load("../resources/tiles/water/010-1.png").convert_alpha()},
        "0-101": {"sprite": pygame.image.load("../resources/tiles/water/0-101.png").convert_alpha()},
        "100-1": {"sprite": pygame.image.load("../resources/tiles/water/100-1.png").convert_alpha()},
        "-1100": {"sprite": pygame.image.load("../resources/tiles/water/-1100.png").convert_alpha()},
        "0-110": {"sprite": pygame.image.load("../resources/tiles/water/0-110.png").convert_alpha()},
        "00-11": {"sprite": pygame.image.load("../resources/tiles/water/00-11.png").convert_alpha()},
        "1-11-1": {"sprite": pygame.image.load("../resources/tiles/water/1-11-1.png").convert_alpha()},
        "-11-11": {"sprite": pygame.image.load("../resources/tiles/water/-11-11.png").convert_alpha()},
        "11-1-1": {"sprite": pygame.image.load("../resources/tiles/water/11-1-1.png").convert_alpha()},
        "1-1-11": {"sprite": pygame.image.load("../resources/tiles/water/1-1-11.png").convert_alpha()},
        "-1-111": {"sprite": pygame.image.load("../resources/tiles/water/-1-111.png").convert_alpha()},
        "-111-1": {"sprite": pygame.image.load("../resources/tiles/water/-111-1.png").convert_alpha()},
    }
    return water_tiles

def load_sand_tiles():

    sand_tiles = {

        # basic tiles
        "0000": {"sprite": pygame.image.load("../resources/tiles/sand/basic/0000.png").convert_alpha()},
        "1-100": {"sprite": pygame.image.load("../resources/tiles/sand/basic/1-100.png").convert_alpha()},
        "01-10": {"sprite": pygame.image.load("../resources/tiles/sand/basic/01-10.png").convert_alpha()},
        "001-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/001-1.png").convert_alpha()},
        "-1001": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-1001.png").convert_alpha()},
        "10-10": {"sprite": pygame.image.load("../resources/tiles/sand/basic/10-10.png").convert_alpha()},
        "-1010": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-1010.png").convert_alpha()},
        "010-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/010-1.png").convert_alpha()},
        "0-101": {"sprite": pygame.image.load("../resources/tiles/sand/basic/0-101.png").convert_alpha()},
        "100-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/100-1.png").convert_alpha()},
        "-1100": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-1100.png").convert_alpha()},
        "0-110": {"sprite": pygame.image.load("../resources/tiles/sand/basic/0-110.png").convert_alpha()},
        "00-11": {"sprite": pygame.image.load("../resources/tiles/sand/basic/00-11.png").convert_alpha()},
        "1-11-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/1-11-1.png").convert_alpha()},
        "-11-11": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-11-11.png").convert_alpha()},
        "11-1-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/11-1-1.png").convert_alpha()},
        "1-1-11": {"sprite": pygame.image.load("../resources/tiles/sand/basic/1-1-11.png").convert_alpha()},
        "-1-111": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-1-111.png").convert_alpha()},
        "-111-1": {"sprite": pygame.image.load("../resources/tiles/sand/basic/-111-1.png").convert_alpha()},

        # variation a
        "0000a": {"sprite": pygame.image.load("../resources/tiles/sand/a/0000.png").convert_alpha()},
        "1-100a": {"sprite": pygame.image.load("../resources/tiles/sand/a/1-100.png").convert_alpha()},
        "01-10a": {"sprite": pygame.image.load("../resources/tiles/sand/a/01-10.png").convert_alpha()},
        "001-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/001-1.png").convert_alpha()},
        "-1001a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-1001.png").convert_alpha()},
        "10-10a": {"sprite": pygame.image.load("../resources/tiles/sand/a/10-10.png").convert_alpha()},
        "-1010a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-1010.png").convert_alpha()},
        "010-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/010-1.png").convert_alpha()},
        "0-101a": {"sprite": pygame.image.load("../resources/tiles/sand/a/0-101.png").convert_alpha()},
        "100-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/100-1.png").convert_alpha()},
        "-1100a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-1100.png").convert_alpha()},
        "0-110a": {"sprite": pygame.image.load("../resources/tiles/sand/a/0-110.png").convert_alpha()},
        "00-11a": {"sprite": pygame.image.load("../resources/tiles/sand/a/00-11.png").convert_alpha()},
        "1-11-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/1-11-1.png").convert_alpha()},
        "-11-11a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-11-11.png").convert_alpha()},
        "11-1-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/11-1-1.png").convert_alpha()},
        "1-1-11a": {"sprite": pygame.image.load("../resources/tiles/sand/a/1-1-11.png").convert_alpha()},
        "-1-111a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-1-111.png").convert_alpha()},
        "-111-1a": {"sprite": pygame.image.load("../resources/tiles/sand/a/-111-1.png").convert_alpha()},

        # variation b
        "0000b": {"sprite": pygame.image.load("../resources/tiles/sand/b/0000.png").convert_alpha()},

        # variation c
        "0000c": {"sprite": pygame.image.load("../resources/tiles/sand/c/0000.png").convert_alpha()},
    }
    return sand_tiles

def load_sand_grass_tiles():

    sand_grass_tiles = {

        #  basic
        "1-100": {"sprite": pygame.image.load("../resources/tiles/sand_grass/1-100.png").convert_alpha()},
        "01-10": {"sprite": pygame.image.load("../resources/tiles/sand_grass/01-10.png").convert_alpha()},
        "001-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/001-1.png").convert_alpha()},
        "-1001": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-1001.png").convert_alpha()},
        "10-10": {"sprite": pygame.image.load("../resources/tiles/sand_grass/10-10.png").convert_alpha()},
        "-1010": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-1010.png").convert_alpha()},
        "010-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/010-1.png").convert_alpha()},
        "0-101": {"sprite": pygame.image.load("../resources/tiles/sand_grass/0-101.png").convert_alpha()},
        "100-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/100-1.png").convert_alpha()},
        "-1100": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-1100.png").convert_alpha()},
        "0-110": {"sprite": pygame.image.load("../resources/tiles/sand_grass/0-110.png").convert_alpha()},
        "00-11": {"sprite": pygame.image.load("../resources/tiles/sand_grass/00-11.png").convert_alpha()},
        "1-11-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/1-11-1.png").convert_alpha()},
        "-11-11": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-11-11.png").convert_alpha()},

        # diagonal tiles more grass
        "1-1-11": {"sprite": pygame.image.load("../resources/tiles/sand_grass/1-1-11.png").convert_alpha()},
        "11-1-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/11-1-1.png").convert_alpha()},
        "-1-111": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-1-111.png").convert_alpha()},
        "-111-1": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-111-1.png").convert_alpha()},

        # diagonal tiles more sand
        "1-1-11S": {"sprite": pygame.image.load("../resources/tiles/sand_grass/1-1-11S.png").convert_alpha()},
        "11-1-1S": {"sprite": pygame.image.load("../resources/tiles/sand_grass/11-1-1S.png").convert_alpha()},
        "-1-111S": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-1-111S.png").convert_alpha()},
        "-111-1S": {"sprite": pygame.image.load("../resources/tiles/sand_grass/-111-1S.png").convert_alpha()},
    }

    return sand_grass_tiles

def load_grass_tiles():

    grass_tiles = {
        # basic
        "0000": {"sprite": pygame.image.load("../resources/tiles/grass/basic/0000.png").convert_alpha()},
        "1-100": {"sprite": pygame.image.load("../resources/tiles/grass/basic/1-100.png").convert_alpha()},
        "01-10": {"sprite": pygame.image.load("../resources/tiles/grass/basic/01-10.png").convert_alpha()},
        "001-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/001-1.png").convert_alpha()},
        "-1001": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-1001.png").convert_alpha()},
        "10-10": {"sprite": pygame.image.load("../resources/tiles/grass/basic/10-10.png").convert_alpha()},
        "-1010": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-1010.png").convert_alpha()},
        "010-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/010-1.png").convert_alpha()},
        "0-101": {"sprite": pygame.image.load("../resources/tiles/grass/basic/0-101.png").convert_alpha()},
        "100-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/100-1.png").convert_alpha()},
        "-1100": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-1100.png").convert_alpha()},
        "0-110": {"sprite": pygame.image.load("../resources/tiles/grass/basic/0-110.png").convert_alpha()},
        "00-11": {"sprite": pygame.image.load("../resources/tiles/grass/basic/00-11.png").convert_alpha()},
        "1-11-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/1-11-1.png").convert_alpha()},
        "-11-11": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-11-11.png").convert_alpha()},
        "11-1-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/11-1-1.png").convert_alpha()},
        "1-1-11": {"sprite": pygame.image.load("../resources/tiles/grass/basic/1-1-11.png").convert_alpha()},
        "-1-111": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-1-111.png").convert_alpha()},
        "-111-1": {"sprite": pygame.image.load("../resources/tiles/grass/basic/-111-1.png").convert_alpha()},

        # variation a
        "0000a": {"sprite": pygame.image.load("../resources/tiles/grass/a/0000.png").convert_alpha()},
        "1-100a": {"sprite": pygame.image.load("../resources/tiles/grass/a/1-100.png").convert_alpha()},
        "01-10a": {"sprite": pygame.image.load("../resources/tiles/grass/a/01-10.png").convert_alpha()},
        "001-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/001-1.png").convert_alpha()},
        "-1001a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-1001.png").convert_alpha()},
        "10-10a": {"sprite": pygame.image.load("../resources/tiles/grass/a/10-10.png").convert_alpha()},
        "-1010a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-1010.png").convert_alpha()},
        "010-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/010-1.png").convert_alpha()},
        "0-101a": {"sprite": pygame.image.load("../resources/tiles/grass/a/0-101.png").convert_alpha()},
        "100-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/100-1.png").convert_alpha()},
        "-1100a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-1100.png").convert_alpha()},
        "0-110a": {"sprite": pygame.image.load("../resources/tiles/grass/a/0-110.png").convert_alpha()},
        "00-11a": {"sprite": pygame.image.load("../resources/tiles/grass/a/00-11.png").convert_alpha()},
        "1-11-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/1-11-1.png").convert_alpha()},
        "-11-11a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-11-11.png").convert_alpha()},
        "11-1-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/11-1-1.png").convert_alpha()},
        "1-1-11a": {"sprite": pygame.image.load("../resources/tiles/grass/a/1-1-11.png").convert_alpha()},
        "-1-111a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-1-111.png").convert_alpha()},
        "-111-1a": {"sprite": pygame.image.load("../resources/tiles/grass/a/-111-1.png").convert_alpha()},

        # variation b
        "0000b": {"sprite": pygame.image.load("../resources/tiles/grass/b/0000.png").convert_alpha()},

        # variation c
        "0000c": {"sprite": pygame.image.load("../resources/tiles/grass/c/0000.png").convert_alpha()},
    }
    return grass_tiles

# vegetation

def load_plants():
    # plants
    plants = {
        "bush": {"sprite": pygame.image.load("../resources/plants/bush.png").convert_alpha()},
        "palm1": {"sprite": pygame.image.load("../resources/plants/palm1.png").convert_alpha()},
        "palm2": {"sprite": pygame.image.load("../resources/plants/palm2.png").convert_alpha()},
        "palm3": {"sprite": pygame.image.load("../resources/plants/palm3.png").convert_alpha()},
        "palm4": {"sprite": pygame.image.load("../resources/plants/palm4.png").convert_alpha()},
        "palm5": {"sprite": pygame.image.load("../resources/plants/palm5.png").convert_alpha()},
        "palm6": {"sprite": pygame.image.load("../resources/plants/palm6.png").convert_alpha()},
        "palm7": {"sprite": pygame.image.load("../resources/plants/palm7.png").convert_alpha()},
        "palm8": {"sprite": pygame.image.load("../resources/plants/palm8.png").convert_alpha()},
        "palm9": {"sprite": pygame.image.load("../resources/plants/palm9.png").convert_alpha()},
    }
    return plants