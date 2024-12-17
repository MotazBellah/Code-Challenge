class BridgeRepair:
    def read_input(self):
        with open("input.txt", 'r') as f:
            for line in f:
                x = [i for i in line.strip().split(":")]
                lhs = int(x[0])
                rhs = [int(i) for i in x[1].split()]
                yield (lhs, rhs)

    def part1(self):
        total = 0
        for lhs, rhs in self.read_input():
            left_numbers = [rhs.pop(0)]
            while rhs:
                curr = rhs.pop(0)
                check = []

                for n in left_numbers:
                    check.append( n + curr)
                    check.append( n * curr)
                left_numbers = check

            if lhs in left_numbers:
                total += lhs
        return total

    def part2(self):
        total = 0
        for lhs, rhs in self.read_input():
            left_numbers = [rhs.pop(0)]
            while rhs:
                curr = rhs.pop(0)
                check = []

                for n in left_numbers:
                    check.append( n + curr)
                    check.append( n * curr)
                    check.append( int(str(n) + str(curr)),)
                left_numbers = check

            if lhs in left_numbers:
                total += lhs
        return total







if __name__ == "__main__":
    r = BridgeRepair()
    part1 = r.part1()
    part2 = r.part2()

    print(part1)
    print(part2)
