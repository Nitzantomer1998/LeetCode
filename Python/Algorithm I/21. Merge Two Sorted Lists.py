class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    
    solution_nodelist = ListNode()
    current_node = solution_nodelist

    while list1 and list2:

        if list1.value < list2.value:

            current_node.next = list1

            list1 = list1.next

        else:

            current_node.next = list2

            list2 = list2.next

        current_node = current_node.next

    if list1:
        current_node.next = list1

    if list2:
        current_node.next = list2

    return solution_nodelist.next
