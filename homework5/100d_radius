import random
import numpy

sample_size = int(1E6)

def random_f_value():
    result = 0
    for _ in range(100):
        result += random.uniform(0, 1) ** 2
    return numpy.sqrt(result)

sum = 0
for _ in range(sample_size):
    sum += random_f_value()

print(sum / sample_size)