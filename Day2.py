import re

def getMax(line, color):
    return max(map(lambda tup: int(tup[0]), filter(lambda tup: tup[1] == color, line)))

# Part A
with open('input.txt') as f:
    numbers = [list(map(lambda s: s.split(" "), re.findall('\d+ [red|blue|green]', l))) for l in f.readlines()]
    dicts = [{'r': getMax(game, 'r'), 'b': getMax(game, 'b'), 'g': getMax(game, 'g')} for game in numbers]
    filtered = filter(lambda tup: tup[1]['r'] <= 12 and tup[1]['b'] <= 14 and tup[1]['g'] <= 13, enumerate(dicts))
    
    print(sum(map(lambda x: x[0]+1, filtered)))

# Part B    
with open('input.txt') as f:
    numbers = [list(map(lambda s: s.split(" "), re.findall('\d+ [red|blue|green]', l))) for l in f.readlines()]
    dicts = [{'r': getMax(game, 'r'), 'b': getMax(game, 'b'), 'g': getMax(game, 'g')} for game in numbers]
    print(sum(map(lambda x: x['r']*x['b']*x['g'], dicts)))