import re
from math import inf


class Sensor:
    pattern = re.compile(r'Sensor at x=(?P<s_x>-?\d*), y=(?P<s_y>-?\d*): closest beacon is at x=(?P<b_x>-?\d*), y=(?P<b_y>-?\d*)')
    min_x, max_x = inf, -inf

    def __init__(self, raw) -> None:
        res = self.pattern.match(raw)
        if not res:
            raise ValueError

        x, y = int(res.group('s_x')), int(res.group('s_y'))
        bx, by = int(res.group('b_x')), int(res.group('b_y'))
        self.pos = (x, y)
        self.beacon_pos = (bx, by)
        self.distance = abs(x - bx) + abs(y - by)

        if x - self.distance < Sensor.min_x: Sensor.min_x = x - self.distance
        if x + self.distance > Sensor.max_x: Sensor.max_x = x + self.distance

    def __repr__(self) -> str:
        x, y = self.pos
        bx, by = self.beacon_pos
        return f'({x}, {y}) ({bx}, {by})'


with open('input.txt') as f:
    raw = [line.strip() for line in f.readlines()]


sensors = [Sensor(line) for line in raw]


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def part1():
    y = 2_000_000
    unavailable = set()
    bxs = set()
    useful_sensors = [s for s in sensors if abs(s.pos[1] - y) <= s.distance]
    for x in range(Sensor.min_x, Sensor.max_x + 1):
        for s in useful_sensors:
            sx, sy = s.pos
            bx, by = s.beacon_pos
            if y == by and x == bx:
                bxs.add(bx)
                break
            if x not in bxs and dist(x, y, sx, sy) <= s.distance:
                unavailable.add(x)
                break

    print(len(unavailable))


def check(x: int, y: int, sensors: list[Sensor], max: int):
    if not (0 <= x <= max) or not (0 <= y <= max):
    	return False
    	
    for s in sensors:
    	sx, sy = s.pos
    	if dist(x, y, sx, sy) <= s.distance:
    		return False
    		
    return True
		

def part2():
    for s in sensors:
        max = 4_000_000
        sx, sy = s.pos
        for d in range(s.distance + 1): # top-right
            x = sx + d
            y = sy - (s.distance + 1) + d
            if check(x, y, sensors, max):
            	print(x * 4_000_000 + y)
            	return
        for d in range(s.distance + 1): # bottom-right
            x = sx + (s.distance + 1) - d
            y = sy + d
            if check(x, y, sensors, max):
            	print(x * 4_000_000 + y)
            	return
        for d in range(s.distance + 1): # bottom left
            x = sx - d
            y = sy + (s.distance + 1) - d
            if check(x, y, sensors, max):
            	print(x * 4_000_000 + y)
            	return
        for d in range(s.distance + 1): # top left
            x = sx - (s.distance + 1) + d
            y = sy - d
            if check(x, y, sensors, max):
            	print(x * 4_000_000 + y)
            	return

    print('????')


part2()
