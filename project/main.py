from collections import Counter
import pygame
import random

# Define constants
WIDTH, HEIGHT = 1200, 600
CELL_SIZE = 20
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Initialize pygame
pygame.init()

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("War Simulation")

COLORS = {
    0 : (255, 255, 255),
    1 : (0, 0, 0),
    2 : (255, 0, 0),
    3 : (0, 255, 0)
}

class Troops:

    def __init__(self, team_id, location):
        self.team_id = team_id
        self.location = location
    
    def get_team(self):
        return self.team_id
    
    def get_location(self):
        return self.location
    
    def move(self, new_location):
        self.location = new_location

    def __repr__(self):
        return str(self.team_id) + " @ " + str(self.location)

# Create a 2D array to represent the grid
grid = [[Troops(random.randint(1, 3), (row, col)) for col in range(COLS)] for row in range(ROWS)]
new_grid = [[None for col in range(COLS)] for row in range(ROWS)]

def neighbors(location):
    neighbors = []
    row = location[0]
    col = location[1]
    if row != 0:
        neighbors.append(grid[row - 1][col].get_team())
    if row != ROWS - 1:
        neighbors.append(grid[row + 1][col].get_team())
    if col != 0:
        neighbors.append(grid[row][col - 1].get_team())
    if col != COLS - 1:
        neighbors.append(grid[row][col + 1].get_team())
    return Counter(neighbors)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row in range(ROWS):
        for col in range(COLS):
            cell = grid[row][col]
            new_grid[row][col] = cell
            neighbors_counter = neighbors((row, col))
            neighbors_count = neighbors_counter.most_common(len(neighbors_counter))
            winning_team = neighbors_count[0][0]
            strength = neighbors_count[0][1]
            if cell.get_team() != 0:
                new_grid[row][col] = Troops(winning_team, (row, col))

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the grid
    for row in range(ROWS):
        for col in range(COLS):
            cell_color = COLORS[grid[row][col].get_team()]
            pygame.draw.rect(screen, cell_color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.flip()

    grid = new_grid

# Quit pygame
pygame.quit()
