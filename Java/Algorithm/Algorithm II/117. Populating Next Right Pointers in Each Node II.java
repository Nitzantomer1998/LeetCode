import java.util.LinkedList;
import java.util.Queue;

class Solution {

  public Node connect(Node root) {
    Queue<Node> queue = new LinkedList<>();
    queue.offer(root);

    while (queue.peek() != null) {
      int currentLevel = queue.size();

      for (int level = 0; level < currentLevel; level++) {
        Node currentNode = queue.poll();

        if (level < currentLevel - 1) 
          currentNode.next = queue.peek();
        
        if (currentNode.left != null) 
          queue.offer(currentNode.left);
        
        if (currentNode.right != null) 
          queue.offer(currentNode.right);
      }
    }

    return root;
  }
}
