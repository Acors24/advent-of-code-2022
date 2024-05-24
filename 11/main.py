class Monkey:
    all_monkeys: list["Monkey"] = []
    divisor = 3
    M = 1

    def __init__(self, raw: str, divisor: int = 3):
        _, items, operation, test, if_true, if_false = [
            line.strip() for line in raw.split("\n")
        ]

        self.items = [int(n) for n in items[16:].split(", ")]

        self.div = int(test[19:])
        Monkey.M *= self.div
        Monkey.divisor = divisor

        match operation[21:].split():
            case ["+", "old"]:
                self.op = lambda item: (2 * item)
            case ["*", "old"]:
                self.op = lambda item: (item * item)
            case ["+", n]:
                self.op = lambda item: (item + int(n))
            case ["*", n]:
                self.op = lambda item: (item * int(n))

        self.if_true = int(if_true[25:])
        self.if_false = int(if_false[26:])

        self.inspected = 0

        Monkey.all_monkeys.append(self)

    def update(self, item: int) -> int:
        if Monkey.divisor == 3:
            return self.op(item) // Monkey.divisor
        else:
            return self.op(item) % Monkey.M // Monkey.divisor

    def inspect_all(self):
        while self.items:
            item = self.items.pop(0)
            item = self.update(item)
            if item % self.div == 0:
                Monkey.all_monkeys[self.if_true].items.append(item)
            else:
                Monkey.all_monkeys[self.if_false].items.append(item)
            self.inspected += 1

    def __repr__(self) -> str:
        return f"{self.items} {self.div} {self.if_true} {self.if_false}"


with open("input.txt") as f:
    raw = [part.strip() for part in f.read().split("\n\n")]


def go(rounds: int, divisor: int):
    for raw_part in raw:
        Monkey(raw_part, divisor)
        
    _round = 0
    while _round < rounds:
        for m in Monkey.all_monkeys:
            m.inspect_all()
        _round += 1

    inspected = [m.inspected for m in Monkey.all_monkeys]
    inspected = sorted(inspected)
    
    Monkey.all_monkeys.clear()
    return inspected[-1] * inspected[-2]


def part1():
    return go(20, 3)


def part2():
    return go(10000, 1)


if __name__ == "__main__":
    print(part1())
    print(part2())
