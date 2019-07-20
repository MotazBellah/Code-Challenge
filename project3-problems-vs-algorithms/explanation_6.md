# Explanation 6


We intialize the current minimum and maximum to `None`.
We then iterate over the array, and at each element, we compare the current element to the saved minimum and
maximum.  If the element is less than the current minimum, or if the current minimum is `None`, we update
the current minimum with the current element.  Similarly if the element is greater than the current maximum,
or if the current maximums is `None`, we update the current maximum with the current element.

The runtime is `O(n)`.  The space complexity is `O(n)`.