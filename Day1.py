import re

# Part A
with open('input.txt') as f:
    numbers = [re.findall('[0-9]', l) for l in f.readlines()]
    print(sum(int(a[0] + a[-1]) for a in numbers))

# Part B
with open('input.txt') as f:
    l = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    numbers = [re.findall('[0-9]|one|two|three|four|five|six|seven|eight|nine', l) for l in f.readlines()]
    numbers2 = [int((l[a[0]] if a[0] in l else a[0]) + (l[a[-1]] if a[-1] in l else a[-1])) for a in numbers]

    print(sum(numbers2))
