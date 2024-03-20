with open('input.txt') as f:
    pattern = f.read().strip()

rocks = [
    [
        '####'
    ],
    [
        '.#.',
        '###',
        '.#.'
    ],
    [
        '..#',
        '..#',
        '###'
    ],
    [
        '#',
        '#',
        '#',
        '#'
    ],
    [
        '##',
        '##'
    ]
]

top_height = 0
rock_index = 0
move_index = 0
stopped = []


def drop():
    global rock_index, move_index, top_height, stopped
    turn = 1 # 1 - jet; -1 - fall
    rock = rocks[rock_index]
    rock_index = (rock_index + 1) % len(rocks)
    x, y = 2, top_height - 3 - len(rock)

    while True:
        # rock_p = []
        # for ry, row in enumerate(rock):
        #     for rx, col in enumerate(row):
        #         if col == '#':
        #             rock_p.append((x + rx, y + ry))

        # for py in range(-10, 0):
        #     for px in range(7):
        #         if (px, py) in stopped:
        #             print('#', end='')
        #         elif (px, py) in rock_p:
        #             print('@', end='')
        #         else:
        #             print('.', end='')
        #     print()
        # print('='*7)

        ok = True
        if turn == 1:
            move = pattern[move_index]
            move_index = (move_index + 1) % len(pattern)
            dx = -1 if move == '<' else 1
            for ry, row in enumerate(rock):
                for rx, col in enumerate(row):
                    new_x = x + rx + dx
                    new_y = y + ry
                    if col == '#' and (not 0 <= new_x < 7 or (new_x, new_y) in stopped):
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                x += dx
        else:
            for ry, row in enumerate(rock):
                for rx, col in enumerate(row):
                    new_x = x + rx
                    new_y = y + ry + 1
                    if col == '#' and (new_y >= 0 or (new_x, new_y) in stopped):
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break

            y += 1

        turn *= -1
    
    for sy in range(y, y + len(rock)):
        for sx in range(x, x + len(rock[0])):
            if rock[sy - y][sx - x] == '#':
                stopped.append((sx, sy))
                if sy < top_height:
                    top_height = sy
    
    stopped = stopped[-100:]
    

amount = 1_000_000_000_000
while amount > 0:
    drop()
    amount -= 1

    # for y in range(-20, 0):
    #     for x in range(7):
    #         if (x, y) in stopped:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
    # print('=' * 7)

print(abs(top_height))
