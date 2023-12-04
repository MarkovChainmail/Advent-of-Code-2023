import re

def getBox(first, last, line):
    # Get all characters within the bounds and the line
    return line[max([first-1, 0]):min(last+1,len(line))]

# Part A
with open('input.txt') as f:
    lines = f.readlines()

    sum = 0

    for i in range(len(lines)):
        for mtch in re.finditer(r'[0-9]+', lines[i]):
            characters = ""
            first, last = mtch.span()
            
            # Get all characters in a box around the number
            if i != 0:
                characters += getBox(first, last, lines[i-1])
            if i != len(lines)-1:
                characters += getBox(first, last, lines[i+1])
            characters += getBox(first, last, lines[i])   

            # Check if the box contains any symbols
            if (re.search(r'[^0-9.\n]', characters) != None):
                sum += int(mtch[0])
            
    print(sum)

def isNeighbor(gear, part):
    first, last = part

    return gear >= first - 1 and gear <= last

# Part B
with open('input.txt') as f:
    lines = f.readlines()
        
    sum = 0

    for i in range(len(lines)):
        for mtch in re.finditer(r'\*', lines[i]):
            first, last = mtch.span()

            # Check bounding box around * for 2 separate numbers
            candidates = list(re.finditer(r'[0-9]+', lines[i]))
            if (i != 0):
                candidates += list(re.finditer(r'[0-9]+', lines[i-1]))
            if (i != len(lines)-1):
                candidates += list(re.finditer(r'[0-9]+', lines[i+1]))

            neighbors = [c for c in candidates if isNeighbor(first, c.span())]    

            # If two separate numbers are found, add the gear ratio
            if (len(neighbors) == 2):
                sum += int(neighbors[0][0]) * int(neighbors[1][0])

    print(sum)
