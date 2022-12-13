"""
Advent of Code 2022
Day 10
"""

from tabulate import tabulate


class Process:
    def __init__(self, program):
        self.program = self.run(program)
        self.register = []
        self.searched_runs = [20, 60, 100, 140, 180, 220]

    def run(self, program):
        chain = []
        for command in program:
            match command[0]:
                case 'noop':
                    chain.append((1, 0))
                case 'addx':
                    new_c1 = (1, 0)
                    new_c2 = (1, int(command[1]))
                    chain.extend((new_c1, new_c2))
        return chain

    def calc_run(self):
        cycle = 1
        register = 1
        for cmd in self.program:
            cycle += cmd[0]
            register += cmd[1]
            if cycle in self.searched_runs:
                self.register.append((cycle, register))

    def sum_list(self):
        summed = 0
        for factor in self.register:
            product = factor[0] * factor[1]
            summed += product
        return summed


def parse(filename: str):
    try:
        with open(filename, 'r') as file:
            return [line.strip().split(' ') for line in file.readlines()]
    except FileNotFoundError:
        print(f"[404]: File {filename} not found")


def solution(commands):
    solve_tbl = [['Advent of Code 2022', 'Day 10']]
    prog = Process(commands)
    prog.calc_run()
    print(prog.register)
    print(prog.sum_list())


def main():
    """ Main function """
    commands = parse('day10_input.txt')
    solution(commands)


if __name__ == '__main__':
    main()
