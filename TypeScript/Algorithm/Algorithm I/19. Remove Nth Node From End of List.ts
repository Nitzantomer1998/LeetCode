/**
 * Definition for singly-linked list.
 * @class ListNode
 * @property {number} val - The value of the node.
 * @property {ListNode | null} next - The reference to the next node.
 * @constructor Create a ListNode.
 * @param {number} [val] - The value of the node.
 * @param {ListNode | null} [next] - The reference to the next node.
 
* class ListNode {
*     val: number;
*     next: ListNode | null;
*     constructor(val?: number, next?: ListNode | null) {
*         this.val = (val === undefined ? 0 : val);
*         this.next = (next === undefined ? null : next);
*     }
* }
*/

/**
 * Returns the length of a given singly-linked list.
 * @param {ListNode | null} head - The head node of the linked list.
 * @returns {number} The length of the linked list.
 */
function getListNodeLength(head: ListNode | null): number {
  let listNodeLength: number = 0;

  while (head) {
    listNodeLength++;
    head = head.next;
  }

  return listNodeLength;
}

/**
 * Removes the nth node from the end of a singly-linked list.
 * @param {ListNode | null} head - The head node of the linked list.
 * @param {number} n - The position of the node to be removed from the end.
 * @returns {ListNode | null} The head of the linked list after removal.
 */
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let traverse: ListNode | null = head;

  let listNodeLength: number = getListNodeLength(head);
  let deleteNodeIndex: number = listNodeLength - n - 1;

  if (listNodeLength === 1 && n === 1) return null;
  if (listNodeLength === n && head) return head.next;

  while (deleteNodeIndex && traverse) {
    traverse = traverse.next;
    deleteNodeIndex--;
  }

  if (traverse && traverse.next) traverse.next = traverse.next.next;

  return head;
}
