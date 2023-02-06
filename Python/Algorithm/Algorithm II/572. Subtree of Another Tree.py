class TreeNode:
    def __init__(self, value: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.value = value
        self.left = left
        self.right = right


def is_subtree(tree: 'TreeNode', sub_tree: 'TreeNode') -> bool:
    
    if sub_tree is None:
        return True

    if tree is None:
        return False

    def is_trees_identical(p: TreeNode, q: TreeNode) -> bool:
       
        if p and q:
            return p.value == q.value and is_trees_identical(p.left, q.left) and is_trees_identical(p.right, q.right)

        return p is q

    if is_trees_identical(tree, sub_tree):
        return True

    return is_subtree(tree.left, sub_tree) or is_subtree(tree.right, sub_tree)
