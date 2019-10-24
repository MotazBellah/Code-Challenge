import re
import unittest
# "Any word or phrase that exactly reproduces the letters in another order is an anagram." (Wikipedia).
# Add numbers to this definition to be more interest.
# The challenge is to write the function isAnagram
# to return True if the word test is an anagram of the word original and False if not.

def isAnagram(test, original):
    # make sure the phrases in the Lowercase
    a = test.lower()
    b = original.lower()
    # Get only the letters and numbers using regex
    # if the sorted phrases are equal, return true
    return sorted("".join(re.findall(r'[a-z0-9]+',a)))== sorted("".join(re.findall(r'[a-z0-9]+',b)))


class TestIsAnagram(unittest.TestCase):

    def test_is_anagran(self):
        self.assertEqual(isAnagram("William Shakespeare","I am a weakish speller"), True)
        self.assertEqual(isAnagram("Silent","Listen"), True)
        self.assertEqual(isAnagram("Car","Cat"), False)
        self.assertEqual(isAnagram("12345","54321"), True)


if __name__ == '__main__':
    unittest.main()
