import random
from collections import Counter
import statistics

array = [[1 for _ in range(2)] for _ in range(3)]
array[-1][4] = 3
print(array)