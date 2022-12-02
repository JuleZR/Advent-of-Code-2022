""" Game of Rock Paper Scissors with amn elven strategy guide
PART 2
"""

class RockPaperScissors:
    """ Rock Paper Scissors Class"""

    def __init__(self):
        self.outcome = self.get_outcome(self.get_games())
        self.scores = self.get_score()
        self.total_score = sum(self.scores)

    def get_games(self) -> list[list]:
        """Reads player choices from txt file

        Returns:
            list[list]: List of lists containing the game matches
        """
        with open('day02_input.txt', 'r', encoding='utf-8') as file:
            matches = []
            lines = file.readlines()
            for line in lines:
                game = [l for l in line.strip().split(" ")]
                matches.append(game)
            return matches

    def get_outcome(self, matches:list[list]) -> list[list]:
        outcome = {
            'win': {'A':'Y','B':'Z', 'C':'X'},
            'draw': {'A':'X','B':'Y', 'C':'Z'},
            'loose': {'A':'Z','B':'X', 'C':'Y'}
        }
        
        for game in matches:
            if game[1] == "X":
                game.append(0)
                result = outcome['loose'][game[0]]
            if game[1] == "Y":
                game.append(3)
                result = outcome['draw'][game[0]]
            if game[1] == "Z":
                game.append(6)
                result = outcome['win'][game[0]]
            game.append(result)
        return matches

    def get_score(self) -> list[int]:
        """Claculates the score for each game

        Returns:
            list[int]: List of scores for ech game
        """
        mapping = {'X': 1, 'Y': 2, 'Z': 3}
        scores = []
        for encounter in self.outcome:
            points = encounter[2] + mapping[encounter[3]]
            scores.append(points)
        return scores

def main():
    """Main function"""
    rps = RockPaperScissors()
    print(rps.total_score)

if __name__ == '__main__':
    main()
