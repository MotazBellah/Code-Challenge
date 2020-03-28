def balance_check(s):
    open = ['(', '{', '[']
    match = ['()', '[]', '{}']

    stack = []

    for i in s:
        if i in open:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            x = stack.pop() + i
            if x not in match:
                return False

    return len(stack) == 0




print(balance_check('()[(])'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))
