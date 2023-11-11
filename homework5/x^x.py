import random
import numpy

sample_size = 1E8
in_area = 0
for _ in range(int(sample_size)):
    r = (random.uniform(0, 1), random.uniform(0, 1))
    if r[1] <= r[0] ** r[0]:
        in_area += 1
print("monte carlo: ", in_area / sample_size)
print("claim: ", numpy.pi / 4)

# monte carlo:  0.78341448
# claim:  0.7853981633974483