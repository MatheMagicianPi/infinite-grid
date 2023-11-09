import copy
import pygame
import sys
import random
from collections import Counter
import time

# Constants
CELL_SIZE = 10; GRID_HEIGHT = 30; GRID_WIDTH = 2 * GRID_HEIGHT
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT

DISPLAY = True
SAMPLE_SIZE = 0

NEIGHBORHOOD_RADIUS = 1

COUNTDOWN = 0
STRENGTH_IN_NUMBERS = 10

# REBELLION_PROBABILITY = -1
# REBELLION_SUCCESS_RATE = 0.5

# Colors
BLACK = (0, 0, 0)
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
    0: BLACK,
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
winning_teams = Counter()
rounds_played = 1

def initial_state(row, col):
    return random.randint(1, 19)
    # return random.choices((5, 7, 9), [1/3, 1/3, 1/3], k=1)[0]
    # if col < GRID_WIDTH / 3:
    #     return 5
    # if GRID_WIDTH / 3 <= col <= 2 * GRID_WIDTH / 3:
    #     return 7
    # if 2 * GRID_WIDTH / 3 < col:
    #     return 9

def choose_next_state(neighbors):
    crowd_bias = random.choice(most_common_elements(neighbors))
    if random.randint(1, (2 * NEIGHBORHOOD_RADIUS + 1)**2 + STRENGTH_IN_NUMBERS) >= (2 * NEIGHBORHOOD_RADIUS + 1)**2 + 1:
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
grid = [[initial_state(row, col) for col in range(GRID_WIDTH)] for row in range(GRID_HEIGHT)]
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
            if cell_color != old_color or first_time or cell_color == BLACK:
                cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, cell_color, cell_rect)

def step():
    global new_grid
    global grid
    colors_remaining.clear()
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            # neighbor domination
            if grid[row][col] == 0:
                new_grid[row][col] = 0
            else:
                neighbors = get_neighbors(row, col)
                n = choose_next_state(neighbors)
                if n != 0:
                    new_grid[row][col] = n
                    colors_remaining.add(n)

def get_neighbors(row, col):
    neighbors = []
    for i in range(row - NEIGHBORHOOD_RADIUS, row + NEIGHBORHOOD_RADIUS + 1):
        for j in range(col - NEIGHBORHOOD_RADIUS, col + NEIGHBORHOOD_RADIUS + 1):
            if i < GRID_HEIGHT and j < GRID_WIDTH:
                if i == GRID_HEIGHT:
                    i = -1
                if j == GRID_WIDTH:
                    j = -1
                if grid[i][j] != 0:
                    neighbors.append(grid[i][j])
    return neighbors

# def rebellion(rebel_color, against_color, success_rate):
#     if rebel_color != against_color:
#         for row in range(GRID_HEIGHT):
#             for col in range(GRID_WIDTH):
#                 if new_grid[row][col] == against_color and random.uniform(0, 1) <= success_rate:
#                     new_grid[row][col] = rebel_color

# def attempt_rebellion():
#     if random.uniform(0, 1) <= REBELLION_PROBABILITY:
#         against_color = random.choice(list(colors_remaining))
#         rebel_color = random.choice(list(COLORS.keys()))
#         while (rebel_color == against_color):
#             rebel_color = random.choice(list(COLORS.keys()))
#         rebellion(rebel_color, against_color, REBELLION_SUCCESS_RATE)

if DISPLAY:
    draw_grid(True)
    pygame.display.flip()
running = True
mouse_pressed = False
while running:
    time.sleep(COUNTDOWN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
        elif event.type == pygame.MOUSEMOTION and mouse_pressed:
            # Get the mouse position and convert it to grid coordinates
            mouse_x, mouse_y = event.pos
            col = mouse_x // CELL_SIZE
            row = mouse_y // CELL_SIZE

            # Change the color of the cell at the mouse position
            if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
                grid[row][col] = 0
                new_grid[row][col] = 0
    step()
    # attempt_rebellion()
    if DISPLAY:
        draw_grid(False)
    swap_grids()
    if DISPLAY:
        pygame.display.flip()

    # if len(colors_remaining) == 1 and SAMPLE_SIZE > 0:
    #     grid = [[initial_state(row, col) for col in range(GRID_WIDTH)] for row in range(GRID_HEIGHT)]
    #     new_grid = copy.deepcopy(grid)
    #     if DISPLAY:
    #         draw_grid(True)
    #         pygame.display.flip()
    #     winning_teams.update(tuple(colors_remaining))
    #     print(f"Round {rounds_played} complete")
    #     if rounds_played >= SAMPLE_SIZE:
    #         running = False
    #     rounds_played += 1
    
print(winning_teams)

# Quit Pygame
pygame.quit()
sys.exit()
