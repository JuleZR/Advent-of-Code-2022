"""
Advent of Code 2022
Day:    7
Part:   1
"""

from dataclasses import dataclass

@dataclass
class File:
    position: list
    size: int
    name: str

@dataclass
class Folder:
    position: list
    name: str

class FileSystem:
    def __init__(self, filename):
        self.commands = self._get_cmds(filename)
        self.content = self._get_content()

    def _get_cmds(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                return [line.strip().replace('$ ', '').split() for line in lines]
        except FileExistsError:
            print("Error: File not found")

    def _get_content(self):
        current = []
        content =  []
        for idx, cmd in enumerate(self.commands):
            print(idx, current)
            if cmd[0] == "ls":
                continue
            if cmd[0] == 'cd':
                if cmd[1] == '/':
                    current.append(" ")
                if cmd[1].isalpha() is True:
                    current.append(cmd[1])
                if cmd[1] == '..':
                    del current[-1]
            if cmd[0] == 'dir':
                content.append(Folder(current, cmd[1]))
            if cmd[0].isnumeric() is True:
                content.append(File(current, cmd[0], cmd[1]))
        return content

def main():
    """ Main function """
    file_s = FileSystem('test.txt')

if __name__ == '__main__':
    main()
