class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def loop_size(node):
    if not node or not node.next:
        return 0
    slow = node.next
    fast = node.next.next
    counter = 1
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    slow = slow.next
    while slow != fast:
        counter +=1
        slow = slow.next
    return counter