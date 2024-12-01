class SmallestPair:
    def __init__(self, left_l, right_l):
        self.left_l = left_l
        self.right_l = right_l


    def get_smallest_pair(self):
        unique_left  = sorted(self.left_l)
        unique_right = sorted(self.right_l)

        zip_list = zip(unique_left, unique_right)
        return zip_list

    def far_calculation(self):
        distance = self.get_smallest_pair()
        return sum(abs(i[0] - i[1]) for i in distance)

    def get_occurance(self, n):
        count = 0
        found = False
        for i in sorted(self.right_l):
            if i == n:
                found = True
                count += 1
            if i != n and found:
                break
        return n, count

    def similarity_score(self):
        d = []
        for i in self.left_l:
            d.append(self.get_occurance(i))

        return sum((i[0] * i[1]) for i in d)



if __name__ == "__main__":
    left_list = []
    right_list = []

    with open("input-1.txt", 'r') as f:
        for line in f:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))


    sp = SmallestPair(left_list, right_list)
    # Part-1
    far_calculation = sp.far_calculation()
    print(far_calculation)
    # Part-2
    similarity_score = sp.similarity_score()
    print(similarity_score)
