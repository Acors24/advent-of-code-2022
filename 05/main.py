import re
from copy import deepcopy

with open('input.txt') as f:
    crates, steps = f.read().split('\n\n')

stacks = []
for _ in range((len(crates.split('\n')[0]) + 1) // 4):
    stacks.append([])

for row in crates.split('\n')[-2::-1]:
    res = re.finditer(r'[A-Z]', row)
    for r in res:
        i = (r.span()[0] - 1) // 4
        stacks[i].append(r.group())

r = re.compile(r'move (?P<amount>\d+) from (?P<from>\d+) to (?P<to>\d+)')


def part1():
    local_stacks = deepcopy(stacks)
    for step in steps.split('\n'):
        amount, from_, to = map(lambda x: int(x), r.findall(step)[0])
        from_, to = from_ - 1, to - 1
        for _ in range(amount):
            local_stacks[to].append(local_stacks[from_].pop())

    for stack in local_stacks:
        print(stack[-1], end='')
    print()


def part2():
    local_stacks = deepcopy(stacks)
    for step in steps.split('\n'):
        amount, from_, to = map(lambda x: int(x), r.findall(step)[0])
        from_, to = from_ - 1, to - 1
        moved = local_stacks[from_][-amount:]
        for _ in range(amount):
            local_stacks[from_].pop()
        local_stacks[to].extend(moved)

    for stack in local_stacks:
        print(stack[-1], end='')
    print()


part1()
part2()
