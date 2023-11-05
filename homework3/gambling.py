import random

def play_one_round():
    money = 100
    steps = 1000
    results = (1, -1)
    stops = {0, 120}
    for s in range(steps):
        money += random.choice(results)
        if money in stops:
            break
    return money

def average_per_1000():
    winnings = 0
    for i in range(1000):
        winnings += play_one_round() - 100
    return(winnings / 1000.0)

s = []
for i in range(10):
    s.append(average_per_1000())
print(s)