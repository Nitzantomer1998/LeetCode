/**
 * Definition for singly-linked list.
 * @class ListNode
 * @property {number} val - The value of the node.
 * @property {ListNode | null} next - The next node in the linked list.
 * @constructor Create a ListNode.
 * @param {number} [val] - The value of the node.
 * @param {ListNode | null} [next] - The next node in the linked list.
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
 * Finds the middle node of a linked list.
 * @param {ListNode | null} head - The head node of the linked list.
 * @returns {ListNode | null} The middle node of the linked list.
 */
function middleNode(head: ListNode | null): ListNode | null {
  let fastTraverse: ListNode | null = head;
  let slowTraverse: ListNode | null = head;

  while (slowTraverse && fastTraverse && fastTraverse.next) {
    fastTraverse = fastTraverse.next.next;
    slowTraverse = slowTraverse.next;
  }

  return slowTraverse;
}
