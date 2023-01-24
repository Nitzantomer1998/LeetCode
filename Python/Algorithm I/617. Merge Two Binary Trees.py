class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def merge_trees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    
    def recursive_root_creator(root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        if root1 and root2:
            root = TreeNode(root1.value + root2.value)
            
            root.left = recursive_root_creator(root1.left, root2.left)
            root.right = recursive_root_creator(root1.right, root2.right)

            return root

        else:
            return root1 or root2

    return recursive_root_creator(root1, root2)
