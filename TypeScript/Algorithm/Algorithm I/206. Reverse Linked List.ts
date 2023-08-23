function reverseList(head: ListNode | null): ListNode | null {
    let currentNode: ListNode | null = head;
    let previousNode: ListNode | null = null;
    let nextNode: ListNode | null = null;

    while (currentNode) {
        nextNode = currentNode.next;
        currentNode.next = previousNode;

        previousNode = currentNode;
        currentNode = nextNode;
    }

    return previousNode;
};
