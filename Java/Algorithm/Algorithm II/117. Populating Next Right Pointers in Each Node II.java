import java.util.LinkedList;
import java.util.Queue;

/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

/**
 * Connects each node in a binary tree to its right neighbor.
 *
 * @param root The root node of the binary tree.
 * @return The root node of the modified binary tree with connected neighbors.
 */
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
