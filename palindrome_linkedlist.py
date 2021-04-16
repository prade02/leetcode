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


def isPalindrome(head):
    stack = []
    main = head
    while head:
        stack.append(head.val)
        head = head.next
    """ head = main
    while head:
        if head.val != stack.pop():
            return False
        head = head.next """
    if stack == stack[::-1]:
        return True
    return False


x = [1,2]
x = create_linkedlist(x)
print(isPalindrome(x))