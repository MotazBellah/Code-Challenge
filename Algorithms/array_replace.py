# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
# Example

# For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
# arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
import unittest

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i, v in enumerate(inputArray):
        if v == elemToReplace:
            inputArray[i] = substitutionElem

    return inputArray


class TestPalindromeRearranging(unittest.TestCase):

    def test_palindromeRearranging(self):
        self.assertEqual(arrayReplace([1, 2, 1], 1, 3),[3, 2, 3])
        self.assertEqual(arrayReplace([1, 2, 3, 4, 5], 3, 0),[1, 2, 0, 4, 5])
        self.assertEqual(arrayReplace([1, 1, 1], 1, 10),[10, 10, 10])

if __name__ == '__main__':
    unittest.main()
