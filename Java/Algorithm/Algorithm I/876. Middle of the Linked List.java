class Solution {

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
