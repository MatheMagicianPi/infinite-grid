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

STRENGTH_IN_NUMBERS = 3

REBELLION_PROBABILITY = 0.01
REBELLION_SUCCESS_RATE = 0.5

# Colors
RED = (255, 130, 71)
ORANGE = (255, 182, 83)
YELLOW = (255, 220, 102)
GREEN = (136, 255, 147)
BLUE = (100, 149, 237)
PURPLE = (171, 130, 255)
PINK = (255, 105, 180)
CYAN = (0, 255, 255)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
GOLD = (255, 215, 0)
LAVENDER = (230, 230, 250)
TEAL = (0, 128, 128)
MAGENTA = (255, 0, 255)
MAROON = (128, 0, 0)
TURQUOISE = (64, 224, 208)
INDIGO = (75, 0, 130)
CORAL = (255, 127, 80)
LIME = (0, 255, 0)

COLORS = {
    1: RED,
    2: ORANGE,
    3: YELLOW,
    4: GREEN,
    5: BLUE,
    6: PURPLE,
    7: PINK,
    8: CYAN,
    9: BROWN,
    10: GRAY,
    11: GOLD,
    12: LAVENDER,
    13: TEAL,
    14: MAGENTA,
    15: MAROON,
    16: TURQUOISE,
    17: INDIGO,
    18: CORAL,
    19: LIME
}

colors_remaining = set()

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

def draw_grid(first_time):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            cell_color = COLORS[new_grid[row][col]]
            old_color = COLORS[grid[row][col]]
            if cell_color != old_color or first_time:
                cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, cell_color, cell_rect)

def step(s):
    global grid
    global new_grid
    colors_remaining.clear()
    for _ in range(s):
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                # neighbor domination
                neighbors = get_neighbors(row, col)
                n = choose_next_state(neighbors)
                if n != 0:
                    new_grid[row][col] = n
                    colors_remaining.add(n)

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

def rebellion(rebel_color, against_color, success_rate):
    if rebel_color != against_color:
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if new_grid[row][col] == against_color and random.uniform(0, 1) <= success_rate:
                    new_grid[row][col] = rebel_color

draw_grid(True)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    step(1)
    if random.uniform(0, 1) <= REBELLION_PROBABILITY:
        against_color = random.choice(list(colors_remaining))
        rebel_color = random.choice(list(COLORS.keys()))
        while (rebel_color == against_color):
            rebel_color = random.choice(list(COLORS.keys()))
        rebellion(rebel_color, against_color, REBELLION_SUCCESS_RATE)
    draw_grid(False)
    temp = grid
    grid = new_grid
    new_grid = temp
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
