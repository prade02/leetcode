"""
Approach 1: can not find the previous node as it is a singly linkedlist. instead the node to be deleted must be replaced with the value of next node to it and
delete the next node. the next.next node is current node's next
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return str(self.val)


def create_linkedlist(lt, value):
    previous = node_to_trace = None
    for item in lt:
        current = ListNode(item)
        if node_to_trace is None and item == value:
            node_to_trace = current
        if previous is not None:
            previous.next = current
        previous = current
    return node_to_trace


def deleteNode(node):
    node.val = node.next.val    
    node.next = node.next.next


x = [1,2,3,4]
node = 3
node = create_linkedlist(x, node)
print(node)
deleteNode(node)
print(node)
