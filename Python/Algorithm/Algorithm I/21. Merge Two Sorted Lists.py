from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into a new sorted linked list.

        Args:
            list1 (Optional[ListNode]): The head of the first sorted linked list.
            list2 (Optional[ListNode]): The head of the second sorted linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.

        Time Complexity: o(n) where n is the length of the longer linked list.
        Space Complexity: o(1)
        """
        mergedList = ListNode(0)
        buildMergedList = mergedList

        while list1 and list2:
            if list1.val < list2.val:
                buildMergedList.next = list1
                list1 = list1.next

            else:
                buildMergedList.next = list2
                list2 = list2.next

            buildMergedList = buildMergedList.next

        buildMergedList.next = list1 or list2

        return mergedList.next
