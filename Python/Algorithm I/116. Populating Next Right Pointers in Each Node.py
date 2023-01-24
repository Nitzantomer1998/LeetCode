class Node:
    def __init__(self, value: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    
    def updating_node_next_pointer(root: 'Node') -> 'Node':
        
        if root and root.left:

          
            left = updating_node_next_pointer(root.left)
            right = updating_node_next_pointer(root.right)

            while left:
                left.next = right

                left = left.right
                right = right.left

        return root

    return updating_node_next_pointer(root)
