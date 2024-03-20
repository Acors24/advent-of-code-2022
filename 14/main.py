from math import inf

with open('input.txt') as f:
    paths = [line.strip().split(' -> ') for line in f.readlines()]

min_x, max_x = inf, -inf
min_y, max_y =   0, -inf

for path in paths:
    for i, pos in enumerate(path):
        x, y = pos.split(',')
        x, y = int(x), int(y)
        path[i] = (x, y)
        if x < min_x: min_x = x
        if x > max_x: max_x = x
        if y < min_y: min_y = y
        if y > max_y: max_y = y

cells = set()

for path in paths:
    for i in range(len(path) - 1):
        pos1, pos2 = path[i], path[i+1]
        x1, y1 = pos1
        x2, y2 = pos2
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                cells.add((x, y))


def drop(cells: set, min_x: int, max_x: int, max_y: int) -> bool:
    x, y = 500, 0

    if (x, y) in cells:
        return False
        
    while True:
        if not (out := y + 1 > max_y) and (x, y + 1) not in cells:
            x, y = x, y + 1
        elif not out and not (out := x - 1 < min_x) and (x - 1, y + 1) not in cells:
            x, y = x - 1, y + 1
        elif not out and not (out := x + 1 > max_x) and (x + 1, y + 1) not in cells:
            x, y = x + 1, y + 1
        elif out:
            return False
        else:
            break

    cells.add((x, y))
    return True


def part1():
    units = 0

    while drop(cells, min_x, max_x, max_y):
        units += 1

    print(units)


def drop2(cells: set, max_y: int) -> bool:
    x, y = 500, 0

    if (x, y) in cells:
        return False
        
    while True:
        if y + 1 == max_y + 2:
            break

        if (x, y + 1) not in cells:
            x, y = x, y + 1
        elif (x - 1, y + 1) not in cells:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in cells:
            x, y = x + 1, y + 1
        else:
            break

    cells.add((x, y))
    return True


def part2():
    units = 0
    
    while drop2(cells, max_y):
        units += 1

    print(units)


part2()
