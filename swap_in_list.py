class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if head.next == None:
            return head
        node = head
        data = [node]
        while node.next:
            node = node.next
            data.append(node)
        if len(data) == 2 and k == 2:
            first = data[0]
            last = data[1]
            last.next = first
            first.next = None
            head = last
            return head
        from_first = data[k - 1]
        from_first_next = from_first.next
        if k - 2 >= 0:
            from_first_previous = data[k - 2]
        else:
            from_first_previous = None

        from_last = data[-k]
        from_last_next = from_last.next
        if (-k -1) + len(data) >= 0:
            from_last_previous = data[-k-1]
        else:
            from_last_previous = None

        if from_last.next == from_first:
            from_first.next = from_last
            from_last.next = from_first_next
            if from_last_previous is not None:
                from_last_previous.next = from_first
            return head
        if from_first.next is not from_last:
            from_first.next = from_last_next
            if from_last_previous is not None:
                from_last_previous.next = from_first
            else:
                head = from_first

            from_last.next = from_first_next
            if from_first_previous is not None:
                from_first_previous.next = from_last
            else:
                head = from_last
        else:
            from_first.next = from_last.next 

            from_last.next = from_first
            if from_first_previous is not None:
                from_first_previous.next = from_last
            else:
                head = from_last

        return head


x = [55,60,78,53,93,37,31,4,61,11,13,51,34,83,24,96,5,77,1,67]
def gen_linked_list(i):
    if i < len(x):
        if i + 1 == len(x):
            return ListNode(x[i])
        else:
            return ListNode(x[i], next=gen_linked_list(i+1))
        
head = gen_linked_list(0)

solution = Solution()
print(solution.swapNodes(head, 11))