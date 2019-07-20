# Explanation 4

In this problem we first copy the list and the sort it in-place as we traverse the list.
We maintain three pointers, `p0`, `p2`, and `i`.  Everything to the left
of `p0` is `0`s and everything to the right of `p2` is `2`s.  Everything to the left of `i` is 
sorted, and is either a `0` or a `1`.  

The strategy is to iterate until `i` passes `p2`.  At each iteration, we examine the current element,
`a[i]`.  There are 3 cases:
1. If `a[i]` is `0` it belongs on the left side.   We swap `a[i]` with `a[p0]`, and increment `p0`.  
If `p0 > i`,
everything to up to and including `i` is `0`s and so we can increment `i` (or just set `i = p0`).

1. If `a[i]` is `1`, everything up to and including `i` is sorted since `p0 <= i` 
and `a[j] = 0` for all `j < p0`,
and `a[k] = 1` for all `p0 < p0 <= i`.  Therefore we can increment `i`.

1. If `a[i]` is `2`, we swap `a[i]` with `a[p2]` and decrement `p2`.

The runtime of the algorithm is `O(n)`.  To see this, observe that at each step, we are either
incrementing `p0`, incrementing `i`, or decrementing `p2`.  Since `i` is incremented once
`p0` catches up to `i`, `i` won't be stationary more than `n` turns.  

The space complexity of the algorithm is `O(n)`.

Note there is an alternative algorithm which just counts the number of `0`s, `1`s, and `2`s, then 
fills in the array with the appropriate number of each digit.