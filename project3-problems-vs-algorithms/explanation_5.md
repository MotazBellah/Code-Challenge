# Explanation 5

Insertion of a word into the trie takes `O(n)` time, where `n` is the number of characters in the word.

Lookup of a prefix node takes `O(n)`, where `n` is the number of characters in the prefix.

Gathering of suffixes takes `O(n*m)` time, where `n` is the number of suffixes and `m` is the length of each suffix.

The space of the Trie is `O(n^m)`, where `n` is the size of the alphabet and `m` is the average branching factor,
that is the average number of unique characters following a given character. 
  