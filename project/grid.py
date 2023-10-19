import pygame
import sys
import random
import time
from collections import Counter

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 20  # Size of each cell in pixels
GRID_WIDTH = 150  # Number of cells in the horizontal direction
GRID_HEIGHT = 150  # Number of cells in the vertical direction
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
ZOOM_FACTOR = 1.2  # Zoom in/out factor
PAN_SPEED = 5

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 218, 40)
PINK = (255, 133, 164)
GREEN = (142, 237, 101)
BLUE = (0, 0, 255)
PURPLE = (186, 85, 211)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
LIME_GREEN = (50, 205, 50)
TURQUOISE = (64, 224, 208)
GOLD = (255, 215, 0)
TEAL = (0, 128, 128)
MAGENTA = (255, 0, 255)
SLATE_GRAY = (112, 128, 144)
OLIVE = (128, 128, 0)

COLORS = {
    -1: BLACK,
    0: WHITE,
    1: YELLOW,
    2: PINK,
    3: GREEN,
    4: BLUE,
    5: PURPLE,
    6: CYAN,
    7: ORANGE,
    8: RED,
    9: LIME_GREEN,
    10: TURQUOISE,
    11: GOLD,
    12: TEAL,
    13: MAGENTA,
    14: SLATE_GRAY,
    15: OLIVE
}


# Create the Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Name of Window")

grid = [[random.randint(1, len(COLORS) - 2) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Initialize zoom and pan variables
zoom = 0.5
pan_x, pan_y = 0, 0

def get_neighbors(row, col):
    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < GRID_WIDTH and 0 <= j < GRID_HEIGHT:
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

    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
                # random rebels
            if random.uniform(0, 1) <= 10**-4:
                new_grid[row][col] = random.randint(1, len(COLORS) - 2)
            else:
                # neighbor domination
                # new_grid[row][col] = random.choice(get_neighbors(row, col))
                neighbors = get_neighbors(row, col)
                n = random.choice(neighbors)
                if n != 0:
                    new_grid[row][col] = n

    grid = new_grid

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

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cell_color = COLORS[grid[y][x]]
            cell_rect = pygame.Rect(
                x * CELL_SIZE * zoom + pan_x, y * CELL_SIZE * zoom + pan_y, CELL_SIZE * zoom, CELL_SIZE * zoom
            )
            pygame.draw.rect(screen, cell_color, cell_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()