"""
Advent of Code 2022
Day 09
"""

from tabulate import tabulate

MOVE_MAP = {
    'R': [1, 0],
    'L': [-1, 0],
    'U': [0, 1],
    'D': [0, -1]
}


class Rope:
    def __init__(self, directions):
        self.hx, self.hy = 0, 0
        self.tx, self.ty = 0, 0
        self.directions = directions
        self.tail = set()

    def touch(self, x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

    def move(self, dx, dy):
        self.hx += dx
        self.hy += dy

        if not self.touch(self.hx, self.hy, self.tx, self.ty):
            change_x = 0 if self.hx == self.tx \
                else (self.hx - self.tx) / abs(self.hx - self.tx)
            change_y = 0 if self.hy == self.ty \
                else (self.hy - self.ty) / abs(self.hy - self.ty)

            self.tx += change_x
            self.ty += change_y
        return self.tx, self.ty

    def calc(self):
        for line in self.directions:
            operation, amount = line.split(' ')
            amount = int(amount)
            dx, dy = MOVE_MAP[operation]

            for _ in range(amount):
                tx, ty = self.move(dx, dy)
                self.tail.add((self.tx, self.ty))


class LongerRope:
    def __init__(self, directions):
        self.rope = [[0, 0] for _ in range(10)]
        self.directions = directions
        self.tail = set()

    def touch(self, x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

    def move(self, dx, dy):
        self.rope[0][0] += dx
        self.rope[0][1] += dy
        for i in range(1, 10):
            hx, hy = self.rope[i - 1]
            tx, ty = self.rope[i]
            if not self.touch(hx, hy, tx, ty):
                change_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
                change_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)
                tx += change_x
                ty += change_y
            self.rope[i] = [tx, ty]

    def calc(self):
        for line in self.directions:
            operation, amount = line.split(' ')
            amount = int(amount)
            dx, dy = MOVE_MAP[operation]

            for _ in range(amount):
                self.move(dx, dy)
                self.tail.add(tuple(self.rope[-1]))


def parse(filename):
    with open(filename) as file:
        lines = file.read().strip(). split('\n')
        return lines


def solutions(directions):
    solver_table = [['Advent of Code 2022', 'Day 9']]

    s_rope = Rope(directions)
    s_rope.calc()
    solver_table.append(['Part 1', len(s_rope.tail)])

    l_rope = LongerRope(directions)
    l_rope.calc()
    solver_table.append(['Part 2', len(l_rope.tail)])
    print(tabulate(solver_table, tablefmt='fancy_grid'))


def main():
    """ Main function """
    directions = parse('day09_input.txt')
    solutions(directions)


if __name__ == '__main__':
    main()
