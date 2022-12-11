import cProfile

import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

import math

m_invs = []
m_ops = []
m_div = []
m_tru = []
m_fal = []
m_cnt = []

groups = group_by_blanks(read_lines("input.txt"))
for group in groups:
    m_invs.append([ int(x) for x in group[1].split(':')[1].split(',')])
    m_ops.append(list(filter(lambda item : item != '', group[2].split('=')[1].split(' '))))
    m_div.append(int(group[3].split(' ')[-1]))
    m_tru.append(int(group[4].split(' ')[-1]))
    m_fal.append(int(group[5].split(' ')[-1]))
    m_cnt.append(0)

def program():
    cnt = len(m_invs)
    magic_number = 1 # HACK to compensate for large numbers
    for t in m_div:
        magic_number *= t
    for i in range(10000):
        for idx in range(cnt):
            while m_invs[idx]:
                v = m_invs[idx].pop()
                left = v if m_ops[idx][0] == 'old' else int(m_ops[idx][0])
                right = v if m_ops[idx][2] == 'old' else int(m_ops[idx][2])
                if m_ops[idx][1] == '*':
                    fear =  left * right
                if m_ops[idx][1] == '+':
                    fear = left + right
                fear =  fear % magic_number  # HACK
                if fear % m_div[idx] == 0:
                    m_invs[m_tru[idx]].append(fear)
                else:
                    m_invs[m_fal[idx]].append(fear)
                m_cnt[idx] += 1

        #for idx in range(len(m_invs)):
        #    ivs = [str(x) for x in m_invs[idx]]
        #    vs = ", ".join(ivs)
        #    print(f"Monkey {idx}: {vs}")
        #print("\n")

    m_cnt.sort()
    print(m_cnt[-1]*m_cnt[-2])

cProfile.run('program()')

