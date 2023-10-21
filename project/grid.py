import copy
import pygame
import sys
import random
import time
from collections import Counter

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 20  # Size of each cell in pixels
GRID_WIDTH = 50  # Number of cells in the horizontal direction
GRID_HEIGHT = 2 * GRID_WIDTH + 1  # Number of cells in the vertical direction
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
ZOOM_FACTOR = 1.2  # Zoom in/out factor
PAN_SPEED = 5
ROUNDING = None

EXCLUDED_COLORS = (-1, -1)
REBELS_ENABLED = False
REBEL_RATE = 10**-4
COOLDOWN_ENABLED = False
COOLDOWN_STEPS = 50

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 130, 71)
ORANGE = (255, 182, 83)
YELLOW = (255, 220, 102)
GREEN = (136, 255, 147)
BLUE = (100, 149, 237)
PURPLE = (171, 130, 255)

COLORS = {
    -1: BLACK,
    0: WHITE,
    1: RED,
    2: ORANGE,
    3: YELLOW,
    4: GREEN,
    5: BLUE,
    6: PURPLE
}

cells_on_cooldown = dict()
open = False

def random_color():
    return random.randint(1, len(COLORS) - 2)
    # return random.randint(1, 5)

# Create the Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("War")

grid = [[random_color() for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
for i in range(GRID_WIDTH):
    grid[round(GRID_HEIGHT / 2)][i] = -1
new_grid = copy.deepcopy(grid)

# Initialize zoom and pan variables
zoom = 0.5
pan_x, pan_y = 0, 0
steps = 0

def step(s):
    global grid
    global new_grid
    for _ in range(s):
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if grid[row][col] in EXCLUDED_COLORS:
                    pass
                elif COOLDOWN_ENABLED and (row, col) in cells_on_cooldown:
                    cells_on_cooldown[(row, col)] -= 1
                    if cells_on_cooldown[(row, col)] == 0:
                        del cells_on_cooldown[(row, col)]
                    # random rebels
                elif REBELS_ENABLED and random.uniform(0, 1) <= REBEL_RATE:
                    new_grid[row][col] = random_color()
                else:
                    # neighbor domination
                    neighbors = get_neighbors(row, col)
                    n = random.choice(neighbors)
                    old_state = grid[row][col]
                    if n not in EXCLUDED_COLORS and n != 0:
                        new_grid[row][col] = n
                        if n != old_state:
                            cells_on_cooldown[(row, col)] = random.randint(1, COOLDOWN_STEPS)

    grid = new_grid

def get_neighbors(row, col):
    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < GRID_HEIGHT and 0 <= j < GRID_WIDTH:
                neighbors.append(grid[i][j])
    return neighbors

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle zooming with `+` and `-` keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:  # Handle both '+' and 'numpad +'
                zoom *= ZOOM_FACTOR
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:  # Handle both '-' and 'numpad -'
                zoom /= ZOOM_FACTOR
            if event.key == pygame.K_SPACE:
                open = not open
                if open:
                    grid[round(GRID_HEIGHT / 2)][round(GRID_WIDTH / 2)] = 0
                else:
                    for i in range(GRID_WIDTH):
                        grid[round(GRID_HEIGHT / 2)][i] = -1
            if event.key == pygame.K_c:
                COOLDOWN_ENABLED = not COOLDOWN_ENABLED
                cells_on_cooldown.clear()
            if event.key == pygame.K_r:
                REBELS_ENABLED = not REBELS_ENABLED

    # Handle panning with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pan_x += PAN_SPEED / zoom
    if keys[pygame.K_RIGHT]:
        pan_x -= PAN_SPEED / zoom
    if keys[pygame.K_UP]:
        pan_y += PAN_SPEED / zoom
    if keys[pygame.K_DOWN]:
        pan_y -= PAN_SPEED / zoom

    step(1)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cell_color = COLORS[grid[y][x]]
            cell_rect = pygame.Rect(
                round(x * CELL_SIZE * zoom + pan_x, ROUNDING),
                round(y * CELL_SIZE * zoom + pan_y, ROUNDING),
                round(CELL_SIZE * zoom, ROUNDING),
                round(CELL_SIZE * zoom, ROUNDING)
            )
            pygame.draw.rect(screen, cell_color, cell_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()