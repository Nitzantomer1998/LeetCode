class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root, False)

    def DFS(self, root: Optional[TreeNode], isLeft: bool) -> int:
        if root is None:
            return 0

        if isLeft and root.left is None and root.right is None:
            return root.val

        return self.DFS(root.left, True) + self.DFS(root.right, False)
