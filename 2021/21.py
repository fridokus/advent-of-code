with open('21.in') as f:
    p0 = [int(i[-1]) for i in f.read().splitlines()]

class Die():
    def __init__(self):
        self.rolls = 0
        self.value = 0

    def roll(self):
        self.value = self.value % 100 + 1
        self.rolls += 1
        return self.value

die = Die()
scores = [0, 0]
p = list(p0)

win = False
while not win:
    for i in range(2):
        for _ in range(3):
            p[i] = (p[i] + die.roll() - 1) % 10 + 1
        scores[i] += p[i]
        if scores[i] >= 1000:
            win = True
            break

print(scores[i-1] * die.rolls)

dist = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
       }

states = [[[0 for i in range(11)] for j in range(21)] for k in range(2)]
for p in range(2): states[p][0][p0[i]] = 1

wins = [0, 0]
while any([any([any(j) for j in i]) for i in states]):
    for p in range(2):
        new_state = [[0 for i in range(11)] for j in range(21)]
        wins_if_win = sum([sum(i) for i in states[p-1]])
        for s in range(21):
            for pos in range(1, 11):
                for roll in range(3, 10):
                    new_pos = (pos + roll - 1) % 10 + 1
                    if new_pos + s >= 21:
                        wins[p] += dist[roll] * states[p][s][pos] * wins_if_win
                    else:
                        new_state[new_pos + s][new_pos] += dist[roll] * states[p][s][pos]
        states[p] = new_state

print(max(wins))
