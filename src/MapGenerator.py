from collections import Counter

import pygame
import random


# Initialize pygame
pygame.init()

# Configuration
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
BG = (50, 50, 50)
REFERENCE_TILE_DIMENSION = 62, 32
TILES_DEBUG = False
OFFSET_X = 0
OFFSET_Y = 0

# Game
MORE_GRASS_SUFFIX = "G"
MORE_SAND_SUFFIX = "S"


# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheet-Test")

tile_definitions_water = {
    "0000": { "sprite" :pygame.image.load("../resources/tiles/water/0000.png").convert_alpha()},
    "1-100": { "sprite" :pygame.image.load("../resources/tiles/water/1-100.png").convert_alpha()},
    "01-10": { "sprite" :pygame.image.load("../resources/tiles/water/01-10.png").convert_alpha()},
    "001-1": { "sprite" :pygame.image.load("../resources/tiles/water/001-1.png").convert_alpha()},
    "-1001": { "sprite" :pygame.image.load("../resources/tiles/water/-1001.png").convert_alpha()},
    "10-10": { "sprite" :pygame.image.load("../resources/tiles/water/10-10.png").convert_alpha()},
    "-1010": { "sprite" :pygame.image.load("../resources/tiles/water/-1010.png").convert_alpha()},
    "010-1": { "sprite" :pygame.image.load("../resources/tiles/water/010-1.png").convert_alpha()},
    "0-101": { "sprite" :pygame.image.load("../resources/tiles/water/0-101.png").convert_alpha()},
    "100-1": { "sprite" :pygame.image.load("../resources/tiles/water/100-1.png").convert_alpha()},
    "-1100": { "sprite" :pygame.image.load("../resources/tiles/water/-1100.png").convert_alpha()},
    "0-110": { "sprite" :pygame.image.load("../resources/tiles/water/0-110.png").convert_alpha()},
    "00-11": { "sprite" :pygame.image.load("../resources/tiles/water/00-11.png").convert_alpha()},
    "1-11-1": { "sprite" :pygame.image.load("../resources/tiles/water/1-11-1.png").convert_alpha()},
    "-11-11": { "sprite" :pygame.image.load("../resources/tiles/water/-11-11.png").convert_alpha()},
    "11-1-1": { "sprite" :pygame.image.load("../resources/tiles/water/11-1-1.png").convert_alpha()},
    "1-1-11": { "sprite" :pygame.image.load("../resources/tiles/water/1-1-11.png").convert_alpha()},
    "-1-111": { "sprite" :pygame.image.load("../resources/tiles/water/-1-111.png").convert_alpha()},
    "-111-1": { "sprite" :pygame.image.load("../resources/tiles/water/-111-1.png").convert_alpha()},
}

tile_definitions_sand = {
    "0000": { "sprite" :pygame.image.load("../resources/tiles/sand/0000.png").convert_alpha()},
    "1-100": { "sprite" :pygame.image.load("../resources/tiles/sand/1-100.png").convert_alpha()},
    "01-10": { "sprite" :pygame.image.load("../resources/tiles/sand/01-10.png").convert_alpha()},
    "001-1": { "sprite" :pygame.image.load("../resources/tiles/sand/001-1.png").convert_alpha()},
    "-1001": { "sprite" :pygame.image.load("../resources/tiles/sand/-1001.png").convert_alpha()},
    "10-10": { "sprite" :pygame.image.load("../resources/tiles/sand/10-10.png").convert_alpha()},
    "-1010": { "sprite" :pygame.image.load("../resources/tiles/sand/-1010.png").convert_alpha()},
    "010-1": { "sprite" :pygame.image.load("../resources/tiles/sand/010-1.png").convert_alpha()},
    "0-101": { "sprite" :pygame.image.load("../resources/tiles/sand/0-101.png").convert_alpha()},
    "100-1": { "sprite" :pygame.image.load("../resources/tiles/sand/100-1.png").convert_alpha()},
    "-1100": { "sprite" :pygame.image.load("../resources/tiles/sand/-1100.png").convert_alpha()},
    "0-110": { "sprite" :pygame.image.load("../resources/tiles/sand/0-110.png").convert_alpha()},
    "00-11": { "sprite" :pygame.image.load("../resources/tiles/sand/00-11.png").convert_alpha()},
    "1-11-1": { "sprite" :pygame.image.load("../resources/tiles/sand/1-11-1.png").convert_alpha()},
    "-11-11": { "sprite" :pygame.image.load("../resources/tiles/sand/-11-11.png").convert_alpha()},
    "11-1-1": { "sprite" :pygame.image.load("../resources/tiles/sand/11-1-1.png").convert_alpha()},
    "1-1-11": { "sprite" :pygame.image.load("../resources/tiles/sand/1-1-11.png").convert_alpha()},
    "-1-111": { "sprite" :pygame.image.load("../resources/tiles/sand/-1-111.png").convert_alpha()},
    "-111-1": { "sprite" :pygame.image.load("../resources/tiles/sand/-111-1.png").convert_alpha()},
}

