import copy
import pygame
import sys
import random
from collections import Counter
import time

# Constants
CELL_SIZE = 100; GRID_WIDTH = 3; GRID_HEIGHT = 3
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT

COUNTDOWN = 0.5
STRENGTH_IN_NUMBERS = 10

REBELLION_PROBABILITY = 0.5
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

def initial_state():
    # return random.randint(1, 19)
    return random.choice((5, 7, 9))

def choose_next_state(neighbors):
    crowd_bias = random.choice(most_common_elements(neighbors))
    if random.randint(1, 9 + STRENGTH_IN_NUMBERS) >= 10:
        return crowd_bias
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
grid = [[initial_state() for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
new_grid = copy.deepcopy(grid)

def swap_grids():
    global grid
    global new_grid
    temp = grid
    grid = new_grid
    new_grid = temp

def draw_grid(first_time):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            cell_color = COLORS[new_grid[row][col]]
            old_color = COLORS[grid[row][col]]
            if cell_color != old_color or first_time:
                cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, cell_color, cell_rect)

def step():
    global new_grid
    colors_remaining.clear()
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
    return neighbors

def rebellion(rebel_color, against_color, success_rate):
    if rebel_color != against_color:
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if new_grid[row][col] == against_color and random.uniform(0, 1) <= success_rate:
                    new_grid[row][col] = rebel_color

def attempt_rebellion():
    if random.uniform(0, 1) <= REBELLION_PROBABILITY:
        against_color = random.choice(list(colors_remaining))
        rebel_color = random.choice(list(COLORS.keys()))
        while (rebel_color == against_color):
            rebel_color = random.choice(list(COLORS.keys()))
        rebellion(rebel_color, against_color, REBELLION_SUCCESS_RATE)

draw_grid(True)
pygame.display.flip()
running = True
while running:
    time.sleep(COUNTDOWN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    step()
    attempt_rebellion()
    draw_grid(False)
    swap_grids()
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()
sys.exit()
