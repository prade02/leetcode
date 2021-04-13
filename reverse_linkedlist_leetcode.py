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


def reverseList(head):
    if head is None:
        return None
    current = head
    previous = None
    while current.next is not None:
        current.next, previous, current = previous, current, current.next
    head, current.next = current, previous
    return head


def reverseList_recurrsive(head):
    def reverse(current, previous):
        if current.next is None:
            current.next = previous
            return current
        current.next, previous, current = previous, current, current.next
        return reverse(current, previous)
    if head is None:
        return None
    current = head
    previous = None
    return reverse(current, previous)


x = [1,2,3,4,5]
head = create_linkedlist(x)
new_head = reverseList_recurrsive(head)
print(new_head)