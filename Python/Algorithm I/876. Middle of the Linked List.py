class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def middle_node(head: ListNode) -> ListNode:
    
    solution_node = head

    while head and head.next:
        head = head.next.next

        solution_node = solution_node.next

    return solution_node
