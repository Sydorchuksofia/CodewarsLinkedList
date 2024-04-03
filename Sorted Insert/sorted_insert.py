class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    new_node = Node(data)
    if head is None or head.data >= data:
        new_node.next = head
        return new_node
    current = head
    while current.next and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head