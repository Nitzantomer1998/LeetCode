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
   * Calculates the length of a singly-linked list.
   *
   * @param head The head node of the linked list.
   * @return The length of the linked list.
   */
  private int getListNodeLength(ListNode head) {
    int listNodeLength = 0;

    while (head != null) {
      head = head.next;
      listNodeLength++;
    }

    return listNodeLength;
  }

  /**
   * Removes the nth node from the end of a singly-linked list.
   *
   * @param head The head node of the linked list.
   * @param n    The position of the node to remove from the end.
   * @return The head node of the modified linked list.
   */
  public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode traverse = head;

    int listNodeLength = this.getListNodeLength(head);
    int deleteNextNodeIndex = listNodeLength - n - 1;

    if (listNodeLength == 1 && n == 1) return null;
    else if (listNodeLength == n) return head.next;

    while (deleteNextNodeIndex > 0) {
      traverse = traverse.next;
      deleteNextNodeIndex--;
    }

    traverse.next = traverse.next.next;
    
    return head;
  }
}
