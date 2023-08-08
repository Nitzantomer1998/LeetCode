/*
 * Reverses a singly-linked list in-place.
 *
 * The 'reverseList' function takes the head node of a singly-linked list as input and
 * reverses the order of its nodes in-place. It iterates through the list, reversing the
 * direction of the 'next' pointers for each node. At the end of the reversal process,
 * the head of the reversed list becomes the previous tail node.
 *
 * Parameters:
 * - head: A pointer to the head node of the singly-linked list to be reversed.
 *
 * Returns:
 * A pointer to the new head node of the reversed singly-linked list.
 *
 * This function efficiently reverses the linked list by maintaining three pointers:
 * 'prevNode', 'currentNode', and 'nextNode'. The 'nextNode' variable stores the next
 * node in the original list before it is updated. The 'currentNode' pointer is updated
 * to point to the previous node, and the 'prevNode' pointer is used to keep track of
 * the reversed list's tail. Once the iteration is complete, the reversed list's head is
 * 'prevNode', and it is returned as the new head of the reversed list.
 */
struct ListNode* reverseList(struct ListNode* head) {
   struct ListNode* prevNode = NULL;
   struct ListNode* currentNode = head;
   struct ListNode* nextNode = NULL;

   while (currentNode) {
       nextNode = currentNode->next;
       currentNode->next = prevNode;
       
       prevNode = currentNode;
       currentNode = nextNode;
   }

   return prevNode;
}
