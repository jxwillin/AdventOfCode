import os
import sys
sys.path.append(os.path.join("..",".."))
from utils import *

import math

groups = group_by_blanks(read_lines("test.txt"))

do_print = False
def toggle_print(s):
    if do_print:
        print(s)

class Monkey:
    def __init__(self, data):
        self.start_items = [ int(x) for x in data[1].split(':')[1].split(',')]
        self.ops = list(filter(lambda item : item != '',data[2].split('=')[1].split(' ')))
        self.cond_div = int(data[3].split(' ')[-1])
        self.cond_true = int(data[4].split(' ')[-1])
        self.cond_false = int(data[5].split(' ')[-1])
        self.inspections = 0

    def eval_item(self, item):
        left = item if self.ops[0] == 'old' else int(self.ops[0])
        right = item if self.ops[2] == 'old' else int(self.ops[2])
        result = 0
        if self.ops[1] == '+':
            result = left + right
            toggle_print(f"\t\tWorry level increases by {right} to {result}.")
        elif self.ops[1] == '*':
            result = left * right
            toggle_print(f"\t\tWorry level is multiplied by {right} to {result}.")
        return result


    def step(self, monkey_count):
        results = dict()
        for i in range(monkey_count):
            results[i] = []
        for item in self.start_items:
            self.inspections += 1
            toggle_print(f"\tMonkey inspects an item with a worry level of {item}.")
            value = self.eval_item(item)
            #toggle_print(f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {value//3}.")
            #value = value // 3
            if value % self.cond_div == 0:
                toggle_print(f"\t\tCurrent worry level is divisible by {self.cond_div}.")
                toggle_print(f"\t\tItem with worry level {value} is thrown to monkey {self.cond_true}.")
                results[self.cond_true].append(value)
            else:
                toggle_print(f"\t\tCurrent worry level is not divisible by {self.cond_div}.")
                results[self.cond_false].append(value)
                toggle_print(f"\t\tItem with worry level {value} is thrown to monkey {self.cond_false}.")
        self.start_items = []
        return results


monkies = []
for group in groups:
    monkies.append(Monkey(group))
    print(monkies[-1].start_items)
    print(monkies[-1].ops)
    print(monkies[-1].cond_div)
    print(monkies[-1].cond_true)
    print(monkies[-1].cond_false)

monkey_count = len(monkies)
for i in range(10000):
    for idx, monkey in enumerate(monkies):
        toggle_print(f"Monkey {idx}:")
        actions = monkey.step(monkey_count)
        for key in actions.keys():
            monkies[key].start_items.extend(actions[key])

inspections = [x.inspections for x in monkies]
inspections.sort()
print(inspections[-1]*inspections[-2])

