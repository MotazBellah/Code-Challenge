# Given a string, find out if its characters
# can be rearranged to form a palindrome
import unittest

def palindromeRearranging(s):
    x = [i for i in set(s) if s.count(i) % 2]
    return len(x) <= 1


class TestPalindromeRearranging(unittest.TestCase):

    def test_palindromeRearranging(self):
        self.assertEqual(palindromeRearranging("aabb"),True)
        self.assertEqual(palindromeRearranging("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"),False)
        self.assertEqual(palindromeRearranging("abbcabb"),True)
        self.assertEqual(palindromeRearranging("z"),True)
        self.assertEqual(palindromeRearranging("abdhuierf"),False)


if __name__ == '__main__':
    unittest.main()
