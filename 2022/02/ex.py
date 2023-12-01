import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    CISOR = 3

    beats = {
        ROCK: CISOR,
        PAPER: ROCK,
        CISOR: PAPER
    }
    loses = {
        CISOR: ROCK,
        ROCK: PAPER,
        PAPER: CISOR
    }

    @classmethod
    def move_from_input(cls, s: str):
        if s == 'A' or s == 'X':
            return RPS.ROCK
        if s == 'B' or s == 'Y':
            return RPS.PAPER
        if s == 'C' or s == 'Z':
            return RPS.CISOR

    def get_winner(self):
        self.beats[self.value]

    def get_loser(self):
        self.loses[self.value]

    @classmethod
    def score_from_adv_and_result(cls, adv, res):
        if res == 'X':  # loss
            print('loss')
            move = adv.get_loser()
        if res == 'Y':  # draw
            print('draw')
            move = adv
        if res == 'Z':  # victory
            print('win')
            move = adv.get_winner()
        print(move)
        return move.score(adv) + move.value

    def score(self, other):
        if self.value == other.value:
            return 3
        elif (self.beats[self.value] == other):
            return 6
        else:
            return 0

# A, X: Rock
def easy():
    acc = 0
    for line in sys.stdin:
        round = line.split()
        adv = RPS.move_from_input(round[0])
        me = RPS.move_from_input(round[1])
        print('=============')
        print(line)
        print(me.value)
        print(me.score(adv))
        acc += me.score(adv) + me.value

    print(f'Score is {acc}')

def hard():
    acc = 0
    for line in sys.stdin:
        round = line.split()
        adv = RPS.move_from_input(round[0])
        goal = round[1]
        print('=============')
        print(line)
        print(adv.name)
        acc += RPS.score_from_adv_and_result(adv, goal)

    print(f'Score is {acc}')

if __name__ == '__main__':
    # easy()
    hard()