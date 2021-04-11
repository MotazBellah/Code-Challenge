# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python
# Given two strings s1 and s2, we want to visualize how different the two strings are.
# We will only take into account the lowercase letters (a to z).
# First let us count the frequency of each lowercase letters in s1 and s2.
# s1 = "A aaaa bb c", s2 = "& aaa bbb c d"
# s1 has 4 'a', 2 'b', 1 'c', s2 has 3 'a', 3 'b', 1 'c', 1 'd'

def mix(s1, s2):
    s = []
    lett = "abcdefghijklmnopqrstuvwxyz"
    for ch in lett:
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) >= 2:
            if val1 > val2:
                s.append("1:"+val1*ch)
            elif val1 < val2:
                s.append("2:"+val2*ch)
            else: s.append("=:"+val1*ch)

    s.sort()
    s.sort(key=len, reverse=True)
    return "/".join(s)
