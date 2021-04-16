"""
Approach 1: given 2 sorted linked list merge a sorted list. list 1 and list 2. pick an node from list 2 and insert at appropriate location in list 1
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


def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if not l1 and not l2:
        return
    head_1 = l1
    while l2:
        while l1:
            if l2.val < l1.val:
                temp = l2.next
                l1.val,l2.val,l1.next,l2.next = l2.val,l1.val,l2,l1.next
                l2 = temp
                break
            elif l1.next is None:
                l1.next = l2
                l2 = None
                break
            l1 = l1.next
    return head_1


x = []
y = []
x = create_linkedlist(x)
y = create_linkedlist(y)
head = mergeTwoLists(x,y)
print()