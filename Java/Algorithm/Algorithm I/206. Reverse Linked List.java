class Solution {

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
