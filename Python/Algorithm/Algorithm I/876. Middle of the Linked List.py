# Class provided by LeetCode for the following problem
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def middle_node(head: ListNode) -> ListNode:
    """
    Iterate the ListNode, and return the middle node of the sent ListNode

    :param head: ListNode
    :return: The middle node of the sent ListNode

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Storing the middle node (the solution)
    solution_node = head

    # Loop to traverse the ListNode
    # Note: every 2 steps forwards of head node, will require the solution node to move forward once
    while head and head.next:
        # Updating the head, to jump 2 steps forwards
        head = head.next.next

        # Updating the solution node to move 1 step forward
        solution_node = solution_node.next

    # Returning the solution node
    return solution_node
