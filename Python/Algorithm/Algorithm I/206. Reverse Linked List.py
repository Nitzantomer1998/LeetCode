from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly-linked list in-place.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The head of the reversed linked list.

        Time Complexity: o(n) where n is the length of the linked list.
        Space Complexity: o(1) since we are not using any additional space.
        """
        previousNode = None
        currentNode = head

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode

            previousNode = currentNode
            currentNode = nextNode

        return previousNode
