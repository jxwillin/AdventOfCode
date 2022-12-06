import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

line = read_lines("input.1.txt")[0]
for idx, c in enumerate(line):
    token = line[idx:idx+4]
    if len(token) == len(set(token)):
        print(idx+4)
        break
