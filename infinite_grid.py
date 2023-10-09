import random
import pygame
import numpy as np
import time

# Define constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
CELL_SIZE = 20  # Size of each cell
COLORS = {
    0: (150, 150, 150),
    1: (100, 100, 100),
    2: (0, 0, 0)
}

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Infinite 2D Grid")

# Initialize the grid with random colors
grid_width = SCREEN_WIDTH // CELL_SIZE
grid_height = SCREEN_HEIGHT // CELL_SIZE
grid = np.random.choice([0, 1, 2], (grid_height, grid_width))

def adjacent_neighbors(coords):
    neighbors = dict()
    neighbors[0] = []
    neighbors[1] = []
    neighbors[2] = []
    row = coords[0]
    col = coords[1]

    if row == 0:
        neighbors[(row - 1, col)] = None
    else:
        neighbors[(row - 1, col)] = grid[row - 1][col]
        neighbors.get(grid[row - 1][col]).append((row - 1, col))
    if col == grid_width - 1:
        neighbors[(row, col - 1)] = None
    else:
        neighbors[(row, col - 1)] = grid[row][col - 1]
        neighbors.get(grid[row][col - 1]).append((row, col - 1))
    if row == grid_height - 1:
        neighbors[(row + 1, col)] = None
    else:
        neighbors[(row + 1, col)] = grid[row + 1][col]
        neighbors.get(grid[row + 1][col]).append((row + 1, col))
    if col == 0:
        neighbors[(row, col - 1)] = None
    else:
        neighbors[(row, col - 1)] = grid[row][col - 1]
        neighbors.get(grid[row][col - 1]).append((row, col - 1))

    return neighbors

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    coordinates = (random.randint(0, grid_height - 1), random.randint(0, grid_width - 1))
    cell = grid[coordinates[0]][coordinates[1]]
    neighbors = adjacent_neighbors(coordinates)
    if cell == 2:
        if 2 in neighbors.values():
            kill = random.choice(neighbors.get(2))
            grid[kill[0]][kill[1]] = 0
        elif 1 in neighbors.values() and 0 in neighbors.values():
            child = random.choice(neighbors.get(0))
            grid[child[0]][child[1]] = random.choice((1, 2))
        elif 0 in neighbors.values():
            move = random.choice(neighbors.get(0))
            grid[move[0]][move[1]] = 1
            grid[coordinates[0]][coordinates[1]] = 0
    if cell == 1:
        if 0 not in neighbors.values():
            grid[coordinates[0]][coordinates[1]] = 0
        else:
            move = random.choice(neighbors.get(0))
            grid[move[0]][move[1]] = 1
            grid[coordinates[0]][coordinates[1]] = 0


    # # Clear the screen
    # screen.fill((255, 255, 255))

    # Draw the grid
    for row in range(grid_height):
        for col in range(grid_width):
            pygame.draw.rect(screen, COLORS[grid[row][col]], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

pygame.quit()
