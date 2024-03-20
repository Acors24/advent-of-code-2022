from queue import Queue
from math import inf


def find_moves(pos: tuple[int, int], map: list[str], seen: set):
    x, y = pos
    moves = []
    available = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    for i, j in available:
        if i < 0 or i >= len(map[0]) or j < 0 or j >= len(map):
            continue
        if (i, j) in seen or ord(map[j][i]) > ord(map[y][x]) + 1:
            continue
        if map[j][i] == 'E' and ord(map[y][x]) < ord('y'):
            continue
        moves.append((i, j))
        seen.add((i, j))
    
    return moves


def move(pos: tuple[int, int], map: list[str]):
    seen = {pos}
    q = Queue()
    qsize = 0
    steps = 0

    while True:
        x, y = pos
        if map[y][x] == 'E':
            return steps

        for m in find_moves(pos, map, seen):
            q.put((m, steps + 1))
            qsize += 1

        if qsize != 0:
            pos, steps = q.get(timeout=0.2)
            qsize -= 1
        else:
            return inf


with open('input.txt') as f:
    map = [line.strip() for line in f.readlines()]

start = None
for y, row in enumerate(map):
    for x, square in enumerate(row):
        if square == 'S':
            start = (x, y)
            map[y] = 'a' + map[y][1:]
        if start: break
    if start: break


def part1():
    print(move(start, map))


def part2():
    lowest = inf
    for y, row in enumerate(map):
        for x, square in enumerate(row):
            if square == 'a':
                moves = move((x, y), map)
                if moves < lowest:
                    lowest = moves
    
    print(lowest)


part2()
