import numpy as np
import copy

# Using NumPy arrays
rows = 9
cols = 9

grid = None
new_grid = None

# Define a function to generate a vector for each cell
def initial_vector(row, col):
    # return np.array([1.0, 0.0])
    if col < 5:
        return np.array([1.0, 0.0, 0.0])
    if 5 <= col < 8:
        return np.array([0.0, 1.0, 0.0])
    if 8 <= col < 9:
        return np.array([0.0, 0.0, 1.0])

def adjust_grid():
    global grid
    # grid[0][0] = np.array([0.0, 1.0])

def swap_grids():
    global grid, new_grid
    temp = grid
    grid = new_grid
    new_grid = temp

def get_neighbors(row, col):
    neighbors = []
    for i in range(col - 1, col + 2):
        for j in range(row - 1, row + 2):
            if i == cols:
                i = 0
            if j == rows:
                j = 0
            if i == -1:
                i = cols - 1
            if j == -1:
                j = rows - 1
            neighbors.append(grid[j][i])
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

def sum_array(array_2d):
    # Get the length of the vectors
    vector_length = len(array_2d[0][0])

    # Initialize a list to store the sum of each component
    sum_components = [0] * vector_length

    # Calculate the sum of each component
    for row in array_2d:
        for vector in row:
            if len(vector) != vector_length:
                raise ValueError("All vectors must have the same length")
            sum_components = [sum(x) for x in zip(sum_components, vector)]

    # Create a vector representing the sum
    sum_vector = np.array(sum_components)

    return sum_vector

# Create a 2D array with vectors in each cell
grid = np.array([[initial_vector(col, row) for row in range(rows)] for col in range(cols)])
adjust_grid()
new_grid = copy.deepcopy(grid)

for _ in range(10000):
    for col in range(cols):
        for row in range(rows):
            next_cell = average_vectors(get_neighbors(col, row))
            new_grid[col][row] = next_cell
            swap_grids()

# Print the resulting 2D array
print(grid)
print(sum_array(grid))