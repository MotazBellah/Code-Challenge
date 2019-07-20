# Explanation 7

In this problem, we leverage Tries but instead of using characters as keys, we use path components
as keys.  To handle the edge case of trailing slashes, we filter all `''`s after we split the path
on `/`.

Lookup in the router is `O(n)` where `n` is the number of path components.  Insertion is also
`O(n)`, where `n` is the number of path components.  The size of the Trie is `O(n^m)` where `n`
is the average number of path components, and `m` is the average branching factor, that is,
the average number of unique path components to succeed a given path component.