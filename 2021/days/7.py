from solution import Solution

PART_ONE_DATA = './2021/data/7-1.txt'
PART_TWO_DATA = './2021/data/7-2.txt'

class DaySeven2021(Solution):
    def __init__(self):
        super().__init__(PART_ONE_DATA, PART_TWO_DATA)

    def part_one_solution(self):
        # 351901
        import statistics as stats
        parsed_data = [int(x) for x in self.part_one_data.split(',') if x]

        med = stats.median(parsed_data)

        total_fuel = sum([abs(x - med) for x in parsed_data])

        return int(total_fuel)
        

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
    solution = DaySeven2021()
    # print(solution.part_one_solution())
    print(solution)
