"""
Advent of Code 2022
Day     11
Part     1
"""

from dataclasses import dataclass
from tabulate import tabulate


@dataclass
class Monkey:
    items: list
    operation: list
    divisor: int
    test_map: dict
    inspections: int = 0


class MonkeyHerd:
    def __init__(self, filename: str):
        self.herd: list = []
        self._parse_input(filename)

    def _parse_input(self, filename: str):
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

            # collect item lists
            items_lst = []
            raw_items = lines[1::7]
            for items in raw_items:
                items = items[16:].replace(' ', '').split(',')
                items = list(map(int, items))
                items_lst.append(items)

            # collect operations
            op_lst = []
            raw_op = lines[2::7]
            for operation in raw_op:
                operation = operation[21:].split(' ')
                operation = [int(op) if op.isdigit() else op
                             for op in operation]
                op_lst.append(operation)

            raw_div = lines[3::7]
            divisor_lst = [int(div[19:]) for div in raw_div]

            # get test map
            test_map_lst = []
            raw_true = lines[4::7]
            raw_false = lines[5::7]
            true_lst = [int(t[25:]) for t in raw_true]
            false_lst = [int(f[26:]) for f in raw_false]
            for idx, true in enumerate(true_lst):
                test_map_lst.append({True: true, False: false_lst[idx]})

            for i, _ in enumerate(items_lst):
                self.herd.append(
                    Monkey(
                        items_lst[i],
                        op_lst[i],
                        divisor_lst[i],
                        test_map_lst[i]
                    )
                )

    def get_interactions(self):
        interacts = []
        for monkey in self.herd:
            interacts.append(monkey.inspections)
        return interacts

    def calculate_worry(self, current: int, operation: list) -> int:
        op, val = operation
        if val == "old":
            val = current
        match op:
            case '+':
                return (current + val)
            case '*':
                return (current * val)

    def isdividable(self, value: int, divisor: int):
        return value % divisor == 0

    def throw_20(self):
        for _ in range(20):
            for monkey in self.herd:
                for item in monkey.items:
                    inc_worry = self.calculate_worry(item, monkey.operation)
                    current_worry = (inc_worry // 3)
                    mapping = self.isdividable(current_worry, monkey.divisor)
                    target = monkey.test_map[mapping]
                    self.herd[target].items.append(current_worry)
                    monkey.inspections += 1
                monkey.items = []

    def throw_x(self, rounds: int):
        supermodulo = 1
        for monkey in self.herd:
            supermodulo *= monkey.divisor
        for _ in range(rounds):
            for monkey in self.herd:
                for item in monkey.items:
                    c_worry = self.calculate_worry(item, monkey.operation)
                    mapping = self.isdividable(c_worry, supermodulo)
                    target = monkey.test_map[mapping]
                    self.herd[target].items.append(c_worry)
                    monkey.inspections += 1
                monkey.items = []


def product(*args):
    prod = 1
    for arg in args:
        prod *= arg
    return prod


def part_one(filename):
    part1 = MonkeyHerd(filename)
    part1.throw_20()
    pt1_inspect = part1.get_interactions()
    pt1_inspect.sort(reverse=True)
    pt1_inspect = pt1_inspect[:2]
    return ['Part 1', product(*pt1_inspect)]


def part_two(filename):
    part2 = MonkeyHerd(filename)
    part2.throw_x(10_000)
    pt2_inspect = part2.get_interactions()
    pt2_inspect.sort(reverse=True)
    pt2_inspect = pt2_inspect[:2]
    return ['Part 2', product(*pt2_inspect)]


def main(filename):
    solution_tbl = [['Day 11', 'Solution']]
    pt1 = part_one(filename)
    pt2 = part_two(filename)
    solution_tbl.append(pt1)
    solution_tbl.append(pt2)
    print(tabulate(solution_tbl, tablefmt='fancy_grid', numalign='r'))


if __name__ == '__main__':
    main('example1.txt')
