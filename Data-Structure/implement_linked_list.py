class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

# Traversing the list
def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

print_linked_list(head)
# print(head.value)
# print(head.next.value)
# print(head.next.next.value)
# print(head.next.next.next.value)
# print(head.next.next.next.next.value)

# Creating a linked list using iteration
# See if you can write the code for the create_linked_list function below
# The function should take a Python list of values as input and return the head of a linked list that has those values
def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    for i in input_list:
        if head is None:
            head = Node(i)
        else:
            # Move to the tail
            current_node = head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(i)

    return head


def create_linked_list_better(input_list):
    head = None
    tail = None

    for i in input_list:
        if head is None:
            head = Node(i)
            tail = head  # when we only have 1 node, head and tail refer to the same node
        else:
            tail.next = Node(i)  # attach the new node to the `next` of tail
            tail = tail.next  # update the tail

    return head
