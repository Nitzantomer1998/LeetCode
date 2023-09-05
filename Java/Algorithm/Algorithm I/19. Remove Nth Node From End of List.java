class Solution {

  private int getListNodeLength(ListNode head) {
    int listNodeLength = 0;

    while (head != null) {
      head = head.next;
      listNodeLength++;
    }

    return listNodeLength;
  }

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
