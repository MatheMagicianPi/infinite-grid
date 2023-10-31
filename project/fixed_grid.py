import copy
import pygame
import sys
import random
from collections import Counter

# Constants
CELL_SIZE = 10
GRID_WIDTH = 120
GRID_HEIGHT = 60
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT

EXCLUDED_COLORS = (-1, -1)
STRENGTH_IN_NUMBERS = 20

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

def choose_next_state(neighbors):
    if len(set(neighbors)) == 1:
        return neighbors[0]
    return random.choice(neighbors)

def most_common_elements(input_list):
    # Use Counter to count element occurrences
    count = Counter(input_list)
    
    # Find the maximum count
    max_count = max(count.values())
    
    # Create a list of elements with the maximum count
    most_common = [item for item, freq in count.items() if freq == max_count]
    
    return most_common

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Create a random grid of 0s and 1s
grid = [[random.randint(1, len(COLORS) - 2) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
new_grid = copy.deepcopy(grid)

def draw_grid():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            cell_color = COLORS[new_grid[row][col]]
            old_color = COLORS[grid[row][col]]
            if True:
                cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, cell_color, cell_rect)

def step(s):
    global grid
    global new_grid
    for _ in range(s):
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if grid[row][col] in EXCLUDED_COLORS:
                    pass
                else:
                    # neighbor domination
                    neighbors = get_neighbors(row, col)
                    n = choose_next_state(neighbors)
                    if n != 0:
                        new_grid[row][col] = n
    temp = grid
    grid = new_grid
    new_grid = temp

def get_neighbors(row, col):
    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < GRID_HEIGHT and 0 <= j < GRID_WIDTH:
                neighbors.append(grid[i][j])
    crowd_bias = random.choice(most_common_elements(neighbors))
    for i in range(STRENGTH_IN_NUMBERS):
        neighbors.append(crowd_bias)
    return neighbors

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    step(1)
    draw_grid()
    pygame.display.flip()
    # grid = copy.deepcopy(new_grid)
    # grid = new_grid

# Quit Pygame
pygame.quit()
sys.exit()
