from itertools import product
from collections import Counter

def orderings(n, p):
    # Generate all possible combinations of numbers from 1 to n with repetition
    combinations = product(range(1, n+1), repeat=p)
    
    # Convert the combinations to a set of tuples
    result_set = set(combinations)
    
    return result_set

def modes_of(input_tuple):
    # Use Counter to count the occurrences of each element in the tuple
    element_counts = Counter(input_tuple)
    
    # Find the maximum frequency
    max_frequency = max(element_counts.values())
    
    # Filter elements that have the maximum frequency (modes)
    modes = {element for element, frequency in element_counts.items() if frequency == max_frequency}
    
    return modes

N = 2
P = 3

for n in range(3, 4):
    for p in range(2, 20, 1):
        modes_count = Counter()
        for t in orderings(n, p):
            modes_count.update((frozenset(modes_of(t)),))

        size_to_score = dict()

        for s in modes_count.keys():
            size_to_score[len(s)] = modes_count[s]

        print(f"({n}, {p}) -> {size_to_score}")