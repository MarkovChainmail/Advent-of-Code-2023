import re

# Part A
with open('input.txt') as f:
    parts = [re.split(r'[:|]', line) for line in f.readlines()]
    intersection = [set(re.findall(r'[0-9]+', p[1])).intersection(set(re.findall(r'[0-9]+', p[2]))) for p in parts]
    points = sum([0 if len(s) == 0 else 2**(len(s)-1) for s in intersection])

    print(points)

# Part B
with open('input.txt') as f:
    parts = [re.split(r'[:|]', line) for line in f.readlines()]
    intersection = [len(set(re.findall(r'[0-9]+', p[1])).intersection(set(re.findall(r'[0-9]+', p[2])))) for p in parts]
    
    cards = {i: 1 for i in range(len(intersection))}

    for i in range(len(intersection)): 
        for j in range(i+1, i+1+intersection[i]): 
            if j in cards:
                cards[j] = cards[j]+cards[i]
    
    print(sum(cards.values()))