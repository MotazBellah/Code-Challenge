# Create a function called word_split() which takes in a string phrase and a set list_of_words.
# The function will then determine if it is possible to split the string in a way in which
# words can be made from the list of words.
# You can assume the phrase will only contain words found in the dictionary if it is completely splittable.
# Use recursive
def word_split(phrase,list_of_words, output = None):
    if output is None:
        output = []

    for word in list_of_words:

        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):],list_of_words,output)

    return output

# Use recursive
def word_split2(phrase, words, output=[]):
    if not phrase:
        return output

    for word in words:
        x = phrase.split(word)
        y = ''.join(x)
        if len(x) > 1:
            output.append(word)
            return word_split(y, words[1:], output)


# Without recursive
def word_split3(phrase,list_of_words):
    word_list = []

    for word in list_of_words:
        if word in phrase:
            word_list.append(word)
            phrase.replace(word, '')

    return word_list

print(word_split('themanran',['the','ran','man']))
print(word_split('ilovedogsJohn',['am','i','a','dogs','lover','love','John']))
print(word_split('themanran',['clown','ran','man']))
