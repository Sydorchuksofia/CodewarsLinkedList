class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s is 'None':
        return None
    nodes = s.split(" -> ")
    head = Node(int(nodes[0]))
    current = head
    for i in range(1, len(nodes)-1):
#         if nodes[i] == None:
#             nodes[i] = 'nul'
        current.next = Node(int(nodes[i]))
        current = current.next
    return head