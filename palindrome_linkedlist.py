"""
Approach 1: use additional memory. iterate though the linked list and add the value of each node to a list. check if the list and the reversed version are same

Approach 2: no additional memory. use fast and slow runner - an approach where the length is unknown. let the runners start slow is one at a time progresser, fast is two
 at a time progresser. when fast reaches the end, slow would have completed half way - so this gives the mid. the node after the slow runner will be the start of second
 half. take this node as head of second half and reverse the linked list. if linked list of first half(head till slow node) is same as second half(second head till end)
 then it is a palindrome.
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


def isPalindrome_v1(head):
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


def isPalindrome_v2(head):
    # function to reverse a linkedlist and return new head -> last node of original linkedlist
    def reverse_linkedlist(head):
        previous = None
        while head:
            head.next, head, previous = previous, head.next, head
        return previous
    if not head or not head.next:
        return True
    slow_runner = head
    fast_runner = head.next
    while fast_runner and fast_runner.next:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
    #reverse the second half of the linkedlist
    second_half_head = reverse_linkedlist(slow_runner.next)
    reference_1 = head
    reference_2 = second_half_head
    while reference_2:
        if reference_1.val != reference_2.val:
            return False
        reference_1 = reference_1.next
        reference_2 = reference_2.next
    return True

x = [1,2]
x = create_linkedlist(x)
print(isPalindrome_v2(x))