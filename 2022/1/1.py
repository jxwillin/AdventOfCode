import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

results = []
for x in group_by_blanks(read_lines("test.1.txt")):
    results.append(sum([int(y) for y in x]))   
results.sort()
print(results[-1])
