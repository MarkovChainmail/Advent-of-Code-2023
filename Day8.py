import re
import itertools
from math import lcm

# Part A
with open('input.txt') as f:
    input = f.read().splitlines()
    route = itertools.cycle(input[0])
    network = [re.findall(r'[A-Z]+', line) for line in input[2:]]
    networkmap = {line[0]: (line[1], line[2]) for line in network}

    current = 'AAA'
    steps = 0

    while current != 'ZZZ':
        steps += 1
        step = next(route)
        node = networkmap[current]

        if step == 'L':
            current = node[0]
        else:
            current = node[1]

    print(steps)

# Part B
with open('input.txt') as f:
    input = f.read().splitlines()
    route = itertools.cycle(input[0])
    network = [re.findall(r'[A-Z]+', line) for line in input[2:]]
    networkmap = {line[0]: (line[1], line[2]) for line in network}

    current = [node for node in networkmap if re.match(r'[A-Z]+A', node)]
    steps_to_ending = [0 for node in current]
    steps = 0

    while not all([num != 0 for num in steps_to_ending]):
        steps += 1
        step = next(route)

        current = [networkmap[node][0] if step == 'L' else networkmap[node][1] for node in current]

        for index, node in enumerate(current):
            if steps_to_ending[index] == 0 and re.match(r'[A-Z]+Z', node):
                steps_to_ending[index] = steps

    print(lcm(*steps_to_ending))