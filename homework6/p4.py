epsilon = 10**-10
old_optimal_time = lambda c1, c4: ((c1 * ((1000 + epsilon) * c1)) + 1000 * c1 * c4 + ((1000 + epsilon) * c4) * c4) / (c1 + c4)
new_optimal_time = lambda c1, c4: 1000 * (c1 + c4)

c1 = 1
c4 = 1

print(new_optimal_time(c1, c4) / old_optimal_time(c1, c4))
print(4000 / (3000 + 4 * epsilon))

