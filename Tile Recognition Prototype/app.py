import pygame

GREEN = 15, 255, 0

YELLOW = 255, 255, 0

RED = 255, 0, 0

BLUE = 0, 23, 255

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


OFFSET_X = 3
OFFSET_Y = 3

MAP_WIDTH = 7
MAP_HEIGHT = 7

TILE_WIDTH = 62
TILE_HEIGHT = 32

BG = (50, 50, 50)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tile Recognition Prototype")

grass_sprite = pygame.image.load("0000.png").convert_alpha()
highlight_sprite = pygame.image.load("0000H.png").convert_alpha()
border_sprite = pygame.image.load("0000Border.png").convert_alpha()

height_map = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


def tile_to_world(tile_x, tile_y):
    world_x = (tile_x - tile_y) * TILE_WIDTH / 2
    world_y = (tile_x + tile_y) * TILE_HEIGHT / 2

    world_x += OFFSET_X * TILE_WIDTH
    world_y += OFFSET_Y * TILE_HEIGHT

    return world_x, world_y


def render_map(screen):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            world_x, world_y = tile_to_world(x, y)
            terrain_level = height_map[y][x]
            world_y -= 9 * terrain_level
            screen.blit(highlight_sprite, (world_x, world_y))


def render_highlight(tile_x, tile_y, screen):
    screen_x, screen_y = tile_to_world(tile_x, tile_y)
    screen_y -= height_map[tile_y][tile_x] * 9

    screen.blit(grass_sprite, (screen_x, screen_y))

def world_to_tile(world_x, world_y):

    # assume we are on the highest terrain level (5)
    for terrain_level in range(5, -1, -1):
        tmp_world_y = world_y + terrain_level * 9
        tmp_world_x = world_x

        cell_x = tmp_world_x // TILE_WIDTH
        cell_y = tmp_world_y // TILE_HEIGHT

        tile_x = (cell_y - OFFSET_Y) + (cell_x - OFFSET_X)
        tile_y = (cell_y - OFFSET_Y) - (cell_x - OFFSET_X)

        tile_offset_x = world_x % TILE_WIDTH
        tile_offset_y = world_y % TILE_HEIGHT

        correction = check_borders(tile_offset_x, tile_offset_y)
        tile_x += correction[0]
        tile_y += correction[1]

        if height_map[tile_y][tile_x] == terrain_level:
            print(tile_x,tile_y)
            return tile_x,tile_y

    return 0,0

def check_borders(cell_offset_x, cell_offset_y):
    color = border_sprite.get_at((cell_offset_x, cell_offset_y))
    if color[:3] == (BLUE):
        return -1, 0
    elif color[:3] == (RED):
        return 0, -1
    elif color[:3] == (YELLOW):
        return 1, 0
    elif color[:3] == (GREEN):
        return 0, 1
    else:
        return 0, 0

running = True

while running:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update background
    screen.fill(BG)

    # render map
    render_map(screen)

    # mouse
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    screen_x = pygame.mouse.get_pos()[0]
    screen_y = pygame.mouse.get_pos()[1]

    #cell_x = screen_x // TILE_WIDTH
    #cell_y = screen_y // TILE_HEIGHT
    # pygame.draw.rect(screen, RED, (cell_x * TILE_WIDTH, cell_y * TILE_HEIGHT, 62, 32), 1)

    #tile_x = (cell_y - OFFSET_Y) + (cell_x - OFFSET_X)
    #tile_y = (cell_y - OFFSET_Y) - (cell_x - OFFSET_X)

    #tile_offset_x = screen_x % TILE_WIDTH
    #tile_offset_y = screen_y % TILE_HEIGHT

    #correction = check_borders(tile_offset_x, tile_offset_y)
    #tile_x += correction[0]
    #tile_y += correction[1]

    tile_x, tile_y = world_to_tile(screen_x, screen_y)
    render_highlight(tile_x, tile_y, screen)

    # print(tile_x, tile_y)
    # update display
    pygame.display.update()

pygame.quit()
