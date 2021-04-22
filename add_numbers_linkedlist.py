"""
Approach 1: get the numbers from the linkedlist. iterate through and store the values in a list. and reverse the list and join the items to form the non negative integer.
once we have both the numbers, convert to string and reverse it. then create a new linked list with values of the char
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


def addTwoNumbers(l1, l2):
    a1 = []
    a2 = []
    while l1:
        a1.append(str(l1.val))
        l1 = l1.next
    while l2:
        a2.append(str(l2.val))
        l2 = l2.next
    s1 = ''.join(a1[::-1])
    s2 = ''.join(a2[::-1])
    n = int(s1) + int(s2)
    s = str(n)
    s = s[::-1]
    head = create_linkedlist(s)
    return head



l1 = [2,4,3]
l2 = [5,6,4]
l1 = create_linkedlist(l1)
l2 = create_linkedlist(l2)
head = addTwoNumbers(l1, l2)
print()