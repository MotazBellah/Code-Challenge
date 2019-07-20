from collections import defaultdict


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def insert(self, char):
        # Add a child node in this Trie
        pass

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        child_suffixes = []
        if self.is_word:
            child_suffixes.append(suffix)
        for c in self.children:
            child_suffixes += self.children[c].suffixes(suffix + c)
        return child_suffixes


def trie_test(prefix, expected_suffixes):
    trie = Trie()
    word_list = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in word_list:
        trie.insert(word)

    prefix_node = trie.find(prefix)
    if not prefix_node:
        print('No Match')
        if not expected_suffixes:
            print("Pass")
        else:
            print("Fail")
        return

    actual_suffixes = prefix_node.suffixes()
    print(actual_suffixes)
    if set(actual_suffixes) == set(expected_suffixes):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    trie_test('ant', ['', 'hology', 'agonist', 'onym'])
    # ['', 'hology', 'agonist', 'onym']
    # Pass

    trie_test('f', ['un', 'unction', 'actory'])
    # ['un', 'unction', 'actory']
    # Pass

    trie_test('x', [])
    # No Match
    # Pass
