import math
import re
from collections import defaultdict
import matplotlib.pyplot as plt

filename = ['logfile_25.txt', 'logfile_50.txt', 'logfile_100.txt']

def do_calculation(i):
    file = open(filename[i], "r")
    lines = file.readlines()

    stack = []
    heap = []
    stk_addr_count = defaultdict(int)
    heap_addr_count = defaultdict(int)
    num_stk=0
    num_hp=0

    for line in lines:
        if "stack" in line:
            stack.append(line.split(' ')[-1].strip('\n'))
        else:
            heap.append(line.split(' ')[-1].strip('\n'))

    for i in range(len(stack)):
        match = re.search(r"0x[0-9a-fA-F]+", stack[i])
        if match:
            stack_addr = match.group(0)
            stk_addr_count[stack_addr] += 1
            num_stk += 1
    for i in range(len(heap)):
        match = re.search(r"0x[0-9a-fA-F]+", heap[i])
        if match:
            heap_addr = match.group(0)
            heap_addr_count[heap_addr] += 1
            num_hp += 1

    stk_poss = {stack_addr: count / num_stk for stack_addr, count in stk_addr_count.items()}
    hp_poss = {heap_addr: count / num_hp for heap_addr, count in heap_addr_count.items()}  

    if num_stk > 0:
        entropy_stk = -sum(prob * math.log2(prob) for prob in stk_poss.values())
    else:
        entropy_stk = 0.0

    if num_hp > 0:
        entropy_heap = -sum(prob * math.log2(prob) for prob in hp_poss.values())
    else:
        entropy_heap = 0.0
    file.close()
    return {
        "heap": entropy_heap,
        "stack": entropy_stk
    }
log_25 = do_calculation(0)
log_50 = do_calculation(1)
log_100 = do_calculation(2)

x1 = []
x2 = []
y = [25, 50, 100]

x1.append(log_25["heap"])
x1.append(log_50["heap"])
x1.append(log_100["heap"])
x2.append(log_25["stack"])
x2.append(log_50["stack"])
x2.append(log_100["stack"])

plt.plot(y, x1, label='Heap Entropy')
plt.plot(y, x2, label='Stack Entropy')
plt.title("Entropy of Stack and Heap")
plt.show()
