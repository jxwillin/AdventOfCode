import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

result = 0
for line in read_lines("input.1.txt"):
    left = line[0:len(line)//2]
    right = line[len(line)//2:]
    common = next(iter(set(left).intersection(right)))
    print(common)
    pri = (27 + LETTERS_UPPER.rfind(common)) if LETTERS_LOWER.rfind(common) == -1 else 1+LETTERS_LOWER.rfind(common)
    result += pri

print("=", result)