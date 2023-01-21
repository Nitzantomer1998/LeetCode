# Class provided by LeetCode for the following problem
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
   
    short_nodelist = long_nodelist = head

    for _ in range(n):
        long_nodelist = long_nodelist.next

    if long_nodelist is None:
        return head.next

    while long_nodelist.next:
        long_nodelist = long_nodelist.next
        short_nodelist = short_nodelist.next

    short_nodelist.next = short_nodelist.next.next

    return head
