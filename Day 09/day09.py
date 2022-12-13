"""
Advent of Code 2022
Day:    09
"""

import sys
from tabulate import tabulate


class Rope:
    def __init__(self, filename):
        self.movement = self._parse(filename)
        self.head = [hp for hp in self._move_head()]
        self.tail = self._move_tail(self.head)

    def _parse(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = [item.strip().split(' ') for item in f.readlines()]
                directions = [[d, int(a)] for d, a in lines]
                return directions
        except FileNotFoundError:
            print(f'Error [404] - File "{filename}" not found')
            sys.exit('Problem terminated by error')

    def _move_head(self):
        hx, hy = 0, 0
        yield hx, hy
        for move in self.movement:
            for _ in range(move[1]):
                match move[0]:
                    case 'R':
                        hx += 1
                    case 'L':
                        hx -= 1
                    case 'U':
                        hy += 1
                    case 'D':
                        hy -= 1
                yield hx, hy

    def _move_tail(self, cords_to_follow: list):
        tail_cords = [(0, 0)]
        for h_point in cords_to_follow:
            hx, hy = h_point
            tx, ty = tail_cords[-1]
            dx, dy = tx - hx, ty - hy
            if abs(dx) <= 1 and abs(dy) <= 1:
                continue
            if abs(dx) < abs(dy):
                tx = hx
                ty = hy + (dy + 1) if dy < 0 else hy + (dy - 1)
                tail_cords.append((tx, ty))
            elif abs(dx) > abs(dy):
                tx = hx + (dx + 1) if dx < 0 else hx + (dx - 1)
                ty = hy
                tail_cords.append((tx, ty))
        return tail_cords


class LongRope(Rope):
    def __init__(self, filename):
        super().__init__(filename)
        self.movement = self._parse(filename)
        self.head = [hp for hp in self._move_head()]
        self.tail_1 = self._move_tail(self.head)
        self.tail_2 = self._move_tail(self.tail_1)
        self.tail_3 = self._move_tail(self.tail_2)
        self.tail_4 = self._move_tail(self.tail_3)
        self.tail_5 = self._move_tail(self.tail_4)
        self.tail_6 = self._move_tail(self.tail_5)
        self.tail_7 = self._move_tail(self.tail_6)
        self.tail_8 = self._move_tail(self.tail_7)
        self.tail_9 = self._move_tail(self.tail_8)


def solutions(filename):
    solution = [['Advent of Code 2022', 'Day 9']]

    s_rope = Rope(filename)
    solution.append(['Part 1', len(set(s_rope.tail))])

    l_rope = LongRope(filename)
    solution.append(['Part 2', len(set(l_rope.tail_9))])
    print(tabulate(solution, tablefmt='fancy_grid'))


def main():
    solutions('day09_input.txt')


if __name__ == '__main__':
    main()
