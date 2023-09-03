/**
 * Definition for singly-linked list.
 * @class ListNode
 * @property {number} val - The value of the node.
 * @property {ListNode | null} next - The reference to the next node.
 * @constructor Create a ListNode.
 * @param {number} [val] - The value of the node.
 * @param {ListNode | null} [next] - The reference to the next node.
 *
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
 * Reverses a singly-linked list.
 * @param {ListNode | null} head - The head node of the linked list to be reversed.
 * @returns {ListNode | null} The head of the reversed linked list.
 */
function reverseList(head: ListNode | null): ListNode | null {
  let currentNode: ListNode | null = head;
  let previousNode: ListNode | null = null;
  let nextNode: ListNode | null = null;

  while (currentNode) {
    nextNode = currentNode.next;
    currentNode.next = previousNode;

    previousNode = currentNode;
    currentNode = nextNode;
  }

  return previousNode;
}
