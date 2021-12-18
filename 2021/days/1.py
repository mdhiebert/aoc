from solution import Solution

PART_ONE_DATA = './2021/data/1-1.txt'
PART_TWO_DATA = './2021/data/1-2.txt'

class DayOne2021(Solution):
    def __init__(self):
        super().__init__(PART_ONE_DATA, PART_TWO_DATA)

    def part_one_solution(self):
        # 1390
        parsed_data = [int(s) for s in self.part_one_data.split('\n') if s]
        return sum([1 for i,x in enumerate(parsed_data) if i != 0 and x > parsed_data[i - 1]])

    def part_two_solution(self):
        # 1457
        parsed_data = [int(s) for s in self.part_two_data.split('\n') if s]
        sliding_window = lambda i,l: l[i-1] + l[i] + l[i+1]
        return sum([1 for i,x in enumerate(parsed_data) if i not in [0, len(parsed_data) - 2, len(parsed_data) - 1] and sliding_window(i+1,parsed_data) > sliding_window(i,parsed_data)])

if __name__ == '__main__':
    solution = DayOne2021()
    print(solution)
