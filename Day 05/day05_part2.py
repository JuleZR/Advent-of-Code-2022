"""
Advent of Code 2022
Day:    5
Part:   2
"""

class CratePileMovement:
    """
    Class representing a Crane, the movement and the cargo stacks
    """
    def __init__(self, filename: str, d_index: int):
        """
        Creates a instance of a CratePileMovement,
        from a given text file.

        Args:
            filename (str): name of the file
            d_index (int): number of piles as an integer
        """
        self.filename = filename
        self.d_index = d_index
        self.crate_piles = self._get_crate_piles()
        self.movements = self._get_movements()

    def _get_crate_piles(self) -> list:
        """gets crate piles from a text file

        Returns:
            list: list of lists containing crate piles
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            crate_rows = []
            crate_piles = []
            lines = file.readlines()
            for idx, line in enumerate(lines):
                if idx <= self.d_index - 1:
                    line = line.strip("\n")
                    crate_row = [line[i:i+3] for i in range(0, len(line), 4)]
                    crate_rows.append(crate_row)
            crate_rows.reverse()
            for idx, _ in enumerate(crate_rows):
                pile = []
                for crate in crate_rows:
                    if crate[idx] != "   ":
                        pile.append(crate[idx])
                crate_piles.append(pile)
        return crate_piles

    def _get_movements(self) -> list[list]:
        """Gets movemnet instructions from a file

        Returns:
            list[list]: list of lits containing movemnet instructions
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            movements = []
            for idx, line in enumerate(lines):
                if idx >= self.d_index + 1:
                    line = line.strip()
                    line = line.replace("move ", "")
                    line = line.replace("from ", "")
                    line = line.replace("to ", "")
                    line = line.split()
                    movement = [int(l) for l in line]
                    movements.append(movement)
            return movements

    def movement(self, movement:list):
        """Modifys the cratelist by given movement

        Args:
            movement (list): containing amount, start and target
        """
        amount = movement[0]
        start = movement[1] - 1
        target = movement[2] - 1
        m_crates = self.crate_piles[start][-amount:]
        self.crate_piles[start] = self.crate_piles[start][:-amount]
        for crate in m_crates:
            self.crate_piles[target].append(crate)



def main():
    """ Main function"""
    cpm = CratePileMovement('day05_input.txt', 9)
    for move in cpm.movements:
        cpm.movement(move)
    answer = ""
    for crate in cpm.crate_piles:
        answer += crate[-1][1:2]
    print(answer)

if __name__ == '__main__':
    main()
