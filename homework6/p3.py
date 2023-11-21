from collections import Counter

file_path = "homework6/cm.txt"

# extract word frequencies in order
with open(file_path, 'r') as file:
    words = file.read().split()
word_freq = Counter(words)
sorted_freqs = sorted(word_freq.values(), reverse=True)

# number of distinct words found
L = len(sorted_freqs)


# find error of the 1/(x+3) estimate
errors = []
for i in range(L):
    expected = L / (i + 3) # 1/(x+3) scaled to L
    error = abs(expected - sorted_freqs[i]) # calculate error
    errors.append(round(error / L, 3)) # error as percentage of L

# print(errors)
# print(errors[0:100])
# print(max(errors[0:100]))