import itertools

def permutations(string):
    y = ["".join(i) for i in list(itertools.permutations(string))]
    return list(set(y))
