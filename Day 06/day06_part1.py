"""
Advent of Code 2022
Day:    6
Part:   1
"""

class ElvenComunicator:
    """ Class representing a elven communication device"""
    def __init__(self, filename:str):
        self.signal = self._get_signals(filename)

    def _get_signals(self, filename):
        """ gets signal sequence from file"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.readline()
                
        except FileNotFoundError as err:
            print(f"{err}:\nCouldn't find file: {filename}")
    
    def distinct_signals(self, data:str) -> int:
        """
        Takes a string data sequence and calculates the number of
        proccessed characters

        Args:
            data (str): a data squence as a string

        Returns:
            int: _description_
        """
        chars_processed = 4
        for idx, _ in enumerate(data):
            group = data[0+idx:4+idx]
            if len(set(group)) < 4:
                chars_processed += 1
            if len(set(group)) == 4:
                break
        print(chars_processed)

def main():
    """ Main function """
    elf_com = ElvenComunicator('day06_input.txt')
    elf_com.distinct_signals(elf_com.signal)

if __name__ == "__main__":
    main()
