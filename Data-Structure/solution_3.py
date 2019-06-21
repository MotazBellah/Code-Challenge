import sys
from collections import Counter
from heapq import heappop, heappush


class Node:
    def __init__(self, left, right, value, char=None):
        self.value = value
        self.char = char
        self.left = left
        self.right = right
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def is_leaf(self):
        return self.char is not None

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


class Tree:
    def __init__(self, root):
        self.root = root
        self.char_to_leaf = {}
        self.build_char_to_leaf()

    def build_char_to_leaf(self):
        if not self.root:
            return

        def helper(n):
            if n.is_leaf():
                self.char_to_leaf[n.char] = n
            else:
                helper(n.left)
                helper(n.right)

        helper(self.root)

    # Given a char, return a string of 0's and 1's from root
    def reversed_path_from_leaf(self, char):
        if not self.root:
            return ''

        path = []
        n = self.char_to_leaf[char]
        while n != self.root:
            if n is n.parent.left:
                path.append('0')
            else:
                path.append('1')
            n = n.parent

        return ''.join(reversed(path))

    # Given a binary code, return the char associated with the prefix of the code along with the
    # non-consumed part of the code
    def char_from_path(self, code):
        if not self.root:
            return None

        code_list = list(code)
        n = self.root
        while not n.is_leaf():
            choice = code_list.pop(0)
            if choice == '0':
                n = n.left
            else:
                n = n.right
        return n.char, ''.join(code_list)

    @staticmethod
    def build_tree(string):
        if not string:
            return Tree(None)

        counter = Counter(string)
        heap = []
        for char, count in counter.items():
            node = Node(None, None, count, char)
            heappush(heap, node)

        while len(heap) > 1:
            node1 = heappop(heap)
            node2 = heappop(heap)
            node3 = Node(node1, node2, node1.value + node2.value, None)
            heappush(heap, node3)

        return Tree(heappop(heap))


def huffman_encoding(data):
    tree = Tree.build_tree(data)
    codes = [tree.reversed_path_from_leaf(c) for c in data]
    return ''.join(codes), tree


def huffman_decoding(data, tree):
    if not data:
        return None
    decoded_chars = []
    while data:
        char, data = tree.char_from_path(data)
        decoded_chars.append(char)
    return ''.join(decoded_chars)


def test_huffman(input_sentence):
    encoded_data, tree = huffman_encoding(input_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    encoded_data_size = sys.getsizeof(int(encoded_data, base=2)) if encoded_data else 0
    stats = (input_sentence == decoded_data, sys.getsizeof(decoded_data), encoded_data_size)
    print(stats)


if __name__ == '__main__':
    s1 = 'The bird is the word'
    s2 = '''Pop and return the smallest item from the heap, and also push the new item. 
    The heap size doesn’t change. If the heap is empty, IndexError is raised. This is more efficient 
    than heappop() followed by heappush(), and can be more appropriate when using a fixed-size heap.
    '''
    s3 = ''

    test_huffman(s1)
    # (True, 69, 36)

    test_huffman(s2)
    # (True, 642, 188)

    test_huffman(s3)
    # (False, 16, 0)
