/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Finds the middle node of a singly-linked list.
 *
 * The 'middleNode' function takes a singly-linked list 'head' as input and uses two pointers,
 * 'middleListNode' and 'traverseListNode', to traverse the list. The 'middleListNode' pointer
 * moves at half the pace of the 'traverseListNode' pointer. When the 'traverseListNode' reaches
 * the end of the list, the 'middleListNode' points to the middle node.
 *
 * Parameters:
 * - head: A pointer to the head node of the singly-linked list.
 *
 * Returns:
 * A pointer to the middle node of the singly-linked list.
 */
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
