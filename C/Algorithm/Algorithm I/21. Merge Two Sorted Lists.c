struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode head;
    struct ListNode* mergedList = &head;

    while (list1 && list2) {
        if (list1->val < list2->val) {
            mergedList->next = list1;
            mergedList = mergedList->next;
            list1 = list1->next;
        }

        else {
            mergedList->next = list2;
            mergedList = mergedList->next;
            list2 = list2->next;
        }
    }

    if (list1) 
        mergedList->next = list1;
    
    else 
        mergedList->next = list2;

    return head.next;
}
