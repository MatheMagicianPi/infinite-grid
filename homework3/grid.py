import pygame
import sys
import random  # Import the random module

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 20  # Size of each cell in pixels
GRID_WIDTH = 200  # Number of cells in the horizontal direction
GRID_HEIGHT = 500  # Number of cells in the vertical direction
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
ZOOM_FACTOR = 1.2  # Zoom in/out factor
PAN_SPEED = 5

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Name of Window")

grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Initialize zoom and pan variables
zoom = 0.5
pan_x, pan_y = 0, 0

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

        for row in range(1, GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                neighbors = [] # will have five elements
                if col <= 1:
                    neighbors.append(0)
                else:
                    neighbors.append(grid[row - 1][col - 2])
                if col == 0:
                    neighbors.append(0)
                else:
                    neighbors.append(grid[row - 1][col - 1])
                neighbors.append(grid[row - 1][col])
                if col == GRID_WIDTH - 1:
                    neighbors.append(0)
                else:
                    neighbors.append(grid[row - 1][col + 1])
                if col >= GRID_WIDTH - 2:
                    neighbors.append(0)
                else:
                    neighbors.append(grid[row - 1][col + 2])
                # grid[row][col] = either 0 or 1
                # based on the list `neighbors`

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
    screen.fill(WHITE)

    # Draw the grid
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cell_color = BLACK if grid[y][x] else WHITE
            cell_rect = pygame.Rect(
                x * CELL_SIZE * zoom + pan_x, y * CELL_SIZE * zoom + pan_y, CELL_SIZE * zoom, CELL_SIZE * zoom
            )
            pygame.draw.rect(screen, cell_color, cell_rect)

    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
