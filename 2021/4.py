with open('4.in') as f:
    groups = f.read().split('\n\n')

class Board():
    def __init__(self, b):
        self.board = [[int(i) for i in row.split()] for row in b.splitlines()]
        self.marked = [[0 for j in range(5)] for i in range(5)]
        self.wins = 0
    
    def mark(self, d):
        for j in range(5):
            for i in range(5):
                if self.board[j][i] == d:
                    self.marked[j][i] = 1
                    if all(self.marked[j]) or all([self.marked[y][i] for y in range(5)]):
                        self.wins += 1
                        return True
                    break

    def score(self, d):
        return d * sum([(not self.marked[j][i])*self.board[j][i] for i in range(5) for j in range(5)])

boards = [Board(i) for i in groups[1:]]
winners = []
ds = [int(i) for i in groups[0].split(',')]

for d in ds:
    for board in boards:
        if board.mark(d) and board.wins == 1: winners.append(board.score(d))

print(winners[0], winners[-1])
