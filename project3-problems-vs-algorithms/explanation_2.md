# Explanation 2
We can do a modified binary search on a rotated list.

First, we determine if the list is ordered by checking if `a[left] < a[right]`.  
If it's ordered, we do binary search.

If the list is not ordered, it's rotated.  In this case, we split the list into two halves
and observe that at least one of the halves will be ordered.  Choose an arbitrary half,
for example the left half, and see if it's the ordered list.  If it is, and the target number
falls within it's range, do binary search on it.  Otherwise, recursively search the other
(right) half.

Since we are dividing the list in 2 at each pass, this algorithm has the same complexity
as binary search: `O(log(n))`.  The space complexity is the size of the array, `O(n)`.