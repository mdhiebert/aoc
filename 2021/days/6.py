from collections import defaultdict
from typing import List
from solution import Solution

PART_ONE_DATA = './2021/data/6-1.txt'
PART_TWO_DATA = './2021/data/6-2.txt'

class LanternFish:
    def __init__(self, timer):
        self.timer = timer

    def iterate(self):
        if self.timer == 0:
            self.timer = 6
        else:
            self.timer -= 1

    def ready_to_spawn(self):
        return self.timer == 0

    def __str__(self):
        return str(self.timer)

class LanternFishSchool:
    @staticmethod
    def parse_from_str(s):
        return LanternFishSchool([LanternFish(int(i)) for i in s.strip().split(',')])

    def __init__(self, fish: List[LanternFish]):
        self.fish = fish

    def iterate(self):
        num_fish_to_add = sum([int(f.ready_to_spawn()) for f in self.fish])

        for f in self.fish:
            f.iterate()

        for _ in range(num_fish_to_add):
            self.fish.append(LanternFish(8))

    def iterate_for_days(self, num_days, debug=False):
        for day in range(num_days):
            self.iterate()
            if debug: print(f'Completed day {day + 1}.')

    @property
    def size(self):
        return len(self.fish)

    def __str__(self):
        return ','.join([str(f) for f in self.fish])

class LanternFishSchoolEfficient(LanternFishSchool):

    @staticmethod
    def parse_from_str(s):
        timers = defaultdict(int)
        for value in [int(i) for i in s.strip().split(',')]:
            timers[value] += 1
        return LanternFishSchoolEfficient(timers)

    def __init__(self, timers: defaultdict):
        self.timers = timers

    def iterate(self):
        self.timers[9] = self.timers[0]
        self.timers[7] += self.timers[0]
        
        for i in range(1, 10):
            self.timers[i - 1] = self.timers[i]
    
    @property
    def size(self):
        temp = self.timers[9]
        self.timers[9] = 0
        sz = sum(list(self.timers.values()))
        self.timers[9] = temp
        return sz

    def __str__(self):
        return ','.join([str(f) for f in self.timers.values()])


class DaySix2021(Solution):
    def __init__(self):
        super().__init__(PART_ONE_DATA, PART_TWO_DATA)

    def part_one_solution(self):
        # 362740
        school = LanternFishSchool.parse_from_str(self.part_one_data)
        school.iterate_for_days(80)
        return school.size
        
    def part_two_solution(self):
        # 1644874076764
        school = LanternFishSchoolEfficient.parse_from_str(self.part_two_data)
        school.iterate_for_days(256)
        return school.size

if __name__ == '__main__':
    solution = DaySix2021()
    # print(solution.part_one_solution())
    print(solution.part_two_solution())
    # print(solution)
