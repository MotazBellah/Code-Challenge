import itertools
def anagrams(word, words):
    output = []
    word_permutation = [''.join(i) for i in itertools.permutations(word)]
    for w in words:
        if w in word_permutation:
            output.append(w)

    return output
