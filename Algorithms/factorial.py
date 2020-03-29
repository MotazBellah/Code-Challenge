def factorial(n):
    # Base Case
    if n == 0:
        return 1
    # Recursion
    else:
        return n * factorial(n-1)

print(factorial(5))
