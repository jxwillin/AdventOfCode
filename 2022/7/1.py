import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

curdir, files = '/', {'/':0}
for line in read_lines("input.txt"):
    tokens = line.split(' ')
    if tokens[0] == '$':
        if tokens[1] == 'cd':
            curdir = os.path.abspath(os.path.join(curdir, tokens[2]))
    elif tokens[0] == 'dir':
        files[os.path.join(curdir,tokens[1])+'/'] = 0
    else:
        files[os.path.join(curdir,tokens[1])] = int(tokens[0])

dirs = [key for key in files if key.endswith('/')]
sizes = sorted([sum([size for fn,size in files.items() if fn.startswith(d)]) 
         for d in dirs])

print("1:", sum([x for x in sizes if x < 100000]))
required = 30000000 - (70000000 - sizes[-1])
sizes.sort()
for idx, v in enumerate(sizes):
    if v > required:
        break
print("2:", sizes[idx]) # 2