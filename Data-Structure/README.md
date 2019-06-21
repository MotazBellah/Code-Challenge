# Show-Me-the-Data-Structures.
Project 2 for the Algorithms &amp; Data Structures.

This project cover a variety of topics related to the data structures. I have written clean and efficient answer in Python, as well as a text explanation of the efficiency of my code and my design choices.

## 1. Least Recently Used Cache
Least Recently Used (LRU) cache is a type of cache in which we remove the least recently used entry when the cache memory reaches it's limit.
For this first problem I designed a data structure known as Least Recently Used (LRU) cache. I have to use appropriate data structure(s) to implement the cache.

- In case of a cache hit, your get() operation should return the appropriate value.
- In case of a cache miss, your get() should return -1.
- While putting an element in the cache, put() / set() operation must insert the element. If the cache is full, I need to remove the least recently used entry first and then insert the element.

All operations must take O(1) time.

## 2. Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

## 3. Huffman Coding
Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding scheme is also lossless meaning that when compressing the data to make it smaller that there is no loss of information. The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman codes can be of any length and does not require a prefix, therefore this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode code for this algorithm. At the basic core it is comprised of building a Huffman tree, encoding the data and lastly decoding the data.

Here is one type of pseudocode for this coding schema:

- Take string and determine the relevant frequencies of the characters
- Builds and sort a list of tuples from lowest to highest frequencies.
- Build the Huffman Tree by assigning a binary code to each letter using shorter codes for the more frequent letters. This is the heart of the Huffman algorithm.
- Trim the Huffman Tree (Remove the frequencies from the previously built tree)
- Encode the text into its compressed form
- Decode the text from its compressed form

[Huffman Visualization!](https://people.ok.ubc.ca/ylucet/DS/Huffman.html)
[Tree Generator](http://huffman.ooz.ie/)
[Additional Explanation](https://www.siggraph.org/education/materials/HyperGraph/video/mpeg/mpegfaq/huffman_tutorial.html)

## 4. Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.
In this problem I have written a function that provides an efficient look up of wether the use is in a group.

## 5. Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created and text strings as the data.

We can breakdown the blockchain down into having 3 main parts.
- First is the information hash
- The next main component is the block on the blockchain
- Finally link all of this together in a block chain

## 6. Union and Intersection of Two Linked Lists
In this problem I had to write the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

I had taken in the the two linked lists and return a linked list that is composed of either the union or intersection respectively.
