import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

results = []
v = 0
for x in read_lines("input.1.txt"):
    if x != "":
        v += int(x)
    else:
        results.append(v)
        v = 0

results.append(v)
v = 0

results.sort()
results.reverse()
print(sum(results[0:3]))