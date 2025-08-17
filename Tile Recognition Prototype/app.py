import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RED =

OFFSET_X = 5
OFFSET_Y = 1

MAP_WIDTH = 14
MAP_HEIGHT = 10

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
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
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
            # terrain_level = height_map[y][x]
            # world_y -= 9 * terrain_level
            screen.blit(highlight_sprite, (world_x, world_y))


def render_highlight(tile_x, tile_y, screen):
    screen_x, screen_y = tile_to_world(tile_x, tile_y)
    screen.blit(grass_sprite, (screen_x, screen_y))


def check_borders(cell_offset_x, cell_offset_y):
    color = border_sprite.get_at((cell_offset_x, cell_offset_y))
    if color[:3] == (0, 23, 255):
        return -1, 0
    elif color[:3] == (255, 0, 0):
        return 0, -1
    elif color[:3] == (255, 255, 0):
        return 1, 0
    elif color[:3] == (15, 255, 0):
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

    cell_x = screen_x // TILE_WIDTH
    cell_y = screen_y // TILE_HEIGHT
    # pygame.draw.rect(screen, RED, (cell_x * TILE_WIDTH, cell_y * TILE_HEIGHT, 62, 32), 1)

    tile_x = (cell_y - OFFSET_Y) + (cell_x - OFFSET_X)
    tile_y = (cell_y - OFFSET_Y) - (cell_x - OFFSET_X)

    tile_offset_x = screen_x % TILE_WIDTH
    tile_offset_y = screen_y % TILE_HEIGHT

    correction = check_borders(tile_offset_x, tile_offset_y)
    tile_x += correction[0]
    tile_y += correction[1]

    render_highlight(tile_x, tile_y, screen)

    # print(tile_x, tile_y)
    # update display
    pygame.display.update()

pygame.quit()
