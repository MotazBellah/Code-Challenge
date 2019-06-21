In this problem I have to create a chain of blocks that is a linked list.
I have created a class for creating the linked list. I have initialized the linked list with head and tail. Head points to the starting of the chain while tail points to the end of linked list. I have used Tail of the linked list to add the next block in O(1) time.

Linked list are implemented as shown in the figure (in the classroom) ie each block points to its previous block and not the next block. (ie in the reversed order)

Space complexity: O(n) - total space occupied by the blockchain
Time complexity: O(1) - for appending a block
