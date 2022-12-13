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

    def x_for_cycle(self, start: int, end: int):
        cycle = 0
        register = 1
        x_values = []
        for cmd in self.program:
            cycle += cmd[0]
            register += cmd[1]
            if cycle in range(start, end):
                x_values.append(register)
        return x_values

def parse(filename: str):
    try:
        with open(filename, 'r') as file:
            return [line.strip().split(' ') for line in file.readlines()]
    except FileNotFoundError:
        print(f"[404]: File {filename} not found")

def draw(x_val):
    output = ""
    for i in range(40):
        rng = x_val[i]
        if i in range(rng-2, rng+1):
            output += "#"
        else:
            output += "."
    print(output)

def solution1(commands):
    prog = Process(commands)
    prog.calc_run()
    print('PART I ======================================\n')
    print(f"Sum of X Values: {prog.sum_list()}\n\n")


def solution2(commands):
    prog2 = Process(commands)
    prog2.calc_run()
    xl_1 = prog2.x_for_cycle(0, 41)
    xl_2 = prog2.x_for_cycle(41, 81)
    xl_3 = prog2.x_for_cycle(81, 121)
    xl_4 = prog2.x_for_cycle(121, 161)
    xl_5 = prog2.x_for_cycle(161, 201)
    xl_6 = prog2.x_for_cycle(201, 241)
    print('PART II =====================================\n')
    draw(xl_1)
    draw(xl_2)
    draw(xl_3)
    draw(xl_4)
    draw(xl_5)
    draw(xl_6)
    

def main():
    """ Main function """
    commands = parse('day10_input.txt')
    solution1(commands)
    solution2(commands)


if __name__ == '__main__':
    main()
