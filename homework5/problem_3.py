import numpy as np
from sympy import symbols, Matrix, simplify, expand

# Define symbolic variables for p and q
p1, p2 = symbols('p1 p2')
p3 = 1 - p1 - p2
q1, q2 = symbols('q1 q2')
q3 = 1 - q1 - q2

# Create a 3x3 matrix A
P = Matrix([[1, 2, 4],
            [-3, 0, 2],
            [1, 2, 1]])

# Create symbolic vectors p and q
p = Matrix([p1, p2, p3])
q = Matrix([q1, q2, q3])

# Substitute specific values for some variables
p_values = {p1: 0, p2: 1}  # Assign specific values to p1 and p2
q_values = {q1: 1, q2: 0}  # Assign specific values to q1 and q2

# Calculate the dot product of q and A*p
result = simplify(expand(p.dot(P*q).subs(p_values).subs(q_values)))
result = simplify(expand(p.dot(P*q)))

# Print the result
print(f"{result}")
