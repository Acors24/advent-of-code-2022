with open('input.txt') as f:
    buffer = f.readlines()[0].strip()


def part1():
    for i in range(len(buffer) - 4):
        if len(set(buffer[i:i+4])) == 4:
            break

    return i + 4


def part2():
    for i in range(len(buffer) - 14):
        if len(set(buffer[i:i+14])) == 14:
            break

    return i + 14


print(part2())
