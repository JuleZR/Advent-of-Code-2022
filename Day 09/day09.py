"""
Advent of Code 2022
Day:    09
Part:   1
"""

import os

def parse_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        exp_lst = []
        for line in lines:
            line = line.strip().split()
            row = []
            for exp in line:
                if exp.isdigit():
                    row.append(int(exp))
                else:
                    row.append(exp)
            exp_lst.append(row)
        return exp_lst

def move(directions:list):
    head_x, head_y = 0, 0
    yield head_x, head_y
    for move in directions:
        for _ in range(move[1]):
            match move[0]:
                case "R":
                    head_x += 1
                case "L":
                    head_x -= 1
                case "U":
                    head_y += 1
                case "D":
                    head_y -= 1
            yield  head_x, head_y

def _trace(points:tuple):
    tail_points = [(0,0)]
    for point in points:
        tx, ty = tail_points[-1]
        hx, hy = point
        dx, dy = tx - hx, ty - hy
        if abs(dx) <= 1 and abs(dy) <= 1:
            continue
        if abs(dy) > abs(dx):
            tx = hx
            ty = hy + (dy + 1) if dy < 0 else hy + (dy - 1)
            tail_points.append((tx, ty))
        elif abs(dy) < abs(dx):
            tx = hx + (dx + 1) if dx < 0 else hx + (dx - 1)
            ty = hy
            tail_points.append((tx, ty))
    return tail_points

def pt1():
    clear = lambda: os.system('cls')
    clear()
    p_input = parse_input('day09_input.txt')
    tail_points = _trace(move(p_input))
    print("==================== ADVENT OF CODE 2022 ====================")
    print("-- PART 1 ---------------------------------------------------\n")
    print(f'Number of points that the tail visited at least onece: {len(set(tail_points))}\n')
    print("-------------------------------------------------------------")

def main():
    """ Main function"""
    pt1()

if __name__ == "__main__":
    main()
