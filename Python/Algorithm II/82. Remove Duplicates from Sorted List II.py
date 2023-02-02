class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def delete_duplicates(head: ListNode) -> ListNode:
    
    solution_nodelist = ListNode(next=head)

    previous_node = solution_nodelist
    current_node = head

    while current_node and current_node.next:

        if current_node.value != current_node.next.value:
            previous_node = current_node
            current_node = current_node.next

        else:

            while current_node.next and current_node.value == current_node.next.value:
                current_node = current_node.next

            previous_node.next = current_node.next
            current_node = current_node.next

    return solution_nodelist.next
