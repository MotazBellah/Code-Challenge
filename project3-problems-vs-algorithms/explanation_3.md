# Explanation 3

The solution is in two steps. At first the array is sorted, in order to be able to find the largest sums in the second step. For sorting, I picked the quicksort algorithm. The sum is then simply formed by traversing the array and multiplying the factor by 10 at every second step.

Quicksort has a time complexity of `O(n log n)`, when the rare worst case is ignored, so the overall complexity is `O(n log(n) + n) = O(n log n)`. This algorithm has a space complexity of   `O(n)`, as it is just re-arranging the input array in place.
