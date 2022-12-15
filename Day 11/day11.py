"""
Advent of Code 2022
Day   11
"""


class Monkey:
    def __init__(self, index: int, items: list[int],
                 operation: list[str, int | str],
                 divisor: int, test_map: dict):
        self.index = index
        self.items = items
        self.op = operation
        self.divisor = divisor
        self.test = test_map
        self.inspected: int = 0

    def __repr__(self) -> str:
        return f'#{self.index} 🐒'


class MonkeyHorde:
    def __init__(self, filename: str):
        self.monkeys: list = []
        self._parse(filename)
        self.mod_product = self._calc_product()

    def _parse(self, filename):
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

            raw_index = lines[0::7]
            indeces = [int(i[7::].rstrip(':')) for i in raw_index]

            raw_items = lines[1::7]
            items: list = []
            for itm in raw_items:
                itm = itm[16::].replace(' ', '').split(',')
                itm = list(map(int, itm))
                items.append(itm)

            raw_op = lines[2::7]
            op_lst: list = []
            for op in raw_op:
                op = op[21::].split(' ')
                op = [int(o) if o.isdigit() else o for o in op]
                op_lst.append(op)

            raw_divisor = lines[3::7]
            divisor_lst: list = []
            for div in raw_divisor:
                div = div[19::]
                divisor_lst.append(div)
            divisor_lst = list(map(int, divisor_lst))

            test: list = []
            raw_test_true = lines[4::7]
            raw_test_false = lines[5::7]
            for idx, t_test in enumerate(raw_test_true):
                t_test = int(t_test[25::])
                f_test = int(raw_test_false[idx][26::])
                test_dict = {True: t_test, False: f_test}
                test.append(test_dict)

            for i, m in enumerate(indeces):
                self.monkeys.append(
                    Monkey(
                        indeces[i], items[i], op_lst[i],
                        divisor_lst[i], test[i])
                )

    def _calc_worry(self, item_lvl: int, op_lst: list) -> int():
        op, val = op_lst
        if val == "old":
            val = item_lvl
        match op:
            case '+':
                return item_lvl + val
            case '-':
                return item_lvl - val
            case '*':
                return item_lvl * val

    def _calc_product(self) -> int:
        product = 1
        for mon in self.monkeys:
            product *= mon.divisor
        return product

    def is_congruent(self, worry: int) -> bool:
        return worry % self.mod_product == 0

    def is_devisable(self, worry: int, divisor: int) -> bool:
        return worry % divisor == 0

    def throw_items_1(self):
        for _ in range(20):
            for m in self.monkeys:
                for idx, item in enumerate(m.items):
                    worry = self._calc_worry(item, m.op)
                    bored_worry = worry // 3
                    div_chk = self.is_devisable(bored_worry, m.divisor)
                    target = m.test[div_chk]
                    self.monkeys[target].items.append(bored_worry)
                    m.inspected += 1

                    if idx == len(m.items) - 1:
                        m.items = []

    def throw_items_2(self):
        for _ in range(10_000):
            for m in self.monkeys:
                for idx, item in enumerate(m.items):
                    worry = self._calc_worry(item, m.op)
                    div_chk = self.is_congruent(worry)
                    target = m.test[div_chk]
                    self.monkeys[target].items.append(worry)
                    m.inspected += 1

                    if idx == len(m.items) - 1:
                        m.items = []


def calc_product(*args):
    product = 1
    for arg in args:
        product *= arg
    return product


def part_one(filename: str):
    part_1 = MonkeyHorde(filename)
    part_1.throw_items_1()

    buisiness_1: list = []
    for mon in part_1.monkeys:
        buisiness_1.append(mon.inspected)
    buisiness_1.sort(reverse=True)
    buisiness_1 = buisiness_1[:2]
    print(calc_product(*buisiness_1))


def part_two(filename: str):
    part_2 = MonkeyHorde(filename)
    part_2.throw_items_2()
    buisiness_2:  list = []
    for mon in part_2.monkeys:
        buisiness_2.append(mon.inspected)
    buisiness_2.sort(reverse=True)
    buisiness_2 = buisiness_2[:2]
    print(calc_product(*buisiness_2))


def main():
    part_one('day11_input.txt')
    part_two('example1.txt')


if __name__ == '__main__':
    main()
