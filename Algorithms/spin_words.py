def spin_words(sentence):
    word_list = []
    for i in sentence.split():
        if len(i) >= 5:
            word_list.append(i[::-1])
        else:
            word_list.append(i)

    return " ".join(word_list)
