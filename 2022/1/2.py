import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

max_v = 0
v = 0
results = []
for x in read_lines("input.1.txt"):
    if x != "":
        v += int(x)
    else:
        if v > max_v:
            max_v = v
        results.append(v)
        v = 0

if v > max_v:
    max_v = v
results.append(v)
v = 0

results.sort()
results.reverse()
print(sum(results[0:3]))