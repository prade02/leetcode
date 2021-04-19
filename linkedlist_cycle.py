"""
Approach 1: with additional memory. use set to hold nodes. iterate through the linkedlist, each time check if the node present in the set, if not add to the set and 
continue. when a node is found in the set, means i am seeing a node which is already a node i came across - so it is a cycle - return true. if the iteration succeeds 
then return false as we did not find any node in the set.

Approach 2: not recommended. no additional memory, iterate through the linked list, check if the node if present anywhere between head and before this node - means i am seeing 
a node that node is already present in the past iteration. if i see a node with next as `None` - means i reached end of linkedlist and there is no cycle. the problem with this approach is it takes time. if the number of nodes increases, the number of iteration
increases.

Approach 3: using slow and fast runner. no addtional memory. start 2 runners at different speed - slow with one hop at a time, fast with 2 hops at a time. if there is a
 cycle, the fast runner will meet the slow runner at a point. for ex: if we have 10 nodes and the 10th node point to first node. then at the end of 10 iterations,
 slow and fast runner will be in the same position - confirming the cycle. if there is no cycle, fast would reach a node which has next as null - confirming there is no
 cycle.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linkedlist_cycle(lt, pos):
    previous = head = None
    nodes = []
    for item in lt:
        current = ListNode(item)
        nodes.append(current)
        if head is None:
            head = current
        if previous is not None:
            previous.next = current
        previous = current
    if pos != -1:
        current.next = nodes[pos]
    return head


def hasCycle_v1(head):
    history = set()
    while head:
        if head in history:
            return True
        history.add(head)
        head = head.next
    return False


def hasCycle_v2(head):
    current = head
    node_index = 0
    while current:
        node_index += 1
        check_index = 0
        temp = head 
        while temp:
            check_index += 1
            if check_index == node_index:
                break
            if temp is current:
                return True
            temp = temp.next
        current = current.next
    return False


def hasCycle_v3(head):
    if not head or not head.next:
        return False
    slow_runner = head
    fast_runner = head.next
    """ while slow_runner != fast_runner:
        if fast_runner is None or fast_runner.next is None:
            return False
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next 
    return True """
       
    while fast_runner is not None and fast_runner.next is not None:
        if slow_runner == fast_runner:
            return True
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
    return False

x = [1,2,3,4,5]
head = create_linkedlist_cycle(x, -1)
print(hasCycle_v3(head))