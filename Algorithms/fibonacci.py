# Solve the problem using simple recursion
def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# print(fib_rec(10))

# Implement the function using dynamic programming to store results (memoization).
memo = {}

def fib_dyn(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if not n in memo:
            memo[n] = fib_rec(n-1) + fib_rec(n-2)

        return memo[n]

# print(fib_dyn(5))

# Implement the solution with simple iteration.
def fib_iter(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a

print(fib_iter(8))
