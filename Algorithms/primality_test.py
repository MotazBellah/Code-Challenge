# Create the function prime that returns true when the given input is prime,
# and false when it is composite.
# All inputs will be positive integers.

def prime(n):
    return all(n%i for i in range(2,int(n**.5)+1))
