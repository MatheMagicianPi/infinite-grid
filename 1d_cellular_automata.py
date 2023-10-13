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
# RULE_NUMBER = random.randint(0, 2**32 - 1)
RULE_NUMBER = 2202350827
RANDOM_NUMBER = False
RANDOM_START = False
# Triangles: 2**31 + 1
# Order to Chaos: 2420521844
# Chaos to Order: 2515161969
# Geometry: 3488981109
# order chaos split: 3216760548
# house: 2135742347
# total order, objects in 4D: 825818938

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("1D Automata with 5 Neighbors")

grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Initialize zoom and pan variables
zoom = 0.5
pan_x, pan_y = 0, 0

def int_to_binary_tuple(n):
    if n < 0 or n >= 2**32:
        raise ValueError("Input integer must be between 0 and 2^32 - 1")

    binary_str = format(n, '032b')  # Convert to binary string with 32 bits
    binary_tuple = tuple(map(int, binary_str))  # Convert to a tuple of integers
    return binary_tuple

def tuple_to_binary_int(tuple_5):
    binary_str = ''.join(map(str, tuple_5))
    binary_int = int(binary_str, 2)
    return binary_int

rules = {
    (0, 0, 0, 0, 0): 0,
    (0, 0, 0, 0, 1): 0,
    (0, 0, 0, 1, 0): 0,
    (0, 0, 0, 1, 1): 0,
    (0, 0, 1, 0, 0): 0,
    (0, 0, 1, 0, 1): 0,
    (0, 0, 1, 1, 0): 0,
    (0, 0, 1, 1, 1): 0,
    (0, 1, 0, 0, 0): 0,
    (0, 1, 0, 0, 1): 0,
    (0, 1, 0, 1, 0): 0,
    (0, 1, 0, 1, 1): 0,
    (0, 1, 1, 0, 0): 0,
    (0, 1, 1, 0, 1): 0,
    (0, 1, 1, 1, 0): 0,
    (0, 1, 1, 1, 1): 0,
    (1, 0, 0, 0, 0): 0,
    (1, 0, 0, 0, 1): 0,
    (1, 0, 0, 1, 0): 0,
    (1, 0, 0, 1, 1): 0,
    (1, 0, 1, 0, 0): 0,
    (1, 0, 1, 0, 1): 0,
    (1, 0, 1, 1, 0): 0,
    (1, 0, 1, 1, 1): 0,
    (1, 1, 0, 0, 0): 0,
    (1, 1, 0, 0, 1): 0,
    (1, 1, 0, 1, 0): 0,
    (1, 1, 0, 1, 1): 0,
    (1, 1, 1, 0, 0): 0,
    (1, 1, 1, 0, 1): 0,
    (1, 1, 1, 1, 0): 0,
    (1, 1, 1, 1, 1): 0
}

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle zooming
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:  # Handle both '+' and 'numpad +'
                zoom *= ZOOM_FACTOR
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:  # Handle both '-' and 'numpad -'
                zoom /= ZOOM_FACTOR
            elif event.key == pygame.K_SPACE:
                if RANDOM_NUMBER:
                    RULE_NUMBER = random.randint(0, 2**32 - 1)
                print("Rule number: " + str(RULE_NUMBER))
                # Grid representation
                if RANDOM_START:
                    grid = [[random.randint(0, 1) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
                else:
                    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
                    grid[0][GRID_WIDTH // 2] = 1
                rule_number = int_to_binary_tuple(RULE_NUMBER)
                for tuple_ in rules.keys():
                    rules[tuple_] = rule_number[tuple_to_binary_int(tuple_)]

                for row in range(1, GRID_HEIGHT):
                    for col in range(GRID_WIDTH):
                        neighbors = []
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
                        grid[row][col] = rules[tuple(neighbors)]


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
