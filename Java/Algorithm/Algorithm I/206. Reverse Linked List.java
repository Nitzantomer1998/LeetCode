/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

  /**
   * Reverses a singly-linked list in place.
   *
   * @param head The head node of the linked list to be reversed.
   * @return The head node of the reversed linked list.
   */
  public ListNode reverseList(ListNode head) {
    ListNode currentNode = head;
    ListNode previousNode = null;

    while (currentNode != null) {
      ListNode tempNode = currentNode.next;
      currentNode.next = previousNode;

      previousNode = currentNode;
      currentNode = tempNode;
    }

    return previousNode;
  }
}
