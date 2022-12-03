"""
Advent of Code 2022 - PART 2
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


class RucksackGroups(object):
    """
    Class representing Rucksack groups

    Args:
    group_inventory (list): a list of containing the invenmtory of 3 rucksacks
    """
    mapping = {
        str(x) : y+1
        for y, x in enumerate(ascii_lowercase + ascii_uppercase)
    }

    def __init__(self, group_inventory: list):
        self.items = group_inventory
        self.fst_rucksack = self.get_rucksacks(1)
        self.snd_rucksack = self.get_rucksacks(2)
        self.trd_rucksack = self.get_rucksacks(3)
        self.common = self.get_common()

    def get_rucksacks(self, rucksack_nr: int,) -> str:
        """Returns inventory of each rucksack in a group

        Args:
            rucksack_nr (int): number of the rucksack

        Raises:
            ValueError: if rucksack_nr is out of range 1 to 3

        Returns:
            str: Rucksack inventory
        """
        if rucksack_nr > 3 or rucksack_nr < 1:
            raise ValueError("Rucksack number must be between 1 and 3")
        return self.items[rucksack_nr-1]

    def get_common(self) -> int:
        """looks for duplicates in rucksacks and returns the priorities

        Returns:
            int: priority of duplicates as integer
        """
        duplicates = [d for d in self.fst_rucksack if
                      d in self.snd_rucksack and
                      d in self.trd_rucksack]
        return self.mapping[duplicates[0]]

def get_inverntory(file_name:str) -> list[list]:
    """gets the inventory from the given file,
    and divides it into a group of 3 packs

    Args:
        file_name (str): name of the file to get the inventory

    Returns:
        list[list]: list of lists containing the inventory_groups
    """
    inventory = []
    group_pack  = []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            if (idx + 1) % 3 != 0:
                group_pack.append(line)
            else:
                group_pack.append(line)
                inventory.append(group_pack)
                group_pack = []
        return inventory


def main():
    """ Main function """
    inv = Inventory(get_inverntory('day03_input.txt'))
    groups = [RucksackGroups(g) for g in inv.inventory]
    group_prios = [gp.common for gp in groups]
    print(sum(group_prios))

if __name__ == '__main__':
    main()
