# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is
# replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3,
# D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.

class CaesarCipher(object):
    def __init__(self, shift):
        self.key = shift

    def encode(self, str):
        lst = []
        for symbol in str:
            letter = symbol.lower()
            if letter.isalpha():
                num = ord(letter)
                num += self.key

                if num > ord('z'):
                    num = num - 26

                lst.append(chr(num))

            else:
                lst.append(symbol)

        return ('').join(lst).upper()

    def decode(self, str):
        lst = []
        for symbol in str:
            letter = symbol.lower()

            if letter.isalpha():
                num = ord(letter)
                num -= self.key

                if num < ord('a'):
                    num = num + 26

                lst.append(chr(num))

            else:
                lst.append(letter)

        return ('').join(lst).upper()
