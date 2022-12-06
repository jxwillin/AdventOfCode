import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *



result = 0
for line in read_lines("input.1.txt"):
    sets = line.split(',')
    a, b = sets[0].split("-")
    set_a = set(range(int(a),int(b)+1))
    c, d = sets[1].split("-")
    set_b = set(range(int(c),int(d)+1))
    print(set_a, set_b)
    if len(set_a.union(set_b)) < len(set_a) + len(set_b):
        result += 1
print("=",result)

