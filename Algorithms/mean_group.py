from itertools import permutations, product, combinations

def concatenationsSum2(a):
    x = []
    for i in a:
        for j in a:
            x.append(str(i) + str(j))

    return sum(int(i) for i in x)

def concatenationsSum3(a):
    return sum(int(str(i) + str(j)) for i in a for j in a)

def concatenationsSum(a):
    return list(combinations(a, r=4))


print(concatenationsSum([10, 2]))
