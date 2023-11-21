from collections import Counter

file_path = "homework6/cm.txt"
with open(file_path, 'r') as file:
    words = file.read().split()
word_freq = Counter(words)
sorted_freqs = sorted(word_freq.values(), reverse=True)
L = len(sorted_freqs)

errors = []

for i in range(L):
    expected = L / (i + 3) # 1/(x+3) scaled to the number of words
    error = abs(expected - sorted_freqs[i])
    errors.append(round(error / L, 3)) # error as percentage of L

print(errors)