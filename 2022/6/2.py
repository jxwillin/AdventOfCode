import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

line = read_lines("input.1.txt")[0]
length = 14
for idx, c in enumerate(line):
    token = line[idx:idx+length]
    if len(token) == len(set(token)):
        print(idx+length)
        break
