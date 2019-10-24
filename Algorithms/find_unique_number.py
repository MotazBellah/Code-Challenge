import unittest
# There is an array with some numbers.
# All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    # Get the set of the List
    set_list = set(arr)
    # Loop through the set
    # If the item in the set has shown once in the main array, return it
    for i in set_list:
        if arr.count(i) == 1:
            return i




class TestFindUnique(unittest.TestCase):

    def test_find_uniq(self):
        self.assertEqual(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
        self.assertEqual(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
        self.assertEqual(find_uniq([ 3, 10, 3, 3, 3 ]), 10)


if __name__ == '__main__':
    unittest.main()
