from typing import Optional


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Merges two binary trees by summing up corresponding nodes.

        Args:
            root1: The root of the first binary tree.
            root2: The root of the second binary tree.

        Returns:
            The root of the merged binary tree.

        Time Complexity: o(n), where n is the total number of nodes in the smaller of the two trees.
        Space Complexity: o(n), where n is the maximum height of the smaller of the two trees.
        """
        if root1 and root2:
            mergedTree = TreeNode(root1.val + root2.val)
        
            mergedTree.left = self.mergeTrees(root1.left, root2.left)
            mergedTree.right = self.mergeTrees(root1.right, root2.right)

        else:
            mergedTree = root1 if root1 else root2

        return mergedTree
