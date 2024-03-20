with open('input.txt') as f:
    data = ''.join(f.readlines()).split('\n\n')

top = []
for line in data:
    s = sum(map(int, line.split()))
    if len(top) < 3:
        top.append(s)
        continue

    for i, t in enumerate(top):
        if s > t and t == min(top):
            top[i] = s
            break

print(sum(top))
