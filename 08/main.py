with open('input.txt') as f:
    grid = [line.strip() for line in f.readlines()]

for row in grid[:5]:
    print(row)


def is_visible(x: int, y: int, grid: list[str]) -> bool:
    tree = int(grid[y][x])
    top, bottom, left, right = [True] * 4
    for i in range(y - 1, -1, -1):
        if int(grid[i][x]) >= tree:
            top = False
            break
    for i in range(y + 1, len(grid)):
        if int(grid[i][x]) >= tree:
            bottom = False
            break
    for i in range(x - 1, -1, -1):
        if int(grid[y][i]) >= tree:
            left = False
            break
    for i in range(x + 1, len(grid[0])):
        if int(grid[y][i]) >= tree:
            right = False
            break

    return any([top, bottom, left, right])

def part1():
    amount = 2 * len(grid) + 2 * (len(grid[0]) - 2)
    for y, row in enumerate(grid[1:-1]):
        for x, tree in enumerate(row[1:-1]):
            amount += 1 if is_visible(x + 1, y + 1, grid) else 0

    return amount


def get_score(x: int, y: int, grid: list[str]) -> int:
    tree = int(grid[y][x])
    top, bottom, left, right = [0] * 4
    for i in range(y - 1, -1, -1):
        if int(grid[i][x]) < tree:
            top += 1
        else:
            top += 1
            break
    for i in range(y + 1, len(grid)):
        if int(grid[i][x]) < tree:
            bottom += 1
        else:
            bottom += 1
            break
    for i in range(x - 1, -1, -1):
        if int(grid[y][i]) < tree:
            left += 1
        else:
            left += 1
            break
    for i in range(x + 1, len(grid[0])):
        if int(grid[y][i]) < tree:
            right += 1
        else:
            right += 1
            break

    return top * bottom * left * right


def part2():
    best = 0
    for y, row in enumerate(grid[1:-1]):
        for x, tree in enumerate(row[1:-1]):
            if (res := get_score(x + 1, y + 1, grid)) > best:
                best = res

    return best


print(part2())
