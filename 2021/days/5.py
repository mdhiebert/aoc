from solution import Solution

PART_ONE_DATA = './2021/data/5-1.txt'
PART_TWO_DATA = './2021/data/5-2.txt'

class Point:
    @staticmethod
    def parse_from_str(s):
        x,y = s.split(',')

        return Point(int(x), int(y))

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'

    def __eq__(self, other):
        return type(other) == Point and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y)

class Line:
    @staticmethod
    def parse_from_str(s):
        start_point, end_point = s.split(' -> ')

        return Line(Point.parse_from_str(start_point), Point.parse_from_str(end_point))

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_tl_to_br(self):
        return self.tl in [self.start, self.end]

    def is_tr_to_bl(self):
        return self.tr in [self.start, self.end]

    def is_horizontal_vertical(self):
        return self.is_horizontal() or self.is_vertical()

    def covers(self, p: Point, count_diag = False):
        if self._point_in_bounds(p):
            
            if self.is_horizontal(): return self.start.y == p.y
            elif self.is_vertical(): return self.start.x == p.x
            elif count_diag and self.is_tl_to_br():
                return self.tl.x - p.x == self.tl.y - p.y
            elif count_diag and self.is_tr_to_bl():
                return self.tr.x - p.x == p.y - self.tr.y
            else: return False

    def _point_in_bounds(self, p: Point):
        lt_in_range = lambda a, prop: getattr(a, prop) <= max(getattr(self.start, prop), getattr(self.end, prop))
        gt_in_range = lambda a, prop: getattr(a, prop) >= min(getattr(self.start, prop), getattr(self.end, prop))

        return lt_in_range(p, 'x') and lt_in_range(p, 'y') and gt_in_range(p, 'x') and gt_in_range(p, 'y')

    @property
    def tl(self):
        return Point(min([self.start.x, self.end.x]), min([self.start.y, self.end.y]))

    @property
    def tr(self):
        return Point(max([self.start.x, self.end.x]), min([self.start.y, self.end.y]))

    @property
    def bl(self):
        return Point(min([self.start.x, self.end.x]), max([self.start.y, self.end.y]))

    @property
    def br(self):
        return Point(max([self.start.x, self.end.x]), max([self.start.y, self.end.y]))


class DayFive2021(Solution):
    def __init__(self):
        super().__init__(PART_ONE_DATA, PART_TWO_DATA)

    def part_one_solution(self):
        # 7297
        from collections import defaultdict
        lines = [Line.parse_from_str(s) for s in self.part_one_data.split('\n') if s]

        top_left_x = min([l.tl.x for l in lines])
        top_left_y = min([l.tl.y for l in lines])
        bot_right_x = max([l.br.x for l in lines])
        bot_right_y = max([l.br.y for l in lines])

        counts = defaultdict(int)

        # generate our field
        for x in range(top_left_x, bot_right_x + 1):
            for y in range(top_left_y, bot_right_y + 1):
                p = Point(x,y)
                for line in lines:
                    if line.covers(p): counts[p] += 1

        # get counts >= 2
        return sum([int(x >= 2) for x in counts.values()])
        

    def part_two_solution(self):
        # 21038
        from collections import defaultdict
        import numpy as np
        lines = [Line.parse_from_str(s) for s in self.part_two_data.split('\n') if s]

        top_left_x = min([l.tl.x for l in lines])
        top_left_y = min([l.tl.y for l in lines])
        bot_right_x = max([l.br.x for l in lines])
        bot_right_y = max([l.br.y for l in lines])

        counts = defaultdict(int)

        # grid = np.zeros((bot_right_y - top_left_y + 1, bot_right_x - top_left_x + 1))

        # generate our field
        for x in range(top_left_x, bot_right_x + 1):
            for y in range(top_left_y, bot_right_y + 1):
                p = Point(x,y)
                for line in lines:
                    if line.covers(p, True):
                        counts[p] += 1
                        # grid[p.y,p.x] += 1

        # get counts >= 2
        return sum([int(x >= 2) for x in counts.values()])

if __name__ == '__main__':
    solution = DayFive2021()
    # print(solution.part_one_solution())
    # print(solution.part_two_solution())
    print(solution)
