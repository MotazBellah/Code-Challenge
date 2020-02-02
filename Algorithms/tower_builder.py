# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
#
# Tower block is represented as *
# for example, a tower of 3 floors looks like below
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]

def tower_builder(n):
    tower = []
    count = 0
    for i in range(n):
        floor = ' ' *(n-i-1)+ '*' + (count* '*') + ' ' *(n-i-1)
        count += 2
        tower.append(floor)
    return tower
