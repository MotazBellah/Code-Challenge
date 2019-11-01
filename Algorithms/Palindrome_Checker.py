import re
import unittest

# Write a function palindrome which returns true
# if the string passed to it is a palindrome and false otherwise.
# The function should ignore case and all non-alphabetical characters
# (including spaces, punctuation marks and numbers).

def palindrome(word):
    # get only the string letters
    clear_word = re.sub(r'\W','',word).lower()
    # return true if the word equal to the reversed word
    return clear_word == clear_word[::-1]



class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertEqual(palindrome(''), False)
        self.assertEqual(palindrome("bob"), True)
        self.assertEqual(palindrome("banana"), False)
        self.assertEqual(palindrome("Madam In Eden, I’m Adam"), True)


if __name__ == '__main__':
    unittest.main()
