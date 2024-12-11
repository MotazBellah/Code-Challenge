class PrintQueue:
    def __init__(self):
        with open("day_5.txt", 'r') as f:
            self.rules = []
            self.page_numbers = []
            for line in f:
                if "|" in line:
                    self.rules.append([int(i) for i in line.strip().split("|")])
                elif "," in line:
                    self.page_numbers.append([int(i) for i in line.strip().split(",")])
                else:
                    continue

    def _create_pair(self, a, b):
        return [a, b] if a < b else [b, a]

    def check_rules(self, lst):
        seen = set()
        for j in range(len(lst)):
            s = [lst[j]]
            for x in range(j+1, len(lst)):
                if j < x:
                    s = [lst[j], lst[x]]
                elif j > x:
                    s = [lst[x], lst[j]]
                else:
                    continue

                if tuple(s) in seen:
                    continue
                if s not in self.rules:
                    return False

                seen.add(tuple(s))
        return True

    def update_rules(self, lst):
        fixed = False
        seen = set()
        for j in range(len(lst)):
            s = [lst[j]]
            for x in range(len(lst)):
                if j < x:
                    s = [lst[j], lst[x]]
                elif j > x:
                    s = [lst[x], lst[j]]
                else:
                    continue

                if tuple(s) in seen:
                    continue

                if s not in self.rules:
                    lst[j], lst[x] = lst[x], lst[j]
                    fixed = True

                seen.add(tuple(s))

        return lst if fixed else None

    def get_pages(self):
        return [i for i in self.page_numbers if self.check_rules(i)]

    def sum_mid_part1(self):
        return sum(l[len(l)//2] for l in self.get_pages())

    def sum_mid_part2(self):
        s = 0
        for i in self.page_numbers:
            new = self.update_rules(i)
            if new:
                s += new[len(new)//2]

        return s







if __name__ == "__main__":
    pq = PrintQueue()
    part1 = pq.sum_mid_part1()
    part2 = pq.sum_mid_part2()

    print(part1)
    print(part2)
