# Class provided by LeetCode for the following problem
class TreeNode:
    def __init__(self, value: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.value = value
        self.left = left
        self.right = right


def is_subtree(tree: 'TreeNode', sub_tree: 'TreeNode') -> bool:
    """
    Finding if the sent "sub_tree" exist in the sent "tree", and return accordingly

    :param tree: TreeNode
    :param sub_tree: TreeNode
    :return: True if the trees are identical, else False

    Time Complexity: o(|tree| * min(|tree|, |sub_tree|)
    Space Complexity: o(|tree| + |sub_tree|)
    """
    # if "sub_tree" is None then it's definitely a part of tree
    if sub_tree is None:
        return True

    # if tree is None then it's can't have a subtree, expect the case of empty tree which been handled before
    if tree is None:
        return False

    # Assisting function to make the DFS calls
    def is_trees_identical(p: TreeNode, q: TreeNode) -> bool:
        """
        Checking if the sent trees are identical using DFS algorithm, and return accordingly

        :param p: TreeNode
        :param q: TreeNode
        :return: True if the trees are identical, else False
        """
        # if both trees exist
        if p and q:
            # Returning True/False using recursive call for the subtree of both of them
            return p.value == q.value and is_trees_identical(p.left, q.left) and is_trees_identical(p.right, q.right)

        # if we reach to here, means one or more of the trees is None
        # Return True if both of them None, else False
        return p is q

    # if "sub_tree" is identical to "tree", Return True
    if is_trees_identical(tree, sub_tree):
        return True

    # 2 Callbacks for each child of the current node for checking the possibility of a "sub_tree"
    return is_subtree(tree.left, sub_tree) or is_subtree(tree.right, sub_tree)
