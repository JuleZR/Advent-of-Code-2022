"""
Advent of Code 2022 - PART 1
The Rucksacks prioritys
"""
from string import ascii_uppercase, ascii_lowercase
from dataclasses import dataclass


@dataclass
class Inventory(object):
    """
    Data class that represents the entire inventory that is available
    """
    inventory: list


class Rucksack(object):
    """ A rucksack with two compartments containing items """
    mapping = {
        str(x) : y+1
        for y, x in enumerate(ascii_lowercase + ascii_uppercase)
    }
    def __init__(self, items):
        self.items = items
        self.fst_compartment = self.get_compartment_items(1)
        self.snd_compartment = self.get_compartment_items(2)
        self.duplicate_prio = self.get_duplicates_prio()

    def get_compartment_items(self, compartment: int,) -> list:
        """Distributes the contents of a rucksacks into two compartments

        Args:
            compartment (int): must be 1 or 2

        Returns:
            list: distributet item
        """
        comp_i = int(len(self.items) / 2)
        if compartment == 1:
            return self.items[:comp_i]
        if compartment == 2:#
            return self.items[comp_i:]

    def get_duplicates_prio(self) -> int:
        """looks for duplicates in compartments and returns the priorities

        Returns:
            int: priority of duplicates as integer
        """
        duplicates = [d for d in self.fst_compartment if d in self.snd_compartment]
        return self.mapping[duplicates[0]]


def get_inverntory(file_name:str) -> list:
    """Reads the inventory contents from a file

    Args:
        file_name (str): the name of the file to read

    Returns:
        list: List of all items in the inventory
    """
    inventory = []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            inventory.append(line)
        return inventory


def main():
    """ Main function"""
    inv = Inventory(get_inverntory('day03_input.txt'))
    rucksacks = [Rucksack(itemm_stack) for itemm_stack in inv.inventory]
    prio_lst = [r.duplicate_prio for r in rucksacks]
    print(sum(prio_lst))

if __name__ == '__main__':
    main()
