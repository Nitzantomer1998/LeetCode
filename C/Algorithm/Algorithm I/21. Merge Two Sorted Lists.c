/*
 * Merges two sorted singly-linked lists into a single sorted list.
 *
 * The 'mergeTwoLists' function takes two pointers to the heads of two sorted
 * singly-linked lists, 'list1' and 'list2', as input. It merges the two lists into a
 * single sorted list in ascending order, using a new merged list that is constructed
 * iteratively. The function compares the values of nodes from 'list1' and 'list2', and
 * appends the smaller value node to the merged list. The merged list is built using the
 * 'mergedList' pointer, and the function returns a pointer to the head of the merged
 * list.
 *
 * Parameters:
 * - list1: A pointer to the head node of the first sorted singly-linked list.
 * - list2: A pointer to the head node of the second sorted singly-linked list.
 *
 * Returns:
 * A pointer to the head node of the merged sorted singly-linked list.
 *
 * This function efficiently merges the two sorted lists by iterating through both lists
 * and selectively appending nodes to the merged list. The final merged list contains
 * all elements from both input lists in sorted order.
 */
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
