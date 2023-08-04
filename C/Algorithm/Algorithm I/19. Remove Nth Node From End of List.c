int getNodeListLength(struct ListNode* head) {
	struct ListNode* traverse = head;
	int listNodeLength = 0;

	while (traverse) {
		traverse = traverse->next;
		listNodeLength++;
	}

	return listNodeLength;
}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* traverse = head;
	int listNodeLength = getNodeListLength(head);
    int deleteIndex = listNodeLength - n - 1;

	if (listNodeLength == 1 && n == 1) return NULL;
    
    if (listNodeLength == n) return head -> next;

	while (deleteIndex > 0) {
		traverse = traverse->next;
		deleteIndex--;
	}

	traverse->next = traverse->next->next;
	return head;
}
