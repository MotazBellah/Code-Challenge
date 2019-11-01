import re
def palindrome(word):
    clear_word = re.sub(r'\W','',word).lower()
    return clear_word == clear_word[::-1]
