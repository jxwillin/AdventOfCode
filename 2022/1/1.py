import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

max_v = 0
v = 0
for x in read_lines("input.1.txt"):
    if x != "":
        v += int(x)
    else:
        if v > max_v:
            max_v = v
        v = 0
if v > max_v:
    max_v = v
v = 0
print(max_v)