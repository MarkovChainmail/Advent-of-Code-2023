def getMap(input):
    return [[int(n) for n in line.split(" ") if n != ""] for line in input.split("\n")[1:]]

def useMap(source, map):
    for line in map:
        if line != [] and source >= line[1] and source < line[1] + line[2]:
            return line[0] + source - line[1]
    
    return source

# Part A
with open('input.txt') as f:
    data = f.read().split("\n\n")

    current = [int(n) for n in data[0].split(" ")[1:]]
    maps = [getMap(line) for line in data[1:]]
    
    # Go through all the maps and update the current value
    for map in maps:
        current = [useMap(n, map) for n in current]

    print(min(current))

# Part B
# def useMapRanges(rng, map):
#     # Use map but on a range of numbers
#     newranges = []
#     for line in map:
#         # If the mapping contains any of the numbers in this range
#         if rng[0] >= line[1] and rng[0] + rng[1] < line[1] + line[2]:
#             newranges.append()

# def getMapRanges(line):
    

# with open('input.txt') as f:
#     data = f.read().split("\n\n")

#     ranges = [int(n) for n in data[0].split(" ")[1:]]
#     ranges = [range(ranges[i*2], ranges[i*2+1]) for i in range(int(len(ranges)/2))]
#     maps = [getMap(line) for line in data[1:]]

    
#     print(ranges)
