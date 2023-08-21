function getListNodeLength(head: ListNode | null): number {
    let listNodeLength: number = 0;
    
    while (head) {
        listNodeLength++;
        head = head.next;
    }

    return listNodeLength;
}

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let traverse: ListNode | null = head;
    let listNodeLength = getListNodeLength(head);
    let deleteNodeIndex: number = listNodeLength - n - 1;

    if (listNodeLength === 1 && n === 1) return null;
    if (listNodeLength === n) return head.next;

    while (deleteNodeIndex) {
        traverse = traverse.next;
        deleteNodeIndex--;
    }

    traverse.next = traverse.next.next;
    return head;
};
