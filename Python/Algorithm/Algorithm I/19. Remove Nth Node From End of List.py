from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the n-th node from the end of a linked list.

        Args:
            head (Optional[ListNode]): The head of the linked list.
            n (int): The position of the node to be removed from the end.

        Returns:
            Optional[ListNode]: The head of the modified linked list.

        Time Complexity: o(n) where n is the length of the linked list.
        Space Complexity: o(1)
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next if slow.next else None

        return dummy.next
