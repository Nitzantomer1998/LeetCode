import collections
from typing import Optional


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Connect nodes at the same level in a binary tree with a next pointer.

        Args:
            root (Optional[Node]): The root node of the binary tree.

        Returns:
            Optional[Node]: The root node of the modified binary tree with next pointers.

        Time Complexity: o(n) where n is the number of nodes in the binary tree.
        Space Complexity: o(n) where n is the number of nodes in the binary tree.
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
