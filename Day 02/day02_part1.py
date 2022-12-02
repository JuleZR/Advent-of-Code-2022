""" Game of Rock Paper Scissors with amn elven strategy guide"""

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
        """Cheks if the game is won or lost and appends the points for it

        Args:
            matches (list[list]): list of lists with all game combinations

        Returns:
            list[list]: list of list with game combinations plus win/lost points
        """
        for game in matches:
            if game[0] == 'A' and game[1] == 'X':
                game.append(3)
            if game[0] == 'A' and game[1] == 'Y':
                game.append(6)
            if game[0] == 'A' and game[1] == 'Z':
                game.append(0)
            if game[0] == 'B' and game[1] == 'X':
                game.append(0)
            if game[0] == 'B' and game[1] == 'Y':
                game.append(3)
            if game[0] == 'B' and game[1] == 'Z':
                game.append(6)
            if game[0] == 'C' and game[1] == 'X':
                game.append(6)
            if game[0] == 'C' and game[1] == 'Y':
                game.append(0)
            if game[0] == 'C' and game[1] == 'Z':
                game.append(3)
        return matches

    def get_score(self) -> list[int]:
        """Calculate the score for the games and returns the
        total game score as a list

        Returns:
            list[int]: List of integers representing score for for each game
        """
        mapping = {'X': 1, 'Y': 2, 'Z': 3}
        scores = []
        for encounter in self.outcome:
            points = encounter[2] + mapping[encounter[1]]
            scores.append(points)
        return scores

def main():
    """Main function"""
    rps = RockPaperScissors()
    print(rps.total_score)

if __name__ == '__main__':
    main()
