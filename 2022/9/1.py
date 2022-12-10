import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

import math

class Pos:
    def __init__(self):
        self.x = 0
        self.y = 0


lines = read_lines("input.txt")

head = Pos()
tail_1 = Pos()
tail_2 = Pos()
tail_3 = Pos()
tail_4 = Pos()
tail_5 = Pos()
tail_6 = Pos()
tail_7 = Pos()
tail_8 = Pos()
tail_9 = Pos()

dir_map = dict()
dir_map['U'] = (0,1)
dir_map['D'] = (0,-1)
dir_map['L'] = (-1,0)
dir_map['R'] = (1,0)
def step_head(head, action):
    x, y = dir_map[action]
    head.x += x
    head.y += y

def sign(x):
    return (x > 0) - (x < 0)

nbs = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]

def step_tail(head, tail):
    delta_x = max(0,abs(tail.x - head.x)-1)
    delta_y = max(0,abs(tail.y - head.y)-1)
    if delta_x >0 or delta_y > 0:
        dis = 10
        move = (0,0)
        for nb in nbs:
            delta = math.sqrt(math.pow((tail.x+nb[0])-head.x,2)+math.pow((tail.y+nb[1])-head.y,2))
            if delta < dis:
                dis = delta
                move = nb
        tail.x += move[0]
        tail.y += move[1]

def vis_tail(height, asd, oc, nc):
    if asd.x == x and height-asd.y == y:
        return nc
    else:
        return oc


def vis():
    width = 12
    height = 12

    for y in range(height):
        line = ""
        for x in range(width):
            c = '.'
            if tail_9.x == x and height-tail_9.y == y:
                c='9'
            if tail_8.x == x and height-tail_8.y == y:
                c='8'
            if tail_7.x == x and height-tail_7.y == y:
                c='7'
            if tail_6.x == x and height-tail_6.y == y:
                c='6'
            if tail_5.x == x and height-tail_5.y == y:
                c='5'
            if tail_4.x == x and height-tail_4.y == y:
                c='4'
            if tail_3.x == x and height-tail_3.y == y:
                c='3'
            if tail_2.x == x and height-tail_2.y == y:
                c='2'
            if tail_1.x == x and height-tail_1.y == y:
                c='1'
            if head.x == x and height-head.y == y:
                c='H'
            line += c
        print(line)

tail_1_poss = []
tail_9_poss = []
for x in lines:
    print(x)
    tokens = x.split(' ')
    dir = tokens[0]
    dist = int(tokens[1])

    for i in range(dist):
        step_head(head, dir)
        step_tail(head, tail_1)
        step_tail(tail_1, tail_2)
        step_tail(tail_2, tail_3)
        step_tail(tail_3, tail_4)
        step_tail(tail_4, tail_5)
        step_tail(tail_5, tail_6)
        step_tail(tail_6, tail_7)
        step_tail(tail_7, tail_8)
        step_tail(tail_8, tail_9)
        if (tail_1.x, tail_1.y) not in tail_1_poss:
            tail_1_poss.append((tail_1.x, tail_1.y))
        if (tail_9.x, tail_9.y) not in tail_9_poss:
            tail_9_poss.append((tail_9.x, tail_9.y))
        #print("\tH:", head.x, head.y)
        #print("\tT:", tail.x, tail.y)
    vis()

print("1:", len(tail_1_poss))
print("2:", len(tail_9_poss))