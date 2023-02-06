import collections


# Class provided by LeetCode for the following problem
class Node:
    def __init__(self, value: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    """
    Populate each next pointer to point to its next right node if exists, else null, and return the binary tree
    Note : using bfs algorithm

    :param root: Root node of a binary tree
    :return: The modified binary tree

    Time Complexity: o(n)
    Space Complexity: o(log(n))
    """
    # dequeue for bfs algorithm, Initialize with the root of the tree
    queue = collections.deque([root])

    # while loop for updating each level of node in the binary tree, queue[0] in order to avoid empty tree
    while queue and queue[0]:

        # Node storing the left node of the current iteration
        # Note : First node in each level is always None
        previous_node = None

        # Loop to update every node in this current binary tree level
        for _ in range(len(queue)):

            # Getting the first node from the queue
            current_node = queue.popleft()

            # if the previous node isn't None, means we need to update the previous next pointer to be the current node
            if previous_node:
                previous_node.next = current_node

            # if the current node has a left child, add it to the queue
            if current_node.left:
                queue.append(current_node.left)

            # if the current node has a right child, add it to the queue
            if current_node.right:
                queue.append(current_node.right)

            # Update the previous node to be the current for the next iteration
            previous_node = current_node

    # Return the modified binary tree
    return root
