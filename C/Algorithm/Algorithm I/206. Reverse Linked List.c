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
