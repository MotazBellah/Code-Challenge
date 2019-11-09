import itertools
import unittest
# you have to create all permutations of an input string and remove duplicates,
# if present. This means, you have to shuffle all letters from the input in all possible orders.

def permutations(string):
    # use itertools bilt-in lib
    y = ["".join(i) for i in list(itertools.permutations(string))]
    # remove the dublicates
    return list(set(y))


class TestPermutation(unittest.TestCase):

    def test_permutations(self):
        self.assertEqual(sorted(permutations('a')), ['a'])
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


if __name__ == '__main__':
    unittest.main()
