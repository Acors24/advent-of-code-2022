with open('input.txt') as f:
    sacks = [line.strip() for line in f.readlines()]

def get_priority(type):
    v = ord(type) - ord('a') + 1
    if v < 1:
        v = ord(type) - ord('A') + 27

    return v


def part1():
    priority_sum = 0
    for sack in sacks:
        l = len(sack) // 2
        common = set(sack[:l]) & set(sack[l:])
        priority_sum += get_priority(common.pop())

    return priority_sum


def part2():
    priority_sum = 0
    for i in range(len(sacks) // 3):
        a, b, c = sacks[i*3:(i+1)*3]
        common = set(a) & set(b) & set(c)
        priority_sum += get_priority(common.pop())

    return priority_sum


print(part2())
