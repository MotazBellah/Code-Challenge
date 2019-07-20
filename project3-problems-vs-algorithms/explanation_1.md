# Explanation 1
To find the square root of a number `n` we can use binary search, where we are searching for an integer
whose square is greater than or equal to `n`, and who's successor's square is less than `n`.  For example
if `n = 21`, `4` satisfies the equation `4^2 <= 21 < (4+1)^2`.  Since binary search is `O(log(n))`
in the worst case, this algorithm is `O(log(n))`.

Note that if we wanted increased precision, we could get an extra decimal of precision
by subdividing the "found" cell into 10 cells and doing binary search on this new subarray.
This process takes `O(log(10)) = O(1)` time.  We could continue this process for `m` precision
points, resulting in a runtime of `O(log(n)) + O(m)`.

The space complexity is of this algorithim is `O(1)` since we are not materializing an array
of numbers. 