import re
import unittest

# Given a random string consisting of
# numbers, letters, symbols, you need to sum up the numbers in the string.

def sum_from_string(string):
    # Use regex to get all numbers in the string
    n = re.findall(r'[\d]+', string)
    # sum all the numbers
    return sum(int(i) for i in list(n))


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum_from_string("In 2015, I want to know how much does iPhone 6+ cost?"),2021)
        self.assertEqual(sum_from_string("1+1=2"),4)
        self.assertEqual(sum_from_string("e=mc^2"),2)
        self.assertEqual(sum_from_string("Hi"),0)


if __name__ == '__main__':
    unittest.main()
