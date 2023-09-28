from typing import Optional
import collections


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Connect nodes at the same level in a binary tree with a next pointer.

        Args:
            root (Optional[Node]): The root node of the binary tree.

        Returns:
            Optional[Node]: The root node of the modified binary tree with next pointers.
        """
        queue = collections.deque([root])

        while queue and queue[0]:
            level = len(queue)

            for currentLevel in range(level):
                currentNode = queue.popleft()

                if currentLevel < level - 1:
                    currentNode.next = queue[0]

                if currentNode.left and currentNode.right:
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)

        return root
