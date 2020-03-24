# Given two strings, check to see if they are anagrams
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase

def anagram_check(str1, str2):
    # ignore space and capitalizatio
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    return sorted(str1) == sorted(str2)


def anagram_check_dict(str1, str2):
    # ignore space and capitalizatio
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    # edge case check
    if len(str1) != len(str2):
        return False

    count1 = {}
    count2 = {}
    for i in range(len(str1)):
        count1[str1[i]] = str1.count(str1[i])
        count2[str2[i]] = str2.count(str2[i])

    return count1 == count2


print(anagram_check_dict('public relations', 'crap built on lies'))
print(anagram_check_dict('clint eastwood', 'old west action'))
