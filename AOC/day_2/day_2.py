class Reports:
    def read_input(self):
        with open("input_2.txt", 'r') as f:
            for line in f:
                x = [int(i) for i in line.split()]
                yield x

    def is_safe(self, lst):
        is_dec = False
        is_inc = False
        for i in range(1, len(lst)):
            if lst[i] < lst[i-1]:
                is_dec = True
                c = lst[i-1] - lst[i]
            elif lst[i] > lst[i-1]:
                is_inc = True
                c = lst[i] - lst[i-1]
            else:
                return False
            if c > 3:
                return False
            if is_dec and is_inc:
                return False
        return True

    def reactor_mounted(self):
        safe = 0
        for data in self.read_input():
            if self.is_safe(data):
                safe += 1
            else:
                for i in range(len(data)):
                    tolerated_levels = data[:i] + data[i + 1:]
                    if self.is_safe(tolerated_levels):
                        safe += 1
                        break
        return safe

    def check_report(self):
        return sum(1 for i in self.read_input() if self.is_safe(i))

if __name__ == "__main__":
    r = Reports()
    part1 = r.check_report()
    part2 = r.reactor_mounted()
    print(part1)
    print(part2)