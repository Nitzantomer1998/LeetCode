class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root, 0)

    def DFS(self, node: Optional[TreeNode], currentSum: int) -> int:
        if node is None:
            return 0

        newSum = currentSum * 10 + node.val
        if node.left is None and node.right is None:
            return newSum

        return self.DFS(node.left, newSum) + self.DFS(node.right, newSum)
