import collections


class Node:
    def __init__(self, value: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    
    queue = collections.deque([root])

    while queue and queue[0]:

        previous_node = None

        for _ in range(len(queue)):

            current_node = queue.popleft()

            if previous_node:
                previous_node.next = current_node

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

            previous_node = current_node

    return root
