from typing import List, Set
from solution import Solution

PART_ONE_DATA = './2021/data/8-1.txt'
PART_TWO_DATA = './2021/data/8-2.txt'

class SevenSegmentNumber:
    def __init__(self, letters: Set[str]):
        self.letters = letters

    def __len__(self):
        return len(self.letters)

    def __in__(self, x):
        return sum([int(i in self.letters) for i in x.letters]) == len(x.letters)

    def __add__(self, x):
        return self.letters.union(x.letters)

    def __sub__(self, x):
        return self.letters.difference(x.letters)

    def __str__(self):
        return self.letters

    def __eq__(self, x):
        return type(x) == type(self) and len(self.letters.intersection(x.letters)) == len(self.letters)

    def is_one(self, solution_dict):
        if self == solution_dict[1]: return True

        return len(self.letters) == 2

    def is_two(self, solution_dict):
        if self == solution_dict[2]: return True
        pass

    def is_three(self, solution_dict):
        if self == solution_dict[3]: return True

        one = solution_dict[1]
        four = solution_dict[4]
        seven = solution_dict[7]
        eight = solution_dict[8]

        if len(self.letters) == 5:
            if one in self and seven in self and four not in self and eight not in self:
                return True
        return False

    def is_four(self, solution_dict):
        if self == solution_dict[4]: return True

        return len(self.letters) == 4

    def is_five(self, solution_dict):
        if self == solution_dict[5]: return True
        
        six = solution_dict[6]

        return len(six - self) == 1

    def is_six(self, solution_dict):
        if self == solution_dict[6]: return True

        eight = solution_dict[8]

        return not self.is_nine() and len(eight - self) == 1

    def is_seven(self, solution_dict):
        if self == solution_dict[7]: return True

        return len(self.letters) == 3

    def is_eight(self, solution_dict):
        if self == solution_dict[8]: return True

        return len(self.letters) == 8

    def is_nine(self, solution_dict):
        if self == solution_dict[9]: return True

        four = solution_dict[4]

        return len(self - four) == 1

    def is_zero(self, solution_dict):
        pass

class SignalPattern:
    @staticmethod
    def parse_from_str(s):
        inp,out = [i.strip() for i in s.split(' | ')]

        return SignalPattern(inp.split(' '), out.split(' '))

    def __init__(self, inp: List[str], out: List[str]):
        self.inp = inp
        self.out = out

class DayEight2021(Solution):
    def __init__(self):
        super().__init__(PART_ONE_DATA, PART_TWO_DATA)

    def part_one_solution(self):
        # 362
        parsed_data = [SignalPattern.parse_from_str(l) for l in self.part_one_data.split('\n') if l]

        count = 0

        for pattern in parsed_data:
            for digit in pattern.out:
                if len(digit) in [2, 3, 4, 7]: count += 1

        return count
        

    def part_two_solution(self):
        # 101079875
        import numpy as np
        parsed_data = [int(x) for x in self.part_two_data.split(',') if x]

        # create the array
        max_val = max(parsed_data)
        distances = np.zeros((len(parsed_data),max_val + 1))

        for row,idx in enumerate(parsed_data):
            running_sum = 0
            for d,col in enumerate(range(idx, -1, -1)):
                running_sum += d
                distances[row][col] = int(running_sum)
            running_sum = 0
            for d,col in enumerate(range(idx,max_val + 1)):
                running_sum += d
                distances[row][col] = int(running_sum)

        distance_to_pos = np.sum(distances, axis=0)
        best_pos = np.argmin(distance_to_pos)
        fuel_consumption = np.min(distance_to_pos)

        return int(fuel_consumption)

if __name__ == '__main__':
    solution = DayEight2021()
    print(solution.part_one_solution())
    # print(solution.part_two_solution())
    # print(solution)
