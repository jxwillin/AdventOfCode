import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *


ROCK     = 1#: A X
PAPER    = 2#: B Y
SCISSORS = 3#: C Z

DRAW = 3
WIN  = 6
LOSE = 0

map = dict()
map["A X"] = DRAW + ROCK
map["B X"] = LOSE + ROCK
map["C X"] = WIN + ROCK
map["A Y"] = WIN + PAPER
map["B Y"] = DRAW + PAPER
map["C Y"] = LOSE + PAPER
map["A Z"] = LOSE + SCISSORS
map["B Z"] = WIN + SCISSORS
map["C Z"] = DRAW + SCISSORS

result = 0
for line in read_lines("input.1.txt"):
    print(map[line])
    result += map[line]
print(result)