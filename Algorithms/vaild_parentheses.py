import unittest

def valid_parenth(s):
    if s[0] == ')' or s[-1] == '(' or len(s) % 2 != 0:
        return False
    opening = set('(')
    match = set([('(', ')')])
    stack = []
    for char in s:
        if char in opening:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            lastOpen = stack.pop()
            if (lastOpen, char) not in match:
                return False
    return len(stack) == 0


class TestParenth(unittest.TestCase):

    def test_valid_parenth(self):
        self.assertEqual(valid_parenth(")"),False)
        self.assertEqual(valid_parenth("())"),False)
        self.assertEqual(valid_parenth("()((((()())())))()"),True)


if __name__ == '__main__':
    unittest.main()


print (valid_parenth(")(()))"))
