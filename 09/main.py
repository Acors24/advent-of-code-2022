with open('input.txt') as f:
    moves = [line.strip() for line in f.readlines()]

rope = [[0, 0] for _ in range(10)]
visited = {(0, 0)}

# .....
# ...#.
# ..#..
# .#...
# .....
# 
# .....
# ...##
# .....
# .#...
# .....
# 


def move(m: tuple[str, str], rope: list[list[int]], visited: set):
    dir, amount = m
    head = rope[0]
    while amount > 0:
        match dir:
            case 'U':
                head[1] += 1
            case 'D':
                head[1] -= 1
            case 'L':
                head[0] -= 1
            case 'R':
                head[0] += 1
        for i, knot in enumerate(rope[1:]):
            prev = rope[i]
            if (prev[0] - knot[0])**2 + (prev[1] - knot[1])**2 > 2.25:
                if prev[0] - knot[0] in (-2, 2) and prev[1] - knot[1] in (-2, 2):
                    knot[0] += (prev[0] - knot[0]) // 2
                    knot[1] += (prev[1] - knot[1]) // 2
                    visited.add((rope[-1][0], rope[-1][1]))
                    continue
                elif prev[0] - knot[0] in (-2, 2):
                    knot[1] = prev[1]
                elif prev[1] - knot[1] in (-2, 2):
                    knot[0] = prev[0]
                knot[0] += (prev[0] - knot[0]) // 2
                knot[1] += (prev[1] - knot[1]) // 2
                if i == len(rope) - 2:
                    visited.add((rope[-1][0], rope[-1][1]))
        amount -= 1


def print_path(visited: set):
    min_x = min(visited, key=lambda x: x[0])[0]
    max_x = max(visited, key=lambda x: x[0])[0]
    min_y = min(visited, key=lambda x: x[1])[1]
    max_y = max(visited, key=lambda x: x[1])[1]

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in visited:
                print('#', end='')
            else:
                print('.', end='')
        print()


for m in moves:
    m = m.split()
    m = (m[0], int(m[1]))
    move(m, rope, visited)

print(len(visited))
