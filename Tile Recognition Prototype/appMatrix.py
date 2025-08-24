import pygame
import math

from src.asset_manager import load_grass_tiles, load_masks, load_cheat_tiles
from src.utils import calculate_tile_id

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAP_WIDTH = 7
MAP_HEIGHT = 7

TILE_WIDTH = 62
TILE_HEIGHT = 32

OFFSET_X = 5 * TILE_WIDTH
OFFSET_Y = 3 * TILE_HEIGHT

BG = (50, 50, 50)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tile Recognition Prototype")

# tiles
grass_sprites = load_grass_tiles()

# highlight tiles
highlight_sprites = load_cheat_tiles()

# masks
grass_sprite_masks = load_masks(grass_sprites)

height_map = [
    [0, 1, 1, 0, 0, 0, 0],
    [0, 1, 2, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


def mouse_in_tile(mouse_x, mouse_y, screen_x, screen_y, tile_id):
    local_x = mouse_x - screen_x
    local_y = mouse_y - screen_y

    sprite = grass_sprites.get(tile_id).get("sprite")
    sprite_mask = grass_sprite_masks.get(tile_id + "M")

    if 0 <= local_x < sprite.get_width() and 0 <= local_y < sprite.get_height():
        return sprite_mask.get_at((local_x, local_y)) == 1


def grid_to_projection(x, y, z):
    projection_x = (x - y) * TILE_WIDTH * 0.5 + OFFSET_X
    projection_y = (x + y) * TILE_HEIGHT * 0.5 - z * 9 + OFFSET_Y
    return projection_x, projection_y


def projection_to_grid(projection_x, projection_y):
    x_no_offset = projection_x - OFFSET_X
    y_no_offset = projection_y - OFFSET_Y

    normed_x = x_no_offset * 2 / TILE_WIDTH  # u
    normed_y = y_no_offset * 2 / TILE_HEIGHT  # v

    grid_x = math.floor((normed_x + normed_y) / 2)
    grid_y = math.floor((normed_y - normed_x) / 2)

    grid_x = min(len(height_map[0]) - 2, grid_x)
    grid_y = min(len(height_map) - 2, grid_y)

    grid_x = max(0, grid_x)
    grid_y = max(0, grid_y)

    return grid_x, grid_y


def render_map(screen):
    for y in range(len(height_map) - 1):
        for x in range(len(height_map[0]) - 1):
            z = height_map[y][x]

            tl = height_map[y + 1][x]
            tr = height_map[y][x]
            br = height_map[y][x + 1]
            bl = height_map[y + 1][x + 1]
            height_values = [tl, tr, br, bl]
            tile_id = calculate_tile_id(height_values)

            sprite = grass_sprites.get(tile_id).get("sprite")

            projection_x, projection_y = grid_to_projection(x, y, z)
            screen.blit(sprite, (projection_x, projection_y))


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
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    # mouse pos to grid coordinates
    grid_x, grid_y = projection_to_grid(mouse_x, mouse_y)

    print(grid_x, grid_y)

    # grid coordinates to screen coordinates
    screen_x, screen_y = grid_to_projection(grid_x, grid_y, height_map[grid_y][grid_x])

    # calculate tile id to check if cursor is in tile area or in an adjacent tile
    # determine corner height values

    tl = height_map[grid_y + 1][grid_x]
    tr = height_map[grid_y][grid_x]
    br = height_map[grid_y][grid_x + 1]
    bl = height_map[grid_y + 1][grid_x + 1]
    height_values = [tl, tr, br, bl]
    tile_id = calculate_tile_id(height_values)

    tile_found = False

    if mouse_in_tile(mouse_x, mouse_y, screen_x, screen_y, tile_id):
        sprite = highlight_sprites.get(tile_id).get("sprite")
        tile_found = True
        screen.blit(sprite, (screen_x, screen_y))
    else:
        neighbours = [(grid_x - 1, grid_y), (grid_x, grid_y - 1), (grid_x + 1, grid_y), (grid_x, grid_y + 1)]
        for neighbour in neighbours:
            temp_grid_x = neighbour[0]
            temp_grid_y = neighbour[1]

            temp_grid_x = min(len(height_map[0]) - 2, temp_grid_x)
            temp_grid_y = min(len(height_map) - 2, temp_grid_y)

            temp_grid_x = max(0, temp_grid_x)
            temp_grid_y = max(0, temp_grid_y)

            print(temp_grid_x, temp_grid_y)
            screen_x, screen_y = grid_to_projection(temp_grid_x, temp_grid_y, height_map[temp_grid_y][temp_grid_x])

            tl = height_map[temp_grid_y + 1][temp_grid_x]
            tr = height_map[temp_grid_y][temp_grid_x]
            br = height_map[temp_grid_y][temp_grid_x + 1]
            bl = height_map[temp_grid_y + 1][temp_grid_x + 1]
            height_values = [tl, tr, br, bl]
            tile_id = calculate_tile_id(height_values)

            if mouse_in_tile(mouse_x, mouse_y, screen_x, screen_y, tile_id):
                sprite = highlight_sprites.get(tile_id).get("sprite")
                tile_found = True
                screen.blit(sprite, (screen_x, screen_y))
                break
        if not tile_found:
            diagonal_neighbours = [(grid_x - 1, grid_y - 1), (grid_x + 1, grid_y - 1), (grid_x + 1, grid_y + 1),
                                   (grid_x - 1, grid_y + 1)]


            for neighbour in diagonal_neighbours:
                temp_grid_x = neighbour[0]
                temp_grid_y = neighbour[1]

                temp_grid_x = min(len(height_map[0]) - 2, temp_grid_x)
                temp_grid_y = min(len(height_map) - 2, temp_grid_y)

                temp_grid_x = max(0, temp_grid_x)
                temp_grid_y = max(0, temp_grid_y)

                print(temp_grid_x, temp_grid_y)
                screen_x, screen_y = grid_to_projection(temp_grid_x, temp_grid_y, height_map[temp_grid_y][temp_grid_x])

                tl = height_map[temp_grid_y + 1][temp_grid_x]
                tr = height_map[temp_grid_y][temp_grid_x]
                br = height_map[temp_grid_y][temp_grid_x + 1]
                bl = height_map[temp_grid_y + 1][temp_grid_x + 1]
                height_values = [tl, tr, br, bl]
                tile_id = calculate_tile_id(height_values)

                if mouse_in_tile(mouse_x, mouse_y, screen_x, screen_y, tile_id):
                    sprite = highlight_sprites.get(tile_id).get("sprite")
                    tile_found = True
                    screen.blit(sprite, (screen_x, screen_y))
                    break

    # update display
    pygame.display.update()

pygame.quit()
