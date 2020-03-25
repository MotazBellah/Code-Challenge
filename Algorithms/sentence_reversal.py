def sentence_reversal2(sentence):
    word_array = sentence.split()
    new_word = []
    for word in word_array[::-1]:
        new_word.append(word)

    return " ".join(new_word)


def sentence_reversal3(sentence):
    word_array = sentence.split()
    new_word = []
    for word in range(1, len(word_array) + 1):
        new_word.append(word_array[-word])

    return " ".join(new_word).strip()

def sentence_reversal(sentence):
    return " ".join(sentence.split()[::-1])


print(sentence_reversal(' This is the best '))
