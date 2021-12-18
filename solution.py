class Solution:
    def __init__(self, part_one_datapath, part_two_datapath):
        with open(part_one_datapath) as f:
            self.part_one_data = f.read()

        with open(part_two_datapath) as f:
            self.part_two_data = f.read()

    def part_one_solution(self):
        raise NotImplementedError

    def part_two_solution(self):
        raise NotImplementedError

    def __str__(self):
        return f'The solution for part one is {self.part_one_solution()} and the solution for part two is {self.part_two_solution()}.'