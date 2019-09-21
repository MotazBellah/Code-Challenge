import operator
import unittest

# Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
#
# For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
#
# For your convenience, the input is formatted such that a space is provided between every token.
#
# Empty expression should evaluate to 0.
#
# Valid operations are +, -, *, /.
#
# You may assume that there won't be exceptional situations (like stack underflow or division by zero).

def polish_notation(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            print(op1, op2)
            stack.append(OPERATORS[token](op2,op1))
        elif token:
            stack.append(float(token))
    return stack.pop()


class TestPolishNotation(unittest.TestCase):

    def test_notation(self):
        self.assertEqual(polish_notation('3.5'), 3.5)
        self.assertEqual(polish_notation('1 3 +'), 4)
        self.assertEqual(polish_notation('1 3 *'), 3)
        self.assertEqual(polish_notation('1 3 -'), -2)
        self.assertEqual(polish_notation('4 2 /'), 2)



if __name__ == '__main__':
    unittest.main()
