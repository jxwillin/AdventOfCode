import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *


ROCK     = 1#: A X
PAPER    = 2#: B Y
SCISSORS = 3#: C Z

# X Lose
# Y Draw
# Z Win

DRAW = 3
WIN  = 6
LOSE = 0

map = dict()
map["A X"] = LOSE + SCISSORS
map["B X"] = LOSE + ROCK
map["C X"] = LOSE + PAPER
map["A Y"] = DRAW + ROCK
map["B Y"] = DRAW + PAPER
map["C Y"] = DRAW + SCISSORS
map["A Z"] = WIN + PAPER
map["B Z"] = WIN + SCISSORS
map["C Z"] = WIN + ROCK

result = 0
for line in read_lines("input.1.txt"):
    print(map[line])
    result += map[line]
print(result)