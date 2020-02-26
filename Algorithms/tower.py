# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# for example, a tower of 3 floors looks like below
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]
def tower(n):
    s = []
    c = 0
    for i in range(n):
        x = ' ' *(n-i-1)+ '*' + (c* '*') + ' ' *(n-i-1)
        c += 2
        s.append(x)
    return s

print (tower(2))
print (tower(3))
print (tower(6))
