class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return


    def to_list(self):
        values_list = []
        current_node = self.head

        while current_node is not None:
            values_list.append(current_node.value)
            current_node = current_node.next

        return values_list


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next
