from collections import Counter
from functools import cmp_to_key

# Part A
order = "AKQJT98765432"

def getType(s):
    counts = Counter(s).most_common()

    if counts[0][1] == 5:
        return 0 # Five of a kind
    elif counts[0][1] == 4:
        return 1 # Four of a kind
    elif counts[0][1] == 3:
        if counts[1][1] == 2:
            return 2 # Full house
        else:
            return 3 # Three of a kiind
    elif counts[0][1] == 2:
        if counts[1][1] == 2:
            return 4 # Two pair
        else:
            return 5 # One pair
    else:
        return 6 # High card        

class HandComparator(tuple):
    def __lt__(self, other):
        typeA = getType(self[0])
        typeB = getType(other[0])

        if typeA < typeB:
            return 1
        elif typeB < typeA:
            return -1
        else:
            for pos in range(len(self[0])):
                posA = order.find(self[0][pos])
                posB = order.find(other[0][pos])

                if posA < posB:
                    return 1
                elif posB < posA:
                    return -1

with open('input.txt') as f:
    hands = [line.split(" ") for line in f.readlines()]
    sort = sorted(hands, key=cmp_to_key(HandComparator.__lt__))
    print(sum([(pos+1) * int(hand[1]) for pos, hand in enumerate(sort)]))


# Part B
order = "AKQT98765432J"

def getTypeScore(counts):
    if counts[0][1] == 5:
            return 0 # Five of a kind
    elif counts[0][1] == 4:
            return 1 # Four of a kind
    elif counts[0][1] == 3:
            if counts[1][1] == 2:
                return 2 # Full house
            else:
                return 3 # Three of a kiind
    elif counts[0][1] == 2:
            if counts[1][1] == 2:
                return 4 # Two pair
            else:
                return 5 # One pair
    else:
            return 6 # High card 
    
def getTypeWithJoker(s):
    ctr = Counter(s)
    
    # If there are jokers, replace them with the most-occurring
    if 'J' not in ctr:
        return getTypeScore(ctr.most_common())
    else:
        highest = 6
        for replacement in order:
            replaced = s.replace("J", replacement)
            score = getTypeScore(Counter(replaced).most_common())

            if score < highest:
                 highest = score
        return highest
    
class HandComparatorWithJoker(tuple):
    def __lt__(self, other):
        typeA = getTypeWithJoker(self[0])
        typeB = getTypeWithJoker(other[0])

        if typeA < typeB:
            return 1
        elif typeB < typeA:
            return -1
        else:
            for pos in range(len(self[0])):
                posA = order.find(self[0][pos])
                posB = order.find(other[0][pos])

                if posA < posB:
                    return 1
                elif posB < posA:
                    return -1
                
with open('input.txt') as f:
    hands = [line.split(" ") for line in f.readlines()]
    sort = sorted(hands, key=cmp_to_key(HandComparatorWithJoker.__lt__))
    print(sum([(pos+1) * int(hand[1]) for pos, hand in enumerate(sort)]))
