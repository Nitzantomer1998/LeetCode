# Class provided by LeetCode for the following problem
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    Removing the nth node from the end of the list, and return its head

    :param head: ListNode
    :param n: Integer represent the nth node from the end of the list that we need to remove
    :return: The head of the modified list node

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # ListNodes pointing to the head
    short_nodelist = long_nodelist = head

    # Pushing the long ListNode n steps ahead to create a gap of n nodes with the short ListNode
    for _ in range(n):
        # Skipping the first n nodes of the long nodelist, if exist
        long_nodelist = long_nodelist.next

    # if after we create the gap we need, the next node isn't exist, return the special case solution
    if long_nodelist is None:
        return head.next

    # After we create the needed gap between the lists, we continue by moving both of them forward, until the long
    # list reach to its end, than we stop and know that the next node of the short list need to be skipped
    while long_nodelist.next:
        long_nodelist = long_nodelist.next
        short_nodelist = short_nodelist.next

    # The next node is the desire node to be removed, then we update his next pointer to move 2 times forwards
    short_nodelist.next = short_nodelist.next.next

    # Return the modified nodelist
    return head
