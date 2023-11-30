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

def sort_dict_by_keys(input_dict):
    sorted_items = sorted(input_dict.items())
    return sorted_items

N = 2
P = 6

for p in range(1, 15):
    modes_count = Counter()
    for t in orderings(N, p):
        modes_count.update((frozenset(modes_of(t)),))

    size_to_score = dict()

    for s in modes_count.keys():
        size_to_score[len(s)] = modes_count[s]

    print(f"({N}, {p}) -> {sort_dict_by_keys(size_to_score)} vs guess: [(1, {2**(p-1)}), (2, {2})]")