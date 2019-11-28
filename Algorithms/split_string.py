def solution(s):
    lst = []
    if len(s) == 0:
        return lst
    else:
        if len(s) % 2 != 0:
            s += "_"
        i, j = 0, 0
        while len(lst) < len(s) / 2:
            i, j = j, j + 2
            lst.append(s[i:j])

    return lst
