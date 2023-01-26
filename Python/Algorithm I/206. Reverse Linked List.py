class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
  
    current_node = head

    previous_node = None

    while current_node:
        next_node = current_node.next

        current_node.next = previous_node

        previous_node = current_node
        current_node = next_node

    return previous_node
