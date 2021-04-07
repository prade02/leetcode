class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


x = [1,2,3,4]
def gen_linked_list(i):
    if i < len(x):
        if i + 1 == len(x):
            return LinkedList(x[i])
        else:
            return LinkedList(x[i], next=gen_linked_list(i+1))
        
head = gen_linked_list(0)


def print_linkedlist(head):
    node = head
    lt = []
    while node is not None:
        lt.append(str(node.value))
        node = node.next
    print(' -> '.join(lt))

# 1 -> 2 -> 3 -> 4
# 4 -> 3 -> 2 -> 1
def reverse_linkedlist(head):
    current = head
    previous = None
    while current.next is not None:
        current.next, previous, current = previous, current, current.next
    head, current.next = current, previous
    return head

print_linkedlist(head)
head = reverse_linkedlist(head)
print_linkedlist(head)