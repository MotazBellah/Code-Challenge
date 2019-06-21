# Problem 1

To implement the LRU, two data structures were used:
1. A doubly-linked list
1. A dictionary


These two data structures work together and contain the same data.  The linked list is used
for modeling access history, and the dictionary is used for O(1) lookups.
Each node in the linked list contains both the key and value of a cache item.  This is so that
when an item expires (by falling off the end of the list), it's key can be used to remove
the corresponding dictionary item.

Dictionary values are pointers to linked list nodes.  This enables direct access to 
the relevant nodes when rearranging the list.

For  `put(key, value)` operations, we first check to see if there was already a 
`value` associated with `key`.  If so, the `(key, value)` node is removed from the list.  
The new `(key, value)` node is added to the head of the list, and `key -> (key, value)` 
is added to the dictionary.  Finally, if the list is over capacity, we remove the tail
of the list and the corresponding item in the dictionary.

For `get(key)` operations that don't hit, we return -1.  For those that hit, we find the 
corresponding linked list node and move it to the front of the list.  We then return the
`value` associated with `key`.

All operations are `O(1)` in time.  Storage required is `O(n)`, where `n` is the size of
the cache history.