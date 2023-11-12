import random

def random_game_length():
    return random.randint(100, 200)

def prisoners_dilemma(a_coop, b_coop):
    if a_coop and b_coop:
        return (2, 2)
    if a_coop and not b_coop:
        return (3, 0)
    if not a_coop and b_coop:
        return (0, 3)
    return (1, 1)

