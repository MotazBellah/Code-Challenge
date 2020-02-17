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
