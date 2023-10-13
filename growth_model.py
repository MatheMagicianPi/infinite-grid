import random
import pygame
import numpy as np
import time

# Define constants
GRID_WIDTH = 128
GRID_HEIGHT = 72
CELL_SIZE = 10  # Size of each cell
COLORS = {
    0: (255, 255, 255),
    1: (0, 0, 0),
}

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Growth Model")

# Initialize the grid with random colors

grid = np.random.choice([0, 0, 0, 0, 1], (GRID_HEIGHT, GRID_WIDTH))
new_grid = np.zeros((GRID_HEIGHT, GRID_WIDTH))
r = 0.3
m = 0.1

def adjacent_neighbors(coords):
    neighbors = dict()
    neighbors[0] = []
    neighbors[1] = []
    row = coords[0]
    col = coords[1]

    if row == 0:
        neighbors[(row - 1, col)] = None
    else:
        neighbors[(row - 1, col)] = grid[row - 1][col]
        neighbors[grid[row - 1][col]].append((row - 1, col))

    if row == GRID_HEIGHT - 1:
        neighbors[(row + 1, col)] = None
    else:
        neighbors[(row + 1, col)] = grid[row + 1][col]
        neighbors[grid[row + 1][col]].append((row + 1, col))

    if col == 0:
        neighbors[(row, col - 1)] = None
    else:
        neighbors[(row, col - 1)] = grid[row, col - 1]
        neighbors[grid[row][col - 1]].append((row, col - 1))

    if col == GRID_WIDTH - 1:
        neighbors[(row, col + 1)] = None
    else:
        neighbors[(row, col + 1)] = grid[row, col + 1]
        neighbors[grid[row][col + 1]].append((row, col + 1))

    return neighbors

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            cell = grid[row][col]
            neighbors = adjacent_neighbors((row, col))
            live = len(neighbors[1])
            new_grid[row][col] = cell
            if cell == 0 and live >= 2 and random.uniform(0, 1) <= r:
                new_grid[row][col] = 1
            elif cell == 1 and random.uniform(0, 1) <= m:
                new_grid[row][col] = 0

    # Draw the grid
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            pygame.draw.rect(screen, COLORS[new_grid[row][col]], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    grid = new_grid

pygame.quit()
