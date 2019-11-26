# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none

import itertools
def anagrams(word, words):
    output = []
    word_permutation = [''.join(i) for i in itertools.permutations(word)]
    for w in words:
        if w in word_permutation:
            output.append(w)

    return output
