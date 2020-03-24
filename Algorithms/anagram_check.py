def anagram_check(str1, str2):
    # ignore space and capitalizatio
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    return sorted(str1) == sorted(str2)


print(anagram_check('public relations', 'crap built on lies'))
