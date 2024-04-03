class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def push(head, data):
    n = Node(data)
    n.next = head
    return n
def build_one_two_three():
    # Your code goes here.
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
#     return Node(None)