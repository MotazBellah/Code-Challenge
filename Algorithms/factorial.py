def factorial(n):
    # Base Case
    if n == 0:
        return 1
    # Recursion
    else:
        return n * factorial(n-1)

print(factorial(5))



# Memoization effectively refers to remembering ("memoization" -> "memorandum" -> to be remembered)
# results of method calls based on the method inputs and
# then returning the remembered result rather than computing the result again
# Create cache for known results
factorial_memo = {}

def factorial_memoization(k):

    if k < 2:
        return 1

    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)

    return factorial_memo[k]
