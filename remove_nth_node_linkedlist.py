"""
Approach 1: iterate through the linked list with head node. put those nodes in a list. now pick the node from list from the end, this is the node to be deleted.
node to be deleted must be replaced with the value of next node to it and delete the next node. the next.next node is current node's next
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linkedlist(lt):
    previous = head = None
    for item in lt:
        current = ListNode(item)
        if head is None:
            head = current
        if previous is not None:
            previous.next = current
        previous = current
    return head

def removeNthFromEnd(head, n):
    node_list = []
    while head:
        node_list.append(head)
        head = head.next
    node_to_delete = node_list[-n]
    if node_to_delete.next:
        node_to_delete.val = node_to_delete.next.val
        node_to_delete.next = node_to_delete.next.next
    elif node_list[0] == node_to_delete: # first node
        node_list.clear()
        del node_to_delete
    else:
        previous = node_list[-n-1]
        previous.next = None
        del node_to_delete
    if len(node_list) > 0:
        return node_list[0]
    return None


x = [1]
n = 1
head = create_linkedlist(x)
new_head = removeNthFromEnd(head, n)
print(new_head)

        