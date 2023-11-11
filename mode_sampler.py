import random
from collections import Counter
import statistics

def custom_mode(data):
    # Use Counter to count occurrences of each element
    counts = Counter(data)
    
    # Find the maximum count
    max_count = max(counts.values())
    
    # Create a list of elements with the maximum count (modes)
    modes = [item for item, freq in counts.items() if freq == max_count]
    
    # If there are multiple modes, randomly choose one
    return random.choice(modes) if modes else None

def normalize_counter(counter):
    normalized_counter = Counter()

    for key, value in counter.items():
        normalized_value = value / sample_size
        normalized_counter[key] = normalized_value

    return normalized_counter

sample_size = 1000000
choices = [1, 2, 3]
x1 = random.choices(choices, [1/3 + 0.04, 1/3 - 0.02, 1/3 - 0.02], k=sample_size)
x2 = random.choices(choices, [1/3 - 0.01, 1/3 + 0.02, 1/3 - 0.01], k=sample_size)
x3 = random.choices(choices, [1/3 - 0.01, 1/3 - 0.01, 1/3 + 0.02], k=sample_size)
winners = Counter()
for i in range(sample_size):
    instance = [x1[i], x2[i], x3[i]]
    winners.update([custom_mode(instance)])
print(normalize_counter(winners))