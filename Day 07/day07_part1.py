"""
Advent of Code 2022
Day:    7
Part:   1
"""

from dataclasses import dataclass, field
from typing import Type

@dataclass(repr=False)
class Folder:
    """ A Folder in a file system"""
    name: str
    parent: Type['Folder'] | None = None
    children: list[Type['Folder'] | Type['File']] = field(default_factory=list)

    def get_child(self, name:str) -> Type['Folder'] | Type['File']:
        """
        Returns the child object for the searched name if the searched
        name is a child of the object

        Args:
            name (str): name of the child

        Raises:
            ValueError: if the name you are looking for is not a child of the current object

        Returns:
            Type[File] | Type[Folder]: the searched child object
        """
        for child in self.children:
            if child.name == name:
                return child
        raise ValueError('Could not find child')

    def add_child(self, child: Type['Folder'] | Type['File']):
        """Adds a child to the current object

        Args:
            child (Type[Folder] | Type[File]):  a child Object that corresponds
            to either the Folder or File class
        """
        self.children.append(child)

    def get_path(self) -> str:
        """
        returns the path of the object. If there is no parent,
        the name of the object is returned

        Returns:
            str: path of the object
        """
        if self.parent is None:
            return self.name
        parent = self.parent.get_path()
        if parent != "/":
            return f"{parent}/{self.name}"
        return f"/{self.name}"

    def get_total_size(self, sizes: dict[str, int] | None = None) -> int:
        """Calculates the total file size of an object

        Args:
            sizes (dict[str, int] | None, optional): a dictionary containing
            already calculated total sizes of subfolders. Defaults to None.

        Returns:
            int: total size of the folder object
        """
        current_p = self.get_path()
        total = sum([child.get_total_size(sizes) if isinstance(child, Folder) else child.size
            for child in self.children])
        if sizes is not None:
            sizes[current_p] = total
        return total

    def __repr__(self) -> str:
        return f'Folder: "{self.name}"'


@dataclass(repr=False)
class File:
    """ Class representing a file"""
    name: str
    parent: Type['Folder']
    size: int

    def get_path(self) -> str:
        """returns the path of the file object

        Returns:
            str: path of the file object
        """
        return f"{self.parent.get_path()}/{self.name}"

    def __repr__(self) -> str:
        return f"{self.name}: size={self.size}"

def parse_input(filename:str) -> Folder:
    """
    Analyzes the commands specified in the input and translates
    them into a file system consisting of file and folder classes

    Args:
        filename (str): name of the input file

    Returns:
        Folder: A folder of Folders and Files representing the file system
    """
    with open(filename, 'r', encoding='utf-8') as file:
        cmds = [l.strip().replace('$ ', '').split() for l in file.readlines()]

    root = Folder('/')
    current = root
    for cmd in cmds:
        match cmd:
            case ['ls']:
                continue
            case ['cd', '..']:
                current = current.parent
            case ['cd', '/']:
                current = root
            case ['cd', folder] if folder != "/":
                current = current.get_child(folder)
            case ['dir', folder]:
                current.add_child(Folder(folder, current))
            case [size, file_name]:
                current.add_child(File(file_name, current, int(size)))
    return root

def calc_dir_size(root: Type['Folder'], sizes: dict[str, int] | None = None) -> dict:
    """Calculates the individual folder sizes

    Args:
        root (Folder): the root folder object
        sizes (dict[str, int] | None, optional): a dictionary of paths and their size.
        Defaults to None.

    Returns:
        dict: paths and their size.
    """
    if sizes is None:
        sizes = {}
    if root.get_path() in sizes:
        return sizes
    root.get_total_size(sizes)
    return sizes

def main():
    """ Main function"""
    file_s = parse_input('day07_input.txt')
    dir_sizes = calc_dir_size(file_s)
    print(sum([size for size in dir_sizes.values() if size < 100_000]))

if __name__ == '__main__':
    main()
