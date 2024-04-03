class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    if source is None:
        raise ValueError("Source list is empty")
    moved_node = source
    source = source.next
    moved_node.next = dest
    dest = moved_node
    return Context(source, dest)
