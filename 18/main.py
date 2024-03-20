from math import inf
from queue import Queue

lava_cubes = []
minx, maxx, miny, maxy, minz, maxz = [inf, -inf] * 3
with open('input.txt') as f:
    while (line := f.readline()):
        t = tuple(map(int, line.strip().split(',')))
        x, y, z = t
        minx = min(minx, x - 1); maxx = max(maxx, x + 1)
        miny = min(miny, y - 1); maxy = max(maxy, y + 1)
        minz = min(minz, z - 1); maxz = max(maxz, z + 1)
        lava_cubes.append(t)


def adjacent(c1: tuple, c2: tuple) -> bool:
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    dx, dy, dz = abs(x1 - x2), abs(y1 - y2), abs(z1 - z2)
    return sorted([dx, dy, dz]) == [0, 0, 1]


total = len(lava_cubes) * 6
for c1 in lava_cubes:
    for c2 in lava_cubes:
        if c1 is not c2 and adjacent(c1, c2):
            total -= 1

air_cubes = [(x, y, z) for x in range(minx, maxx + 1) for y in range(miny, maxy + 1) for z in range(minz, maxz + 1) if (x, y, z) not in lava_cubes]


def flood(start: tuple):
    q = Queue()
    q.put(start)
    while not q.empty():
        current = q.get()
        for air in air_cubes:
            if adjacent(current, air):
                q.put(air)
                air_cubes.remove(air)


flood((minx, miny, minz))

for air in air_cubes:
    t = 0
    for lava in lava_cubes:
        if adjacent(air, lava):
            t += 1
    total -= t

print(total)
