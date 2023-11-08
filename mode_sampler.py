import random
from collections import Counter
import statistics

n = 10


xk = [1, 2, 3]  # Possible outcomes
pks = []
for i in range(n):
    pk1 = random.uniform(0, 1)
    pk2 = random.uniform(0, 1 - pk1)
    pk3 = 1 - pk1 - pk2
    pk = [pk1, pk2, pk3]  # Probabilities
    pks.append(pk)
sample = []
for i in range(n):
    sample.append(random.choices(xk, pks[i], k=1)[0])
print(statistics.mode(sample))