tile_definitions_sand_grass= {
    "0000": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/0000.png").convert_alpha()},
    "1-100": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/1-100.png").convert_alpha()},
    "01-10": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/01-10.png").convert_alpha()},
    "001-1": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/001-1.png").convert_alpha()},
    "-1001": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/-1001.png").convert_alpha()},
    "10-10": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/10-10.png").convert_alpha()},
    "-1010": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/-1010.png").convert_alpha()},
    "010-1": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/010-1.png").convert_alpha()},
    "0-101": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/0-101.png").convert_alpha()},
    "100-1": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/100-1.png").convert_alpha()},
    "-1100": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/-1100.png").convert_alpha()},
    "0-110": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/0-110.png").convert_alpha()},
    "00-11": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/00-11.png").convert_alpha()},
    "1-11-1": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/1-11-1.png").convert_alpha()},
    "-11-11": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/-11-11.png").convert_alpha()},
    "11-1-1": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/11-1-1.png").convert_alpha()},
    "1-1-11": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/1-1-11.png").convert_alpha()},
    "-1-111": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/-1-111.png").convert_alpha()},
    "-111-1": { "sprite" :pygame.image.load("../resources/tiles/sand_grass/-111-1.png").convert_alpha()},
}
tile_definitions_grass = {
    "0000": { "sprite" :pygame.image.load("../resources/tiles/grass/0000.png").convert_alpha()},
    "1-100": { "sprite" :pygame.image.load("../resources/tiles/grass/1-100.png").convert_alpha()},
    "01-10": { "sprite" :pygame.image.load("../resources/tiles/grass/01-10.png").convert_alpha()},
    "001-1": { "sprite" :pygame.image.load("../resources/tiles/grass/001-1.png").convert_alpha()},
    "-1001": { "sprite" :pygame.image.load("../resources/tiles/grass/-1001.png").convert_alpha()},
    "10-10": { "sprite" :pygame.image.load("../resources/tiles/grass/10-10.png").convert_alpha()},
    "-1010": { "sprite" :pygame.image.load("../resources/tiles/grass/-1010.png").convert_alpha()},
    "010-1": { "sprite" :pygame.image.load("../resources/tiles/grass/010-1.png").convert_alpha()},
    "0-101": { "sprite" :pygame.image.load("../resources/tiles/grass/0-101.png").convert_alpha()},
    "100-1": { "sprite" :pygame.image.load("../resources/tiles/grass/100-1.png").convert_alpha()},
    "-1100": { "sprite" :pygame.image.load("../resources/tiles/grass/-1100.png").convert_alpha()},
    "0-110": { "sprite" :pygame.image.load("../resources/tiles/grass/0-110.png").convert_alpha()},
    "00-11": { "sprite" :pygame.image.load("../resources/tiles/grass/00-11.png").convert_alpha()},
    "1-11-1": { "sprite" :pygame.image.load("../resources/tiles/grass/1-11-1.png").convert_alpha()},
    "-11-11": { "sprite" :pygame.image.load("../resources/tiles/grass/-11-11.png").convert_alpha()},
    "11-1-1": { "sprite" :pygame.image.load("../resources/tiles/grass/11-1-1.png").convert_alpha()},
    "1-1-11": { "sprite" :pygame.image.load("../resources/tiles/grass/1-1-11.png").convert_alpha()},
    "-1-111": { "sprite" :pygame.image.load("../resources/tiles/grass/-1-111.png").convert_alpha()},
    "-111-1": { "sprite" :pygame.image.load("../resources/tiles/grass/-111-1.png").convert_alpha()},
}

