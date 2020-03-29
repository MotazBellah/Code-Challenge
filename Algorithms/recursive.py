# Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
def rec_sum(n):
    if n == 0:
        return 0

    else:
        return n + rec_sum(n-1)

print(rec_sum(4))

# Given an integer, create a function which returns the sum of all the individual digits in that integer.
# For example: if n = 4321, return 4+3+2+1
def sum_func(n):
    if n < 1:
        return 0

    else:
        return n%10 + sum_func(n // 10)

print(sum_func(4321))
print(sum_func(432001))
print(sum_func(41))
