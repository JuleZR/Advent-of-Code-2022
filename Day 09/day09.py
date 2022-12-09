"""
Advent of Code 2022
Day:    7
Part:   1
"""
from dataclasses import dataclass, field

@dataclass
class Rope:
    movemnet: list
    head: tuple = (0, 0)
    tail: tuple = (0, 0)
    tail_path: list = field(default_factory=list)

    def move(self):
        for move in self.movemnet:
            match move[0]:
                case 'R':
                    self.head = (self.head[0] + move[1], self.head[1])
                    self.trace_path(move)
                case 'L':
                    self.head = (self.head[0] - move[1], self.head[1])
                    self.trace_path(move)
                case 'U':
                    self.head = (self.head[0], self.head[1] + move[1])
                    self.trace_path(move)
                case 'D':
                    self.head = (self.head[0], self.head[1] - move[1])
                    self.trace_path(move)

    def trace_path(self, move:list):
        print(self.check_diagonal())
        if self.check_diagonal() is False:
            match move[0]:
                case 'R':
                    for r in range(move[1]):
                        new_tail = (self.tail[0] + r, self.tail[1])
                        self.tail_path.append(new_tail)
                    self.tail = (self.head[0] - 1, self.head[1])
                case 'L':
                    for l in range(move[1]):
                        new_tail = (self.tail[0] - l, self.tail[1])
                        self.tail_path.append(new_tail)
                    self.tail = (self.head[0] + 1, self.head[1])
                case 'U':
                    for u in range(move[1]):
                        new_tail = (self.tail[0], self.tail[1] + u)
                        self.tail_path.append(new_tail)
                    self.tail = (self.head[0], self.head[1] - 1)
                case 'D':
                    for d in range(move[1]):
                        new_tail = (self.tail[0], self.tail[1] - d)
                        self.tail_path.append(new_tail)
                    self.tail = (self.head[0], self.head[1] + 1)

    def check_diagonal(self):
        tail_x, tail_y = self.tail
        head_x, head_y = self.head
        delta_x = head_x - tail_x
        delta_y = head_y - tail_y
        if delta_x > 1 or delta_x < -1:
            return False
        elif delta_y > 1 or delta_y < -1:
            return False
        else:
            return True

def parse_input(filename:str) -> list[list]:
    with open(filename, 'r') as f:
        lines = f.readlines()
        movments = []
        for line in lines:
            move = []
            line = line.strip()
            vals = line.split(' ')
            move.append(vals[0])
            move.append(int(vals[1]))
            movments.append(move)
        return movments

def pt1(path_trace:list):
    print("========== Part 1 ==========")
    print(f"number of visited points: {len(set(path_trace))}")

def main():
    rope = Rope(parse_input('example.txt'))
    rope.move()
    for idx, cord in enumerate(rope.tail_path):
        print(f"{idx:2d}:  {cord}")
    pt1(rope.tail_path)

if __name__ == '__main__':
    main()
