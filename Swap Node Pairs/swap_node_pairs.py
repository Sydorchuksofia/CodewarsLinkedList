class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    d = Node(0)
    d.next = head
    prev = d
    curr = head
    while curr and curr.next:
        # Nodes to be swapped
        first = curr
        second = curr.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
        curr = first.next
    return d.next