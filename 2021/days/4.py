from typing import List
from solution import Solution

PART_ONE_DATA = './2021/data/4-1.txt'
PART_TWO_DATA = './2021/data/4-2.txt'

class BingoBoard:
    @staticmethod
    def parse_from_str(s):
        lines = [l for l in s.split('\n') if l]
        numbers = [int(i) for subline in lines for i in subline.split(' ') if i]
        return BingoBoard(numbers)

    def __init__(self, numbers: List[int]):
        self.numbers = numbers
        self.marking = [False for _ in range(25)]

    def mark_value(self, value):
        if value in self.numbers:
            self.marking[self.numbers.index(value)] = True

    def is_win(self):

        # horizontal
        for i in range(0, 25, 5):
            if sum([int(b) for b in self.marking[i:i+5]]) == 5: return True

        # vertical
        for i in range(5):
            if (self.marking[i] and self.marking[i + 5] and self.marking[i + 10] and self.marking[i + 15] and self.marking[i + 20]): return True

        return False

    def sum_of_unmarked_numbers(self):
        s = 0
        for i in range(25):
            s += self.numbers[i] if not self.marking[i] else 0
        return s

    def __str__(self):
        lines = []
        for i in range(0, 25, 5):
            lines.append(self.numbers[i:i+5])
        
        return '\n'.join([' '.join([str(i) for i in line]) for line in lines])

class BingoGame:
    @staticmethod
    def parse_from_str(s):
        lines = [l for l in s.split('\n') if l]

        lineup = lines.pop(0)
        lineup = [int(s) for s in lineup.split(',')]

        boards = []
        for i in range(0, len(lines), 5):
            boards.append(BingoBoard.parse_from_str(' '.join(lines[i:i+5])))

        return BingoGame(lineup, boards)

    def __init__(self, lineup: List[int], boards: List[BingoBoard]):
        self.lineup = lineup
        self.boards = boards

    def is_game_over(self):
        return True in [board.is_win() for board in self.boards]

    def _get_winning_board(self):
        return self.boards[[board.is_win() for board in self.boards].index(True)]

    def play_game(self):
        cur_val = -1
        while not self.is_game_over():
            cur_val = self.lineup.pop(0)
            for board in self.boards:
                board.mark_value(cur_val)
        
        winning_board = self._get_winning_board()

        return cur_val * winning_board.sum_of_unmarked_numbers()

    def __str__(self):
        return f'{self.lineup}\n{self.boards}'

class BingoGameModified(BingoGame):
    @staticmethod
    def parse_from_str(s):
        lines = [l for l in s.split('\n') if l]

        lineup = lines.pop(0)
        lineup = [int(s) for s in lineup.split(',')]

        boards = []
        for i in range(0, len(lines), 5):
            boards.append(BingoBoard.parse_from_str(' '.join(lines[i:i+5])))

        return BingoGameModified(lineup, boards)

    def __init__(self, lineup: List[int], boards: List[BingoBoard]):
        super().__init__(lineup, boards)
        self.win_order = []

    def is_game_over(self):
        winners = [board.is_win() for board in self.boards]

        for i in range(len(winners)):
            if winners[i] and i not in self.win_order: self.win_order.append(i)

        return False not in winners

    def _get_winning_board(self):
        return self.boards[self.win_order[-1]]

class DayFour2021(Solution):
    def __init__(self):
        super().__init__(PART_ONE_DATA, PART_TWO_DATA)

    def part_one_solution(self):
        # 44736
        bingo_game = BingoGame.parse_from_str(self.part_one_data)

        return bingo_game.play_game()
        

    def part_two_solution(self):
        # 1827
        bingo_game = BingoGameModified.parse_from_str(self.part_two_data)

        return bingo_game.play_game()

if __name__ == '__main__':
    solution = DayFour2021()
    # print(solution.part_one_solution())
    print(solution)
