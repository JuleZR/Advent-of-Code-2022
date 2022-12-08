"""
Advent of Code 2022
Day:    7
Part:   1 & 2
"""

import numpy as np


def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        parsing = []
        for line in lines:
            line = line.strip()
            row = []
            for digit in str(line):
                row.append(int(digit))
            parsing.append(row)
        return parsing


def part_one(grid: np.array):
    part1 = np.zeros_like(grid, int)
    for _ in range(4):
        for x, y in np.ndindex(grid.shape):
            lower = [t < grid[x, y] for t in grid[x, y+1:]]
            part1[x, y] |= all(lower)
        
        grid, part1 = map(np.rot90, [grid, part1])
    print("===== PART I =====")
    print(part1.sum())

def part_two(grid: np.array):
    part2 = np.ones_like(grid, int)
    for _ in range(4):
        for x, y in np.ndindex(grid.shape):
            lower = [t < grid[x, y] for t in grid[x, y+1:]]
            part2[x, y] *= next((i+1 for i,t in enumerate(lower) if ~t), len(lower))
        
        grid, part2 = map(np.rot90, [grid, part2])
    print("===== PART II =====")
    print(part2.max())
            

def main():
    np_grid = np.array(parse_input('day08_input.txt'))
    part_one(np_grid)
    part_two(np_grid)

if __name__ == '__main__':
    main()