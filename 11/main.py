with open('example.txt') as f:
    raw = [part.strip() for part in f.read().split('\n\n')]


class Monkey:
    all_monkeys = []

    def __init__(self, raw: str) -> None:
        _, items, operation, test, if_true, if_false =\
            [line.strip() for line in raw.split('\n')]

        self.items = [int(n) for n in items[16:].split(', ')]

        match operation[21:].split():
            case ['+', 'old']:
                self.op = lambda item: item + item
            case ['*', 'old']:
                self.op = lambda item: item * item
            case ['+', n]:
                self.op = lambda item: item + int(n)
            case ['*', n]:
                self.op = lambda item: item * int(n)

        self.div = int(test[19:])

        self.if_true = int(if_true[25:])
        self.if_false = int(if_false[26:])

        self.inspected = 0

        self.all_monkeys.append(self)
    
    def update(self, item: int) -> int:
        return self.op(item) // 3;

    def inspect_all(self):
        while self.items:
            item = self.items.pop(0)
            item = self.update(item)
            if item % self.div == 0:
                self.all_monkeys[self.if_true].items.append(item)
            else:
                self.all_monkeys[self.if_false].items.append(item)
            self.inspected += 1

    def __repr__(self) -> str:
        return f'{self.items} {self.div} {self.if_true} {self.if_false}'
        

monkeys = [Monkey(raw_part) for raw_part in raw]
round = 0
while round < 20:
    for m in monkeys:
        m.inspect_all()
    round += 1

inspected = [m.inspected for m in monkeys]
for i in inspected:
    print(i)
inspected = sorted(inspected)
print(inspected[-1] * inspected[-2])
