# Part A
def getNextLine(line):
    return [line[i+1] - line[i] for i in range(len(line)-1)]

def getNextValue(line):
    if all(n==0 for n in line):
        return 0
    else:
        return getNextValue(getNextLine(line)) + line[-1]

with open('input.txt') as f:
    input = [[int(n) for n in line.split(" ")] for line in f.read().splitlines()]

    print(sum(getNextValue(line) for line in input))

# Part B
def getNextValueHistory(line):
    if all(n==0 for n in line):
        return 0
    else:
        return line[0] - getNextValueHistory(getNextLine(line))

with open('input.txt') as f:
    input = [[int(n) for n in line.split(" ")] for line in f.read().splitlines()]

    print(sum(getNextValueHistory(line) for line in input))
