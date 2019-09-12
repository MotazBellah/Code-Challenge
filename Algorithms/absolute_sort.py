# The array (a tuple) has various numbers.
# You should sort it, but sort it by absolute value in ascending order.
# For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20)

def abs_sort(n):
    return sorted(n, key=abs)


print abs_sorting((-20, -5, 10, 15))
