from solution import Solution

PART_ONE_DATA = './2021/data/2-1.txt'
PART_TWO_DATA = './2021/data/2-2.txt'

class DayTwo2021(Solution):
    def __init__(self):
        super().__init__(PART_ONE_DATA, PART_TWO_DATA)

    def part_one_solution(self):
        # 1924923
        parsed_data = [(d,int(x)) for d,x in [line.split(' ') for line in [s for s in self.part_one_data.split('\n') if s]]]
        
        dir_map = {'up': (0, 1), 'down': (0, -1), 'forward': (1, 0)}

        pos = (0,0)

        mult_sum = lambda o,n,c,i: o[i] + (n * c[i])
        accumulate = lambda o,n,c: (mult_sum(o,n,c,0),mult_sum(o,n,c,1))

        for direction,value in parsed_data:
            pos = accumulate(pos, value, dir_map[direction])
        
        adjusted_pos = (pos[0], -1 * pos[1]) # depth is positive!
        return adjusted_pos[0] * adjusted_pos[1]

    def part_two_solution(self):
        # 1982495697
        parsed_data = [(d,int(x)) for d,x in [line.split(' ') for line in [s for s in self.part_two_data.split('\n') if s]]]
        

        aim = 0
        pos = (0,0,aim)
        mult_sum = lambda o,n,c,i: o[i] + (n * c[i])
        accumulate = lambda o,n,c: (mult_sum(o,n,c,0),mult_sum(o,n,c,1),mult_sum(o,n,c,2))

        for direction,value in parsed_data:
            dir_map = {'up': (0, 0, -1), 'down': (0, 0, 1), 'forward': (1, pos[2], 0)}
            pos = accumulate(pos, value, dir_map[direction])

        return pos[0] * pos[1]

if __name__ == '__main__':
    solution = DayTwo2021()
    # print(solution.part_one_solution())
    print(solution)
