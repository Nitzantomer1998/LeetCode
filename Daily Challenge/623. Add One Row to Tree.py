class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        return self.Helper(root, val, depth, 1)

    def Helper(self, node: TreeNode, value: int, depth: int, currDepth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(value, node, None)

        if node is None:
            return node

        if currDepth == depth - 1:
            leftNode = node.left
            rightNode = node.right

            node.left = TreeNode(value, None, None)
            node.right = TreeNode(value, None, None)

            node.left.left = leftNode
            node.right.right = rightNode
            return node

        node.left = self.Helper(node.left, value, depth, currDepth + 1)
        node.right = self.Helper(node.right, value, depth, currDepth + 1)

        return node
        