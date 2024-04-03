class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if head is None:
        return None
    cur = head
    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head