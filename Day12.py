def combinations(numbers, spare, buffer):
    if len(numbers) == 0:
        return [spare * "."]
    
    out = []
    for i in range(buffer, spare+1):
        tails = combinations(numbers[1:], spare - i, 1)
        for t in tails:
            out.append(i * "." + numbers[0] * "#" + t)
    return out

def is_possible(candidate, template):
    return all([a == b or b == "?" for a, b in zip(candidate, template)])

# Part A
with open('input.txt') as f:
    input = f.read().splitlines()

    total = 0

    for line in input:
        left, right = line.split(" ")

        numbers = [int(n) for n in right.split(",")]
        spare = len(left) - sum(numbers)

        # every combination of spare n spare n spare n spare
        total += len([candidate for candidate in combinations(numbers, spare, 0) if is_possible(candidate, left)])

    print(total)

# Part B
# with open('input.txt') as f:
#     input = f.read().splitlines()

#     total = 0

#     for line in input:
#         left, right = line.split(" ")

#         numbers = 5 * [int(n) for n in right.split(",")]
#         left = "?".join(5 * [left])
#         spare = len(left) - sum(numbers)

#         # every combination of spare n spare n spare n spare
#         total += len([candidate for candidate in combinations(numbers, spare, 0) if is_possible(candidate, left)])

#     print(total)

