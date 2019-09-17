import unittest

# Add two English words together
# Input - Will be between zero and ten and will always be in lower case
# Output - Word representation of the result of the addition. Should be in lower case

class Arith():
    def __init__(self, word):
        self.word = word

    def add(self, x):
        """Function to add two words and return total in number
        input: (string) number in word (zero, one,..)
        output: (integer) return the total in number"""

        numbers = {'zero': 0, 'one': 1, 'two': 2,
                   'three': 3, 'four': 4, 'five': 5,
                   'six': 6, 'seven': 7, 'eight': 8,
                   'nine': 9, 'ten': 10,'eleven': 11,
                   'twelve': 12, 'thirteen': 13, 'fourteen':14,
                   'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
                   'eighteen': 18, 'nineteen': 19, 'twenty': 20}
        # get the value of initialized word and added word from numbers dict
        total = numbers.get(self.word) + numbers.get(x)
        # get the key from numbers dict that related to the total number
        return [k for k, v in numbers.items() if v == total][0]


class TestArith(object):

    def test_notation(self):
        i = Arith("three") # Declare Arith Class

        self.assertEqual(i.add("seven"), "ten")
        self.assertEqual(i.add("eight"), "eleven")
        self.assertEqual(i.add("zero"), "three")


if __name__ == '__main__':
    unittest.main()
