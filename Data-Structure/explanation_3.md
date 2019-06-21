# Problem 3

## Tree Construction
We build a Huffman Tree in 2 phases- frequency analysis and tree building.

### Frequency Analysis
Frequency analysis entails building a map of counters, with one map bucket per character in the
character set.  This process requires a single scan across the text, so has `O(n)` runtime,
where `O(n)` is the number of characters in the text to be analyzed.  The space requirements
are `O(v)`, where `v` is the number of unique characters in the text.

### Tree Building
We build a tree with one leaf per character in the character set.  A balance binary tree with
`n` leaves has `2*n - 1` nodes, so the space requirement is `O(n)`.  Building the tree 
consists of a set of merge steps.  Each merge step requires popping 2 nodes off a heap.
Building the heap takes `O(n * log(n))` and each merge step takes `O(1)` time.  The number
of merge steps is about the same as the number of nodes in the tree.  Therefore the 
time to build the tree is `O(n * log(n)) + O(n) = O(n * log(n))`

## Operations
The two operations are encoding and decoding.

## Encoding
Encoding a sequence of characters entails generating a bit string for each character in the sequence.
The time to generate a bit sequence is the time to traverse the tree from a leaf to the root, which 
is `O(log(v))`, where `v` is the size of the character set.  Therefore the total runtime is
`O(n * log(v))` where `n` is the number of characters to decode.

## Decoding
Decoding a bitstring entails one tree traversal step per bit.  Therefore the runtime of decoding 
is `O(n)`, where `n` is the number of bits to decode.