# height_map = [
#     [ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ],
#     [ 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2 ],
#     [ 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 3, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 0, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 1, 1, 2, 2, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 0, 1, 1, 1, 2, 2, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 2, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 1, 2, 2, 1, 0, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 3, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 0, 1, 2, 3, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 0, 0, 1, 1, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 2, 2, 2, 3, 3, 2, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 2, 2, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 3, 2, 1, 0, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 0, 0, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 1, 1, 1, 0, 1, 1, 2, 2, 1, 1, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 3, 3, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 3, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 0, 0, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 3, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 1, 1, 2, 2, 1, 0, 0, 1, 1, 2, 1, 0, 1, 1, 1, 0, 1, 1, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0, 0, 0, 1, 1, 2, 2, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2 ],
#     [ 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2 ],
#     [ 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2 ],
#     [ 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2 ],
#     [ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ],]

height_map = [
    [0,0,0,1,1,2,2,3,3,4,4,5,5,4,4,4,3,3,2,2,2,2,1,1,0,0,0],
    [0,0,1,2,2,3,3,4,4,5,5,5,5,4,3,3,3,2,1,1,2,2,1,1,0,1,1],
    [0,0,0,1,1,2,2,3,3,4,4,5,5,4,4,4,3,3,2,2,2,2,1,1,0,0,0],
    [0,0,1,2,2,3,3,4,4,5,5,5,5,4,3,3,3,2,1,1,2,2,1,1,0,1,1]
]

def grid_to_screen(grid_x, grid_y, tile_dimensions, terrain_level):
    width, height = tile_dimensions
    screen_x = 0.5 * (grid_x - grid_y) * width
    screen_y = 0.5 * (grid_x + grid_y) * height - terrain_level * 9
    return screen_x, screen_y

def get_tile (x, y):

    # determine surrounding height values
    tl = height_map[y+1][x]
    tr = height_map[y][x]
    br = height_map[y][x+1]
    bl = height_map[y+1][x+1]

    height_values = [tl, tr, br, bl]
    min_height = min(height_values)
    max_height = max(height_values)

    tile_id = str(tr-tl) + str(br-tr) + str(bl-br) + str(tl-bl)

    # if there is any water, return water tile
    if min_height == 0:
        return tile_definitions_water.get(tile_id)

    # if there is only sand, return sand tile
    elif max_height == 2:
        return tile_definitions_sand.get(tile_id)

    # if there is sand and grass, return sand grass tile
    elif min_height <= 2 < max_height:
        # if it is a diagonal tile, determine variation
        if abs(max_height - min_height) > 1:
            dominant_height = Counter(height_values)
            # if there is more sand than grass, append suffix
            if max(dominant_height) < 3:
                tile_id = tile_id + MORE_SAND_SUFFIX

        return tile_definitions_sand_grass.get(tile_id)

    # return grass tile
    else:
        return tile_definitions_grass.get(tile_id)


running = True

while running:

    # update background
    screen.fill(BG)

    # Map zeichnen
    for y in range(len(height_map) - 1):
        for x in range(len(height_map[y]) - 1):
            tile = get_tile(x,y)
            terrain_level = height_map[y][x]
            if tile:
                image = tile.get("sprite")
                screen_x, screen_y = grid_to_screen(x, y, REFERENCE_TILE_DIMENSION, terrain_level)
                screen_x += OFFSET_X
                screen_y += OFFSET_Y
                screen.blit(image, (screen_x, screen_y))

                if (TILES_DEBUG):
                    rect = pygame.Rect(screen_x, screen_y, * image.get_size())
                    pygame.draw.rect(screen, (255, 0, 0), rect, 1)  # roter Rand, 1 Pixel dick

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


pygame.quit()
