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
   * Finds the middle node of a singly-linked list.
   *
   * @param head The head of the linked list.
   * @return The middle node of the linked list.
   */
  public ListNode middleNode(ListNode head) {
    ListNode fastList = head;
    ListNode slowList = head;

    while (fastList != null && fastList.next != null) {
      fastList = fastList.next.next;
      slowList = slowList.next;
    }

    return slowList;
  }
}
