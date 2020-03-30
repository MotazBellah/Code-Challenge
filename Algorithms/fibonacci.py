def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# print(fib_rec(10))


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

print(fib_dyn(11))
