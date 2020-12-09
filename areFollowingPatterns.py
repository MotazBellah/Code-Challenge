def areFollowingPatterns(strings, patterns):
    if len(set(strings)) != len(set(patterns)):
        return False

    d = {}
    for i in range(len(strings)):
        if patterns[i] in d:
            if d[patterns[i]] != strings[i]:
                return False
        else:
            d[patterns[i]] = strings[i]
    return True


def areFollowingPatterns(strings, patterns):
    return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))
