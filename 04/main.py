with open('input.txt') as f:
    pairs = [line.strip().split(',') for line in f.readlines()]


def part1():
    amount = 0
    for pair in pairs:
        startA, endA = pair[0].split('-')
        startB, endB = pair[1].split('-')
        if (int(startA) >= int(startB) and int(endA) <= int(endB)) \
            or (int(startA) <= int(startB) and int(endA) >= int(endB)):
            amount += 1

    return amount


def part2():
    amount = 0
    for pair in pairs:
        startA, endA = pair[0].split('-')
        startB, endB = pair[1].split('-')
        if int(startA) >= int(startB) and int(startA) <= int(endB) \
            or int(startB) >= int(startA) and int(startB) <= int(endA):
            amount += 1

    return amount


print(part2())
