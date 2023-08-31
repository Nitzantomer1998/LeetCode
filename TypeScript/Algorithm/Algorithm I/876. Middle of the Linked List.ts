function middleNode(head: ListNode | null): ListNode | null {
  let fastTraverse: ListNode | null = head;
  let slowTraverse: ListNode | null = head;

  while (slowTraverse && fastTraverse && fastTraverse.next) {
    fastTraverse = fastTraverse.next.next;
    slowTraverse = slowTraverse.next;
  }

  return slowTraverse;
}
