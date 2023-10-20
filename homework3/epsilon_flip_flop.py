import random

EPSILON = 10**-3
TRANSITION_PROBABILITY = 1 - EPSILON

def play_one():
    step = 1
    r = random.uniform(0, 1)
    while r <= TRANSITION_PROBABILITY:
        step += 1
        r = random.uniform(0, 1)
    return step

import matplotlib.pyplot as plt
import random
import numpy as np

# Sample unsorted dataset of integers
data = [random.randint(1, 100) for _ in range(1000)]  # Replace with your dataset

# Count the frequencies of integers
values, counts = np.unique(data, return_counts=True)

# Create an array of x-coordinates for the dots
x_coordinates = range(len(values))

# Create a scatter plot with dots at the top of each bin
plt.scatter(x_coordinates, counts, s=100, c='b', marker='o', label='Frequency')

# Set custom x-axis labels
plt.xticks(x_coordinates, values)

# Adding labels and a title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Dot Plot with Dots at the Top of Each Bin')

# Display the dot plot
plt.legend()
plt.grid(True)
plt.show()