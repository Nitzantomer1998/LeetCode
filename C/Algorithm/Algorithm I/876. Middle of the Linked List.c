struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode* middleListNode = head;
    struct ListNode* traverseListNode = head;

    while (traverseListNode) {
        if (traverseListNode->next) {
            traverseListNode = traverseListNode->next->next;
            middleListNode = middleListNode->next;
        }

        else
            traverseListNode = traverseListNode->next;
    }
    return middleListNode;
}
