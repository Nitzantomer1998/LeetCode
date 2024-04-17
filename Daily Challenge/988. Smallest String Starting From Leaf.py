class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        paths = []
        self.DFS(root, '', paths)
        return min(paths)

    def DFS(self, node: Optional[TreeNode], currentPath: str, paths) -> None:
        if node is None:
            return

        currentPath += chr(97 + node.val)

        if node.left is None and node.right is None:
            paths.append(currentPath[::-1])
            return

        self.DFS(node.left, currentPath, paths)
        self.DFS(node.right, currentPath, paths)
