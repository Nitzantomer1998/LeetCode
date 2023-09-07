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
   * Merges two sorted singly-linked lists into one sorted singly-linked list.
   *
   * @param list1 The head node of the first sorted linked list.
   * @param list2 The head node of the second sorted linked list.
   * @return The head node of the merged sorted linked list.
   */
  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode head = new ListNode();
    ListNode mergedList = head;

    while (list1 != null && list2 != null) {
      if (list1.val < list2.val) {
        mergedList.next = list1;
        list1 = list1.next;
      } 
      
      else {
        mergedList.next = list2;
        list2 = list2.next;
      }

      mergedList = mergedList.next;
    }

    if (list1 != null) mergedList.next = list1;
    if (list2 != null) mergedList.next = list2;

    return head.next;
  }
}
