class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root, False)

    def DFS(self, node: Optional[TreeNode], isLeft: bool) -> int:
        if node is None:
            return 0

        if isLeft and node.left is None and node.right is None:
            return node.val

        return self.DFS(node.left, True) + self.DFS(node.right, False)
        
