# Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

def factorial(n):
    # Base Case
    if n == 0:
        return 1
    # Recursion
    else:
        return n * factorial(n-1)


# Use while loop
def permute(s, output=[]):
    output.append(s)
    print(len(output))
    i = 0
    while len(output) < factorial(len(s)):
        lst = list(s)
        print(lst)
        if i + 1 == len(s):
            i = 0
        lst[i], lst[i+1] = lst[i+1], lst[i]
        s = ''.join(lst)
        output.append(s)
        i += 1

    return set(output)

# Use Recursion
def permute2(s, output=[], i=0):
    output.append(s)
    print(len(output))
    if len(output) < factorial(len(s)):
        lst = list(s)
        print(lst)
        if i + 1 == len(s):
            i = 0
        lst[i], lst[i+1] = lst[i+1], lst[i]
        s = ''.join(lst)
        # output.append(s)
        i += 1
        return permute2(s, output, i)
    else:
        return list(set(output))

print(permute2('abc'))
