import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

def calc(data):
    if len(data) > 0:
        tmp = set(data[0])
        for item in data[1:]:
            tmp = tmp.intersection(item)
        print(tmp)
        common = next(iter(tmp))
        pri = (27 + LETTERS_UPPER.rfind(common)) if LETTERS_LOWER.rfind(common) == -1 else 1+LETTERS_LOWER.rfind(common)
        return pri
    return 0

result = 0
lines = read_lines("input.1.txt")
data = splt_into_groups(3, lines)
for item in data:
    result += calc(item)

print("=", result)