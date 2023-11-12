import random

a_history = []
b_history = []

a_score = 0
b_score = 0

def random_game_length():
    return random.randint(100, 200)

def prisoners_dilemma_result(a_coop, b_coop):
    if a_coop and b_coop:
        return (2, 2)
    if a_coop and not b_coop:
        return (0, 3)
    if not a_coop and b_coop:
        return (3, 0)
    return (1, 1)

def always_cooperate(opponent_history):
    return True

def always_defect(opponent_history):
    return False

def tit_for_tat(opponent_history):
    if len(opponent_history) == 0:
        return True
    return opponent_history[-1]

def grim_trigger(opponent_history):
    if False in opponent_history:
        return False
    return True

def my_strategy(opponent_history):
    if len(opponent_history) >= 3 and len(set(opponent_history[-3:])) == 1:
        return False
    return tit_for_tat(opponent_history)
    

def play_one_prisoners_dilemma(a_strategy, b_strategy):
    global a_score, b_score, a_history, b_history
    a_move = a_strategy(b_history)
    b_move = b_strategy(a_history)
    a_history.append(a_move)
    b_history.append(b_move)
    result = prisoners_dilemma_result(a_move, b_move)
    a_score += result[0]
    b_score += result[1]

def reset():
    global a_history, b_history, a_score, b_score
    a_history = []
    b_history = []
    a_score = 0
    b_score = 0

for _ in range(random_game_length()):
    play_one_prisoners_dilemma(my_strategy, grim_trigger)

print("Final score:", str((a_score, b_score)))