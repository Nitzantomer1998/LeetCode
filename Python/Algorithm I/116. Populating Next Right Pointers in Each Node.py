# Class provided by LeetCode for the following problem
class Node:
    def __init__(self, value: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    """
    Populate each next pointer to point to its next right node if exists, else null, and return the perfect binary tree

    :param root: Root node of a perfect binary tree
    :return: The modified perfect binary tree

    Time Complexity: o(n)
    Space Complexity: o(1)
    """

    # Assisting function to make the DFS calls
    def updating_node_next_pointer(root: 'Node') -> 'Node':
        """
        Recursive function for modifying each node next pointer using DFS Algorithm

        :param root: Node
        :return: The updated root / node next pointer
        """
        # if the current node has a left child
        if root and root.left:

            # Making 2 recursive callback for each child of the current node
            left = updating_node_next_pointer(root.left)
            right = updating_node_next_pointer(root.right)

            # While loop for updating the next pointer
            while left:
                # Updating the next pointer
                left.next = right

                # Updating the nodes
                left = left.right
                right = right.left

        # Returning the modified current node
        return root

    # Calling for the recursive call which modified the tree next pointers, and return it
    return updating_node_next_pointer(root)
