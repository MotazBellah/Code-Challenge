# In this kata you have to create all permutations of an input string and remove duplicates, if present.
# This means, you have to shuffle all letters from the input in all possible orders.

def permutations(string):
    if len(string) == 1:
        return set(string)
    first = string[0]
    rest = permutations(string[1:])
    result = set()
    for i in range(0, len(string)):
        for p in rest:
            result.add(p[0:i] + first + p[i:])
    return result



# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
