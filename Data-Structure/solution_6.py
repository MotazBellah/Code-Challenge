class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    set1 = set()
    set2 = set()

    def add_to_set(llist, s):
        p = llist.head
        while p:
            s.add(p.value)
            p = p.next

    add_to_set(llist_1, set1)
    add_to_set(llist_2, set2)

    res = LinkedList()
    for e in set1.union(set2):
        res.append(e)

    return res


def intersection(llist_1, llist_2):
    set1 = set()
    set2 = set()

    def add_to_set(llist, s):
        p = llist.head
        while p:
            s.add(p.value)
            p = p.next

    add_to_set(llist_1, set1)
    add_to_set(llist_2, set2)

    res = LinkedList()
    for e in set1.intersection(set2):
        res.append(e)

    return res


def test_case_1():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


def test_case_2():
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))


def test_case_3():
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))


if __name__ == '__main__':
    test_case_1()
    # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
    # 4 -> 21 -> 6 ->

    test_case_2()
    # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->

    test_case_3()
    # <nothing>
