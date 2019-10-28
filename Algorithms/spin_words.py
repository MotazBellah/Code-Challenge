# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words reversed .
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

def spin_words(sentence):
    # declare a list
    word_list = []
    # loop through the string
    # if the length of the word >= 5
    # then reverse it
    for i in sentence.split():
        if len(i) >= 5:
            word_list.append(i[::-1])
        else:
            word_list.append(i)

    return " ".join(word_list)
