import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

width = 0
data = None
def get(x,y):
    pos = width*y+x
    return data[pos]

def robust_range(x,y, reverse = False):
    result = list(range( min(x,y), max(x,y)))
    if reverse:
        result.reverse()
    return result

def compute(p, t, reverse):
    pass

def logic(x,y):
    v = get(x,y)
    if x in [0, width-1] or y in [0, height-1]:
        return True, 0
    else:
        w = True
        wd = x
        ar1 = robust_range(x,0, True)
        for a in ar1:
            if v <= get(a, y):
                w = False
                wd = abs(a-x)
                break

        e = True
        ed = (width - 1) - x
        ar2 = robust_range(x+1,width)
        for a in ar2:
            if v <= get(a, y):
                e = False
                ed = abs(a-x)
                break

        n = True
        nd = y
        br1 = robust_range(y,0, True)
        for b in br1:
            if v <= get(x,b):
                n = False
                nd = abs(b-y)
                break

        s = True
        sd = (height - 1)-y
        br2 = robust_range(y+1,height)
        for b in br2:
            if v <= get(x,b):
                s = False
                sd = abs(b-y)
                break
        
        score = nd*sd*wd*ed
        cond = w or e or n or s
        return cond, score

lines = read_lines("input.txt")
width = len(lines[0])
height = len(lines)
data = "".join(lines)
count = 0

high_score = 0
for y in range(height):
    line = ""
    for x in range(width):
        cond, score = logic(x,y)
        high_score = max( score, high_score)
        if cond:
            line += get(x,y)
            count += 1
        else:
            line += 'x'
    print(line)
print("1:", count)
print("2:", high_score)