import string
import unittest

# Complete the function/method so that it takes CamelCase string
# and returns the string in snake_case notation.
# Lowercase characters can be numbers. If method gets number, it should return string.

def to_underscore(s):
    # Make sure the input is a string
    # if not return string
    if str(s) in string.digits:
        return str(s)
    # Lowercase the fist character
    s = s[0].lower() + s[1:]
    # convert the string to List(mutable DS)
    new = list(s)
    # Get the upper case characters
    # Get the index for each one and insert _ before it
    u = [i for i in new if i.isupper()]
    for i in u:
        n = new.index(i)
        new.insert(n, '_')

    return "".join(new).lower()


class TestToUnderscore(unittest.TestCase):

    def test_tounderscore(self):
        self.assertEqual(to_underscore('TestController'), 'test_controller')
        self.assertEqual(to_underscore('MoviesAndBooks'), 'movies_and_books')
        self.assertEqual(to_underscore('App7Test'), 'app7_test')
        self.assertEqual(to_underscore(1), '1')


if __name__ == '__main__':
    unittest.main()
