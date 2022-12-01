import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

max_v = 0
v = 0
def if_max_store(x):
    global max_v
    if x > max_v:
        max_v = x

for x in read_lines("test.1.txt"):
    if x != "":
        v += int(x)
    else:
        if_max_store(v)
        v = 0
if_max_store(v)
v = 0
print(max_v)