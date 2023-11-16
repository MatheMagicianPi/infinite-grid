import numpy as np
import copy

# Using NumPy arrays
rows = 9
cols = 9

grid = None
new_grid = None

# Define a function to generate a vector for each cell
def initial_vector(row, col):
    if col < 3:
        return np.array([1, 0, 0])
    if 3 <= col < 6:
        return np.array([0, 1, 0])
    if 6 <= col < 9:
        return np.array([0, 0, 1])

def swap_grids():
    global grid, new_grid
    temp = grid
    grid = new_grid
    new_grid = temp

def get_neighbors(col, row):
    neighbors = []
    for i in range(col - 1, col + 2):
        for j in range(row - 1, row + 2):
            if i == rows:
                i = 0
            if j == cols:
                j = 0
            if i == -1:
                i = rows - 1
            if j == -1:
                j = cols - 1
            neighbors.append(grid[i][j])
    return neighbors

def average_vectors(vectors):
    # Get the length of the vectors
    vector_length = len(vectors[0])

    # Initialize a list to store the sum of each component
    sum_components = [0] * vector_length

    # Calculate the sum of each component
    for vector in vectors:
        if len(vector) != vector_length:
            raise ValueError("All vectors must have the same length")
        sum_components = [sum(x) for x in zip(sum_components, vector)]

    # Calculate the average by dividing the sum by the number of vectors
    average_vector = [x / len(vectors) for x in sum_components]

    return average_vector

# Create a 2D array with vectors in each cell
grid = np.array([[initial_vector(col, row) for col in range(cols)] for row in range(rows)])
new_grid = copy.deepcopy(grid)

for _ in range(1):
    for row in range(cols):
        for col in range(rows):
            new_grid[col][row] = average_vectors(get_neighbors(col, row))
            swap_grids()

# Print the resulting 2D array
print(grid)