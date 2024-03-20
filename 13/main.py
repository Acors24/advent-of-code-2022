from pprint import pprint


with open('input.txt') as f:
    pairs = [pair.strip().split() for pair in f.read().split('\n\n')]


def find_seps(string: str):
    open = 0
    indices = []
    for i, char in enumerate(string):
        if char == '[':
            open += 1
        elif char == ']':
            open -= 1
        elif char == ',' and open == 0:
            indices.append(i)
    
    return indices


def parse_string(string: str):
    if string[0] == '[':
        string = string[1:-1]
    else:
        return int(string)

    if string == '':
        return []

    if '[' not in string:
        return [int(x) for x in string.split(',')]

    content = []
    seps = [-1] + find_seps(string) + [len(string)]
    for i in range(1, len(seps)):
        a, b = seps[i - 1] + 1, seps[i]
        content.append(parse_string(string[a:b]))
    
    return content


def parse(lst: list[list[str]]) -> list[tuple[list, list]]:
    for i, pair in enumerate(lst):
        l, r = pair
        lst[i] = parse_string(l), parse_string(r)


def check(pair: tuple) -> bool:
    i = 0
    p1, p2 = pair
    for l, r in zip(p1, p2):
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            if l > r:
                return False
        elif isinstance(l, list) and isinstance(r, list):
            result = check((l, r))
            if result is not None:
                return result
        else:
            if isinstance(l, int):
                l = [l]
            elif isinstance(r, int):
                r = [r]
            result = check((l, r))
            if result is not None:
                return result
        
        i += 1

    if i == len(p1) == len(p2):
        return None
    elif i == len(p1) and i <= len(p2):
        return True
    else:
        return False



parse(pairs)


def part1():
    sum = 0
    for i, p in enumerate(pairs):
        result = check(p)
        if result or result is None:
            pprint(p)
            sum += i + 1

    print(sum)


def part2():
    packets = []
    for l, r in pairs:
        packets.append(l)
        packets.append(r)
    
    packets.append([[2]])
    packets.append([[6]])

    for i in range(len(packets) - 1):
        for j in range(1, len(packets) - i):
            if not check((packets[j - 1], packets[j])):
                packets[j - 1], packets[j] = packets[j], packets[j - 1]

    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


part2()
