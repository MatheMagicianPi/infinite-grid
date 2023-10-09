import pygame
import numpy as np

# Define constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
CELL_SIZE = 20  # Size of each cell

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Infinite 2D Grid")

# Initialize the grid with random colors
grid_width = SCREEN_WIDTH // CELL_SIZE
grid_height = SCREEN_HEIGHT // CELL_SIZE
grid = np.random.choice([0, 1], (grid_height, grid_width))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the grid
    for row in range(grid_height):
        for col in range(grid_width):
            color = (0, 0, 0) if grid[row][col] == 1 else (255, 255, 255)
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

pygame.quit()
