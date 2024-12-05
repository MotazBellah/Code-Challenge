class Reports:
    def read_input(self):
        with open("input_2.txt", 'r') as f:
            for line in f:
                x = [int(i) for i in line.split()]
                yield x

    def is_safe(self, lst):
        is_dec = is_inc = False
        for i in range(1, len(lst)):
            diff = lst[i] - lst[i - 1]

            if diff == 0:
                return False
            if abs(diff) > 3:
                return False

            if diff < 0:
                is_dec = True
            else:
                is_inc = True

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
                    removed_item = data.pop(i)
                    if self.is_safe(data):
                        safe += 1
                        break
                    data.insert(i, removed_item)
        return safe

    def check_report(self):
        return sum(1 for i in self.read_input() if self.is_safe(i))

if __name__ == "__main__":
    r = Reports()
    part1 = r.check_report()
    part2 = r.reactor_mounted()
    print(part1)
    print(part2)