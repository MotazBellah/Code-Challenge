def palindromeRearranging(s):
    x = [i for i in set(s) if s.count(i) % 2]
    return len(x) <= 1
