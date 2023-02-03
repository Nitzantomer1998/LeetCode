# Class provided by LeetCode for the following problem
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    """
    Reversing the ListNode, and return it

    :param head: ListNode
    :return: The reversed ListNode

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Storing the current node
    current_node = head

    # Storing the previous node
    previous_node = None

    # Loop to traverse the ListNode
    while current_node:
        # Save the next node
        next_node = current_node.next

        # Update the current_node next pointer to be the previous node
        current_node.next = previous_node

        # Update the previous and current nodes, for the next iteration
        previous_node = current_node
        current_node = next_node

    # Return the new head of the ListNode
    return previous_node
