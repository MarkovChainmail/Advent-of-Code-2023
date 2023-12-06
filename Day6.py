import re

with open('input.txt') as f:
    lines = f.readlines()
    times = [int(s) for s in re.split(r'\s+', lines[0]) if s.isdigit()]
    distances = [int(s) for s in re.split(r'\s+', lines[1]) if s.isdigit()]

    total = 1
    for i in range(len(times)):
        wins = 0
        for t in range(1, times[i]):
            if t * (times[i]-t) > distances[i]:
                wins += 1

        total = total * wins

    print(total)

with open('input.txt') as f:
    lines = f.readlines()
    time = int("".join([s for s in lines[0] if s.isdigit()]))
    distance = int("".join([s for s in lines[1] if s.isdigit()]))

    for t in range(1, time):
        if t * (time-t) > distance:
            print(time - 2 * t + 1)
            break
