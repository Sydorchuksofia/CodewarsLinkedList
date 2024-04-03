class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(head, index):
    if head is None:
        raise ValueError("Linked list is empty")
    current = head
    count = 0
    while current:
        if count == index:
            return current
        current = current.next
        count += 1
    raise ValueError("Index out of range")