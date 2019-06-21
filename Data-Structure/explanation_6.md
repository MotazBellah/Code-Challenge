# Problem 6

## Intersection
Intersecting two lists involves iterating over each list and adding each element to a per-list set, then iterating over
the intersection between the sets to generate a new list.  This requires `O(m + n)` time and `O(m + n)` space, where `m`
is the size of the first list, and `n` is the size of the second list.

## Union
Creating the union of two lists involves iterating over each list and adding each element to a set, then iterating over
the set to generate a new list.  This requires `O(m + n)` time and `O(m + n)` space, where `m` is the size of the first
list, and `n` is the size of the second list.
