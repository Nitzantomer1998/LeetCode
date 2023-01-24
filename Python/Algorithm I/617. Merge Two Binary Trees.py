# Class provided by LeetCode for the following problem
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def merge_trees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """
    Merging the two binary trees into a new binary tree "super" tree, and return it

    :param root1: TreeNode representing binary tree
    :param root2: TreeNode representing binary tree
    :return: The merged "super" tree

    Time Complexity: o(max(n, m))
    Space Complexity: o(max(n + m))
    """

    # Assisting function to make the DFS calls
    def recursive_root_creator(root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        Recursive function for creating "super" binary tree from two TreeNode  using DFS Algorithm

        :param root1: TreeNode representing binary tree
        :param root2: TreeNode representing binary tree
        :return: The "super" tree
        """
        # if both roots exists, combine their values and create a new "super" node
        if root1 and root2:
            root = TreeNode(root1.value + root2.value)

            # After creating a root, follow up by 2 recursive callbacks, for adding the left and right children's
            root.left = recursive_root_creator(root1.left, root2.left)
            root.right = recursive_root_creator(root1.right, root2.right)

            # Finally return this "super" node
            return root

        # if one of the nodes exist, it will return it, else will return None
        else:
            return root1 or root2

    # Calling for the recursive call which create the "super" tree, and return it
    return recursive_root_creator(root1, root2)
