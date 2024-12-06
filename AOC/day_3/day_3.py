import re

def mul(a, b):
        return a * b

class MullOver:
    def read_input(self):
        with open("input_3.txt", 'r') as f:
            for line in f:
                yield line

    def get_mul_part1(self):
        total = 0
        for i in self.read_input():
            pattern = r"mul\(\d+,\d+\)"
            total += sum(eval(m) for m in re.findall(pattern, i))

        return total

    def get_mul_part2(self):
        muls = []
        skip = False
        pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
        for i in self.read_input():
            matches = re.findall(pattern, i)

            for match in matches:
                if match == "don't()":
                    skip = True
                elif match == "do()":
                    skip = False
                elif not skip and match.startswith("mul"):
                    muls.append(eval(match))

        return sum(muls)



if __name__ == "__main__":
    r = MullOver()
    part1 = r.get_mul_part1()
    part2 = r.get_mul_part2()
