import collections


# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Connect nodes at the same level in a binary tree with a next pointer.

        Args:
            root (Node): The root node of the binary tree.

        Returns:
            Node: The root node of the modified binary tree with next pointers.
        """
        queue = collections.deque([root])

        while queue and queue[0]:
            currentLevel = len(queue)

            for level in range(currentLevel):
                currentNode = queue.popleft()

                if level < currentLevel - 1:
                    currentNode.next = queue[0]

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

        return root
