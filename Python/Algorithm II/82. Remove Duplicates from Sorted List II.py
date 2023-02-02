# Class provided by LeetCode for the following problem
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def delete_duplicates(head: ListNode) -> ListNode:
    """
    Delete all the duplicates value nodes in head NodeList, and return it

    :param head: Sorted ListNode with duplicates values
    :return: The updated ListNode that each node value is distinct and sorted

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Variable to traverse and update the head ListNode
    solution_nodelist = ListNode(next=head)

    # Pointers to hold the previous and current nodes
    previous_node = solution_nodelist
    current_node = head

    # Loop to traverse the whole ListNode
    while current_node and current_node.next:

        # if the current node value is unique then add it to the solution ListNode, and update the pointers
        if current_node.value != current_node.next.value:
            previous_node = current_node
            current_node = current_node.next

        # if the current node value is a duplicate, iterate the ListNode till we pass all the duplicates
        else:

            # Loop to update current_node to be the last duplicate node with the value of the current_node.value
            while current_node.next and current_node.value == current_node.next.value:
                current_node = current_node.next

            # Updating the pointers
            previous_node.next = current_node.next
            current_node = current_node.next

    # Returning ListNode without duplicates
    return solution_nodelist.next
