with open('input.txt') as f:
    rounds = [line.strip() for line in f.readlines()]


def part1():
    total_score = 0
    values = {
        'A': 1, # W 1 1 1 mod 3 = 1
        'B': 2, # D 0 0 0 mod 3 = 0
        'C': 3, # L 2 2 2 mod 3 = 2
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    results = [3, 6, 0]
    for round in rounds:
        op, me = round.split()
        total_score += values[me]
        result = (values[me] - values[op]) % 3
        total_score += results[result]

    return total_score


def part2():
    total_score = 0
    values = {
        'A': 0,
        'B': 1,
        'C': 2,
        'X': -1,
        'Y': 0,
        'Z': 1
    }
    results = [3, 6, 0]
    for round in rounds:
        op, res = round.split()
        v = values[res]
        total_score += (v + 1) * 3 + ((values[op] + v) % 3) + 1

    return total_score


print(part2())
