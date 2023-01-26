# Class provided by LeetCode for the following problem
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merging the two lists in a one sorted list, and return it

    :param list1: Sorted ListNode
    :param list2: Sorted ListNode
    :return: The merged ListNode

    Time Complexity: o(n + m)
    Space Complexity: o(n + m)
    """
    # Storing the ListNode head (Solution), and a pointer to the current node
    solution_nodelist = ListNode()
    current_node = solution_nodelist

    # Loop to traverse the lists, and updating the solution list
    while list1 and list2:

        # if the list1 node is lower than list2 node
        if list1.value < list2.value:

            # Updating the next node value
            current_node.next = list1

            # Updating the list1 next pointer
            list1 = list1.next

        # if the list2 node is lower than list1 node
        else:

            # Updating the next node value
            current_node.next = list2

            # Updating the list2 next pointer
            list2 = list2.next

        # Updating the solution node next pointer
        current_node = current_node.next

    # Edge case: list2 is None, therefor the current_node.next equal to the rest of list1
    if list1:
        current_node.next = list1

    # Edge case: list1 is None, therefor the current_node.next equal to the rest of list2
    if list2:
        current_node.next = list2

    # Returning the creating nodelist solution
    return solution_nodelist.next
