import copy
import pygame
import sys
import random
from collections import Counter
import time

# Adjustable Settings

CELL_SIZE = 10; GRID_HEIGHT = 6; GRID_WIDTH = 6

DISPLAY_VISUALS = False
SAMPLE_SIZE = 1000

TIME_BETWEEN_STEPS = 0
STRENGTH_IN_NUMBERS = 0

def initial_state_of_cell(row, col):
    # return random.randint(1, 19)
    # return random.choice((9, 10))
    return random.choices((1, 4, 9), [0.9, 0.07, 0.03], k=1)[0]
    # return 10
    # if col < 2:
    #     return 1
    # if 2 <= col < 4:
    #     return 4
    # if 4 <= col:
    #     return 9

def adjust_initial_state_grid():
    global grid
    # grid[0][0] = 0
    # grid[7][3] = 9
    # grid[0][1] = 9

# Only adjust code beyond this point if you know what you are doing

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

WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT

grid = None
new_grid = None

colors_remaining = set()
winning_teams = Counter()
round_lengths = []
rounds_played = 0
steps_this_round = 0

fpst_start = None
fpst_end = None
five_percent_sampling_time = None

def report_results():
    print(winning_teams)

def create_grid():
    global grid, new_grid
    grid = [[initial_state_of_cell(row, col) for col in range(GRID_WIDTH)] for row in range(GRID_HEIGHT)]
    adjust_initial_state_grid()
    new_grid = copy.deepcopy(grid)

def choose_next_state(neighbors):
    crowd_bias = random.choice(most_common_elements(neighbors))
    if random.randint(1, 9 + STRENGTH_IN_NUMBERS) >= 10:
        return crowd_bias
    return random.choice(neighbors)

def most_common_elements(input_list):
    count = Counter(input_list)
    max_count = max(count.values())
    most_common = [item for item, freq in count.items() if freq == max_count]
    return most_common

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def swap_grids():
    global grid, new_grid
    temp = grid
    grid = new_grid
    new_grid = temp

def draw_grid(first_time):
    if DISPLAY_VISUALS:
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                cell_color = COLORS[new_grid[row][col]]
                old_color = COLORS[grid[row][col]]
                if cell_color != old_color or first_time or cell_color == BLACK:
                    cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, cell_color, cell_rect)

def step():
    global grid, new_grid, steps_this_round
    colors_remaining.clear()
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col] == 0:
                new_grid[row][col] = 0
            else:
                neighbors = get_neighbors(row, col)
                n = choose_next_state(neighbors)
                if n != 0:
                    new_grid[row][col] = n
                    colors_remaining.add(n)
    steps_this_round += 1

def get_neighbors(row, col):
    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == GRID_HEIGHT:
                i = 0
            if j == GRID_WIDTH:
                j = 0
            if i == -1:
                i = GRID_HEIGHT - 1
            if j == -1:
                j = GRID_WIDTH - 1
            if grid[i][j] != 0:
                neighbors.append(grid[i][j])
    return neighbors

def collect_samples():
    global new_grid, rounds_played, round_lengths, steps_this_round, fpst_start, fpst_end, five_percent_sampling_time
    if len(colors_remaining) == 1 and SAMPLE_SIZE > 0:
        rounds_played += 1
        round_lengths.append(steps_this_round)
        winning_teams.update(tuple(colors_remaining))
        steps_this_round = 0
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if grid[row][col] != 0:
                    grid[row][col] = initial_state_of_cell(row, col)
        adjust_initial_state_grid()
        new_grid = copy.deepcopy(grid)
        draw_grid(True)
        pygame.display.flip()
        percent_samples_taken = 100 * rounds_played / SAMPLE_SIZE
        if percent_samples_taken % 5 == 0:
            fpst_end = time.time()
            five_percent_sampling_time = fpst_end - fpst_start
            print(f"Sample Progress: {percent_samples_taken}% in {round(five_percent_sampling_time, 2)} seconds")
            fpst_start = time.time()

create_grid()
draw_grid(True)
pygame.display.flip()
running = True
mouse_pressed = False
fpst_start = time.time()
while running:
    time.sleep(TIME_BETWEEN_STEPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
        elif event.type == pygame.MOUSEMOTION and mouse_pressed:
            mouse_x, mouse_y = event.pos
            col = mouse_x // CELL_SIZE
            row = mouse_y // CELL_SIZE
            if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
                grid[row][col] = 0
                new_grid[row][col] = 0
    step()
    draw_grid(False)
    swap_grids()
    pygame.display.flip()
    collect_samples()
    if rounds_played >= SAMPLE_SIZE > 0:
        running = False
    
report_results()

pygame.quit()
sys.exit()