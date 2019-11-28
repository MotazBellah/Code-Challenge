# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters
# then it should replace the missing second character of the final pair with an underscore ('_').

def solution(s):
    lst = []
    if len(s) == 0:
        return lst
    else:
        if len(s) % 2:
            s += "_"
        i, j = 0, 0
        while len(lst) < len(s) / 2:
            i, j = j, j + 2
            lst.append(s[i:j])

    return lst
