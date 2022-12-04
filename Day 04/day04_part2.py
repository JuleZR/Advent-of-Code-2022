"""
Advent of Code 2022
Day 04 - Part 1
"""


class CampCleanup(object):
    """
    Class for analyzing the section IDs
    """
    def __init__(self, filename: str):
        self.section_id_pairs = self.get_id_pairs(filename)
        self.full_overlap = self.get_full_overlap()

    def get_id_pairs(self, filename: str) -> list[list]:
        """
        Generates a list of of lists from a file containing
        the range of section IDs.

        Args:
            filename (str): name of the file to read

        Returns:
            list[list]: containing range of section IDs
        """
        all_pairs = []
        try:
            with open(filename+".txt", 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip().split(',')
                    line = self._get_range_from_ids(line)
                    all_pairs.append(line)
                return all_pairs

        except FileNotFoundError as err:
            print(f"{err} - File {filename} not found.")

    def _get_range_from_ids(self, id_list: list) -> list:
        """Converts the section ids to its range

        Args:
            id_list (list):  containing section ids

        Returns:
            list: containing range of sction ids
        """
        result = []
        for element in id_list:
            range_nr = element.split("-")
            id_range = list(range(int(range_nr[0]), int(range_nr[1]) +1 ))
            result.append(id_range)
        return result

    def get_full_overlap(self) -> int:
        """Calculates full overlap between id ranges

        Returns:
            int: _description_
        """
        overlapping = 0
        for pair in self.section_id_pairs:
            if bool(set(pair[0]) & set(pair[1])):
                overlapping += 1
        return overlapping

def main():
    """ Main function"""
    c_clean = CampCleanup('day04_input')
    print(f"Number of overlapping: {c_clean.full_overlap}")

if __name__ == "__main__":
    main()
