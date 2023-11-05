import random
import time
import numpy as np
from scipy.linalg import eigvals
from scipy.linalg import eig

def first_eigenvalue(matrix):
    matrix = np.array(matrix)
    eigenvalues = eigvals(matrix)
    return max(eigenvalues)

def find_eigenvectors(matrix, eigenvalue):
    matrix = np.array(matrix)
    eigenvalues, eigenvectors = eig(matrix)
    eigenvalue_index = np.where(np.isclose(eigenvalues, eigenvalue))[0][0]
    eigenvector = eigenvectors[:, eigenvalue_index]
    return eigenvector.tolist()

def calculate_normalized_value(v, matrix):
    v = np.array(v)
    matrix = np.array(matrix)
    Av = np.dot(matrix, v)
    norm_Av = np.linalg.norm(Av)
    result = Av / norm_Av
    return result

def calculate_difference_norm(matrix, v, lmbda):
    matrix = np.array(matrix)
    v = np.array(v)
    Av = np.dot(matrix, v)
    result = Av - (lmbda * v)
    return np.linalg.norm(result)

n = 2000
iterations = 50

start_time = time.process_time()
matrix = [[random.choices([0, 1], weights=[0.99, 0.01])[0] for _ in range(n)] for _ in range(n)]
end_time = time.process_time()
elapsed_time = end_time - start_time

print(f"(1) created {n} by {n} matrix in {elapsed_time} CPU seconds")

start_time = time.process_time()
eig_val = first_eigenvalue(matrix)
end_time = time.process_time()
elapsed_time = end_time - start_time

print(f"(2) first eigenvalue {eig_val} found in {elapsed_time} CPU seconds")

start_time = time.process_time()
eig_vec = find_eigenvectors(matrix, eig_val)
end_time = time.process_time()
elapsed_time = end_time - start_time

print(f"(3) first eigenvector found in {elapsed_time} CPU seconds")

start_time = time.process_time()
rand_vec = np.random.rand(n)
end_time = time.process_time()
elapsed_time = end_time - start_time

print(f"(4) created random vector of length {n} in {elapsed_time} CPU seconds")

start_time = time.process_time()
vec = rand_vec
for i in range(iterations):
    vec = calculate_normalized_value(vec, matrix)

end_time = time.process_time()
elapsed_time = end_time - start_time

print(f"(5) iterated matrix on random vector {iterations} times in {elapsed_time} CPU seconds")

print(f"(6) ||Av - lambda * v|| = {calculate_difference_norm(matrix, vec, eig_val)}")