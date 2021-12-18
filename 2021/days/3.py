from solution import Solution

PART_ONE_DATA = './2021/data/3-1.txt'
PART_TWO_DATA = './2021/data/3-2.txt'

class DayThree2021(Solution):
    def __init__(self):
        super().__init__(PART_ONE_DATA, PART_TWO_DATA)

    def part_one_solution(self):
        # 2967914
        import numpy as np
        from scipy import stats
        parsed_data = np.array([np.array([int(c) for c in s]) for s in [line for line in self.part_one_data.split('\n') if line]])
        flip = {'0': '1', '1': '0'}

        most_common_bitstring = ''.join(str(s) for s in stats.mode(parsed_data).mode[0])
        least_common_bitstring = ''.join([flip[s] for s in most_common_bitstring])
        most_common_bitstring = int(most_common_bitstring, 2)
        least_common_bitstring = int(least_common_bitstring, 2)

        gamma_rate = most_common_bitstring
        epsilon_rate = least_common_bitstring

        return gamma_rate * epsilon_rate
        

    def part_two_solution(self):
        # 7041258
        import numpy as np
        from scipy import stats
        parsed_data = np.array([np.array([int(c) for c in s]) for s in [line for line in self.part_two_data.split('\n') if line]])
        flip = {'0': '1', '1': '0'}

        def identify_str(remaining_array, index, most_toggle = True):
            if remaining_array.shape[0] == 1: return ''.join([str(s) for s in remaining_array[0]])

            target_bitstring,num_occurences = stats.mode(remaining_array)
            target_bit, num_occurences = target_bitstring[0][index], num_occurences[0][index]


            target_bit = target_bit if most_toggle else 1 - target_bit
            target_bit = target_bit if num_occurences != remaining_array.shape[0] / 2 else (1 if most_toggle else 0)

            remaining_array = np.array([array for array in remaining_array if array[index] == target_bit])

            return identify_str(remaining_array, index + 1, most_toggle=most_toggle)
        oxygen_string = identify_str(np.copy(parsed_data), 0)
        oxygen_generator_rating =  int(oxygen_string, 2)

        co2_string = identify_str(np.copy(parsed_data), 0, False)
        co2_scrubber_rating =  int(co2_string, 2)

        return oxygen_generator_rating * co2_scrubber_rating

if __name__ == '__main__':
    solution = DayThree2021()
    # print(solution.part_one_solution())
    print(solution)
