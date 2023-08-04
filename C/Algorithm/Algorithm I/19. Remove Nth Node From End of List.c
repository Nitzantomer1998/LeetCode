/*
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/*
 * Computes the length of a singly-linked list.
 *
 * The 'getNodeListLength' function calculates the number of nodes in a singly-linked
 * list by traversing the list and incrementing the length counter for each node
 * encountered. It takes a pointer to the head of the list as a parameter.
 *
 * Parameters:
 * - head: A pointer to the head node of the singly-linked list.
 *
 * Returns:
 * The length of the singly-linked list.
 *
 * This function traverses the linked list while counting the nodes and returns the
 * total number of nodes in the list.
 */
int getNodeListLength(struct ListNode* head) {
	struct ListNode* traverse = head;
	int listNodeLength = 0;

	while (traverse) {
		traverse = traverse->next;
		listNodeLength++;
	}

	return listNodeLength;
}

/*
 * Removes the nth node from the end of a singly-linked list.
 *
 * The 'removeNthFromEnd' function removes the nth node from the end of a singly-linked
 * list. It calculates the length of the list using the 'getNodeListLength' function and
 * determines the index of the node to be removed. It then traverses the list to find the
 * node before the one to be removed and adjusts the 'next' pointers to skip the targeted
 * node.
 *
 * Parameters:
 * - head: A pointer to the head node of the singly-linked list.
 * - n: The index of the node to be removed from the end (1-based index).
 *
 * Returns:
 * A pointer to the head of the modified singly-linked list after removing the nth node
 * from the end.
 *
 * Special cases are handled: if the list has only one node and n is 1, the function
 * returns NULL. If n equals the length of the list, the function returns the second
 * node as the new head.
 */
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
