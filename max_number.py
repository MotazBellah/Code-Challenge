def solution(N):
    s = str(N)
    if N < 0:
        s = s[1:]
        for k, v in enumerate(s):
            if v >= '5':
                return int("-" + s[:k] + '5' + s[k:])
        return int('-' + s + '5')

    for k, v in enumerate(s):
        if v <= '5':
            return int(s[:k] + '5' + s[k:])

    return int(s + '5')
